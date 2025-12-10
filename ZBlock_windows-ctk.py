# ZBlock - A simple adblocker for Windows that works by modifying the hosts file.
# This source code, according to the MIT License, is free to use, modify and distribute. 
# You must include the original copyright and license notice in any copy of the software/source code.
# Feel free to contribute to this project by adding features, improvements or fixing bugs.

# Imports
import threading
import json
from tkinter import messagebox
import shutil
import customtkinter as ctk
import urllib.request
import tempfile
import subprocess
import webbrowser
import os
import re

# Current version of ZBlock (Used by the update checker)
CURRENT_VERSION = "2.0-beta"

def user_interface():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # Disclaimer message.
    messagebox.showinfo(
        "Welcome to ZBlock",
        "We believe that you have read our Wiki and understood how this software works. If not, then please do so. Continuing means that you acknowledge the fact that I AM NOT RESPONSIBLE FOR DAMAGE CAUSED TO THIS COMPUTER."
    )

    root = ctk.CTk()
    root.title("ZBlock V.2.0 - Beta")
    root.geometry("500x215")
    root.resizable(False, False)
    #root.iconbitmap(r"C:\Program files\ObjectiveVirtual\ZBlock\icons\Zblock-icon.ico")
    # Don't forget to uncomment this line when building the exe.

    # Top frame for title and about
    frame = ctk.CTkFrame(root, fg_color="#0B0E0D", corner_radius=0)
    frame.pack(fill="x", side='top', padx=0, pady=(0, 5))

    objectivevirtual = ctk.CTkLabel(
        frame, text="Objective:Virtual", font=("Calibri", 20, "bold"), text_color="#F5F5F5"
    )
    objectivevirtual.pack(side="right", padx=10, pady=10)
    
    block_button = ctk.CTkButton(
        frame, text="Block Ads", command=block_ads, fg_color="#AF3D3D", hover_color="#722727", corner_radius=50
    )
    block_button.pack(side="left", padx=10, pady=10)

    About = ctk.CTkButton(
        frame, text="About ZBlock", command=about, fg_color="#205E88", hover_color="#0B4DB1"
    )
    About.pack(side="left", padx=10, pady=10)

    # Main frame for backup/restore
    frame2 = ctk.CTkFrame(root, fg_color="#242424")
    frame2.pack(pady=10, side='top', fill="x")

    backup_button = ctk.CTkButton(
        frame2, text="Backup Hosts", command=backup_hosts, fg_color="#179456", hover_color="#17A08E", width=20
    )
    backup_button.pack(side='left', padx=20, pady=20)

    update = ctk.CTkButton(
        frame2, text="What's new ?", command=update_info, fg_color="#294F91", hover_color="#26779C"
    )
    update.pack(side='right', padx=20, pady=20)

    restore_button = ctk.CTkButton(
        frame2, text="Restore Hosts and Stop", command=restore_hosts, fg_color="#2C6DB8", hover_color="#0E3988"
    )
    restore_button.pack(side='right')

    copyright = ctk.CTkLabel(
        root,
        text="©2025 Anir El Haddaj (Objective:Virtual), this software is licensed under the MIT license.",
        font=("Calibri", 14),
        text_color="#A9B0B1"
    )
    copyright.pack(pady=10, side="bottom")
    root.mainloop()

    # Much better now !

# Define hosts file path for windows
windows_hostsfile = r"C:\Windows\System32\drivers\etc\hosts"

# Redirect IP for blocked websites
redirect_ip = "0.0.0.0"
original_hosts_content = None
running = True
stop_event = threading.Event()
blacklist_file = r"C:\Program Files\ObjectiveVirtual\ZBlock\blacklist.json" 
backup_hosts_file = "hosts.bak"

def update_info():
    messagebox.showinfo("Version 2.0 - Beta", "Massive UI redesign, new updater system inside the about ZBlock pop-up, better error handling, improved stability, numerous bug fixes... Read the full changelog on the github releases page for more info.")

def about():
    about = ctk.CTk()
    about.title("About - ZBlock")
    about.geometry("500x215")
    about.resizable(False, False)
    #about.iconbitmap(r"C:\Program Files\ObjectiveVirtual\ZBlock\icons\Zblock-icon.ico")
    title = ctk.CTkLabel(master=about, text="About ZBlock", font=("Calibri", 24, "bold"))
    title.pack(side="top")
    title2 = ctk.CTkLabel(master=about, text="Software version: v.2.0 Beta", font=("Calibri", 18, "bold"))
    title2.pack(side="top")
    title3 = ctk.CTkLabel(master=about, text="Designed & developed by: Anir El Haddaj", font=("Calibri", 14, "bold"))
    title3.pack(side="top")
    title4 = ctk.CTkLabel(master=about, text="License: MIT License", font=("Calibri", 14, "bold"))
    title4.pack(side="top")
    title5 = ctk.CTkLabel(master=about, text="This software is provided as it is, it doesn't include any warranty.", font=("Calibri", 13))
    title5.pack(side="top")
    title6 = ctk.CTkLabel(master=about, text="ZBlock modifies your hosts file located under: C:\Windows\System32\drivers\etc\hosts.", font=("Calibri", 13))
    title6.pack(side="top")
    updateme = ctk.CTkButton(master=about, text="Check for updates", command=update_software, fg_color="#294F91", hover_color="#26779C", corner_radius=50)
    updateme.pack(pady=10)
    about.mainloop()

def update_software():
    update_url = "https://api.github.com/repos/ObjectiveVirtual/ZBlock/releases/latest"
    try:
        with urllib.request.urlopen(update_url, timeout=10) as resp:
            if resp.status != 200:
                messagebox.showerror("Update", f"Could not check updates (HTTP {resp.status}).")
                return
            data = json.load(resp)
    except Exception as e:
        messagebox.showerror("Update", f"Failed to check for updates:\n{e}")
        return

    latest_tag = data.get("tag_name") or data.get("name") or ""
    latest_version_nums = re.findall(r'\d+', latest_tag)
    current_version_nums = re.findall(r'\d+', CURRENT_VERSION)

    def cmp_ver(a_list, b_list):
        a = [int(x) for x in a_list]
        b = [int(x) for x in b_list]
        # compare lexicographically, pad with zeros
        L = max(len(a), len(b))
        a += [0] * (L - len(a))
        b += [0] * (L - len(b))
        if a == b:
            return 0
        return 1 if a > b else -1

    if not latest_version_nums:
        # cannot parse latest version -> open release page to be safe
        if messagebox.askyesno("Update", "Could not parse latest release version. Open releases page?"):
            webbrowser.open(data.get("html_url", "https://github.com/ObjectiveVirtual/ZBlock/releases"))
        return

    compare = cmp_ver(latest_version_nums, current_version_nums)
    if compare <= 0:
        messagebox.showinfo("Update", "ZBlock is up-to-date.")
        return

    # newer release found
    release_name = data.get("name") or latest_tag
    if not messagebox.askyesno("Update available", f"New version available: {release_name}\nDownload and install now?"):
        return

    # try to find downloadable asset
    assets = data.get("assets", []) or []
    download_url = None
    filename = None
    if assets:
        # pick first asset with a browser_download_url
        for a in assets:
            url = a.get("browser_download_url")
            name = a.get("name")
            if url:
                download_url = url
                filename = name or os.path.basename(url)
                break

    if not download_url:
        # no asset: open release page
        webbrowser.open(data.get("html_url", "https://github.com/ObjectiveVirtual/ZBlock/releases"))
        messagebox.showinfo("Update", "No downloadable asset found. The release page was opened in your browser.")
        return

    # download asset to temp file with progress dialog (simple)
    try:
        tmp_dir = tempfile.gettempdir()
        tmp_path = os.path.join(tmp_dir, filename or "ZBlock_update.bin")
        # stream download
        with urllib.request.urlopen(download_url, timeout=30) as dl:
            total = dl.getheader('Content-Length')
            total = int(total) if total and total.isdigit() else None
            with open(tmp_path, "wb") as out:
                chunk_size = 8192
                downloaded = 0
                while True:
                    chunk = dl.read(chunk_size)
                    if not chunk:
                        break
                    out.write(chunk)
                    downloaded += len(chunk)
        # try to launch the downloaded file (Windows)
        try:
            if os.name == "nt":
                os.startfile(tmp_path)
            else:
                subprocess.Popen(["xdg-open", tmp_path])
            messagebox.showinfo("Update", f"Downloaded to:\n{tmp_path}\nThe installer was launched.")
        except Exception:
            # fallback: open containing folder
            try:
                webbrowser.open(f"file:///{os.path.dirname(tmp_path)}")
            except Exception:
                pass
            messagebox.showinfo("Update", f"Downloaded to:\n{tmp_path}\nPlease run it manually to install.")
    except Exception as e:
        messagebox.showerror("Update", f"Failed to download update:\n{e}")
        return

def load_blacklist():
    # Loads the blacklist.json file. And configures the hosts file too!
    try:
        with open(blacklist_file, "r") as f:
            return json.load(f), None
    except FileNotFoundError:
        messagebox.showerror("ZBlock - Load Blacklist", f"Oh no! {blacklist_file} can't be found. ADs won't be blocked.")
        return None, "Blacklist file not found."
    except json.JSONDecodeError as e:
        messagebox.showerror("ZBlock - Load Blacklist", f"Oh no! {blacklist_file} is corrupted, this error code can help you troubleshoot that: {e}")
        return None, f"JSON decode error: {e}"

def backup_hosts():
    #Backs up the original hosts file.
    try:
        shutil.copy2(windows_hostsfile, backup_hosts_file)
        messagebox.showinfo("ZBlock - Backup", "Hosts file backed up successfully.")
    except Exception as e:
        messagebox.showerror("ZBlock - Backup", f"OH NO... Something didn't go as expected and we couldn't back up your hosts file. This error code can help to find more about the issue: {e}")

def restore_hosts():
    #Restores the original hosts file and stops the adblocker.
    global original_hosts_content, running, stop_event
    try:
        shutil.copy2(backup_hosts_file, windows_hostsfile)
        running = False
        stop_event.set()
        messagebox.showinfo("ZBlock - Restore Hosts", "Original hosts file restored. Quitting ZBlock")
    except FileNotFoundError:
        running = False
        stop_event.set()
        messagebox.showerror("ZBlock - Restore Hosts", "Impossible to restore hosts file. Make sure you have backed them up first !")
    except Exception as e:
        running = False
        stop_event.set()
        messagebox.showerror("ZBlock - Restore Hosts", f"Umm... Looks like we can't restore your hosts file. This error code can help to find more about the issue: {e}")

def block_ads():
    # Blocks websites in the blacklist.
    global original_hosts_content
    blacklist_data, error_message = load_blacklist()

    if error_message or not blacklist_data:
        messagebox.showerror("ZBlock - Block ADs", error_message)
        return
    blacklist = blacklist_data

    try:
        with open(windows_hostsfile, "r+") as hostfile:
            if original_hosts_content is None:
                original_hosts_content = hostfile.readlines()
                hostfile.seek(0)
            hostfile.seek(0)
            lines = hostfile.readlines()
            hostfile.seek(0)
            cleaned_hosts = [host for host in lines if not any(site in host for site in blacklist)]
            hostfile.writelines(cleaned_hosts)
            for site in blacklist:
                hostfile.write(f"{redirect_ip} {site}\n")
            hostfile.truncate()
        messagebox.showinfo("ZBlock - Block ADs", "Hosts file configured successfully! ADs will be blocked soon :)")
    except PermissionError:
        messagebox.showwarning("ZBlock - Block ADs", "To proceed, you will need to run this program as an administrator.")
    except FileNotFoundError:
        messagebox.showerror("ZBlock - Block ADs", f"Hosts file not found at {windows_hostsfile}. ADs can't be blocked then. :(")

def run_ad_blocker():
    block_ads()
    while running:
        if stop_event.wait(60 * 60 * 24):
            break
        if running:
            block_ads()

if __name__ == "__main__":
    user_interface()