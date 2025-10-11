# ZBlock - A simple adblocker for Windows that works by modifying the hosts file.
# This source code, according to the MIT License, is free to use, modify and distribute. 
# You must include the original copyright and license notice in any copy of the software/source code.
# Feel free to contribute to this project by adding features, improvements or fixing bugs.

# Some monkeys got access to this shit. 
# IDK How, just ignore those sussy comments.

# Imports
import threading
import json
import tkinter as tk
from tkinter import messagebox
import shutil
import customtkinter as ctk

# Is it better now ?
def user_interface():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # Disclaimer message.
    messagebox.showinfo(
        "Welcome to ZBlock",
        "We believe that you have read our Wiki and understood how this software works. If not, then please do so. Continuing means that you acknowledge the fact that I AM NOT RESPONSIBLE FOR DAMAGE CAUSED TO THIS COMPUTER."
    )

    root = ctk.CTk()
    root.title("ZBlock V.1.2 - Alpha")
    root.geometry("500x220")
    root.resizable(False, False)
    #root.iconbitmap(r"C:\Program Files\ObjectiveVirtual\ZBlock\icons\Zblock-icon.ico")
    # Don't forget to uncomment this line when building the exe.
    # You know what happened last time, so...

    # Top frame for title and about
    frame2 = ctk.CTkFrame(root, fg_color="#1B263B")
    frame2.pack(fill="x", side='top', padx=0, pady=(0, 5))

    objectivevirtual = ctk.CTkLabel(
        frame2, text="Objective:Virtual", font=("Calibri", 16, "bold"), text_color="#61A5C2"
    )
    objectivevirtual.pack(side="right", padx=10, pady=10)

    ZBlock = ctk.CTkButton(
        frame2, text="About ZBlock", command=about, fg_color="#415A77", hover_color="#1B263B"
    )
    ZBlock.pack(side="left", padx=10, pady=10)

    block_button = ctk.CTkButton(
        frame2, text="Block Ads", command=block_ads, fg_color="#1B6CA8", hover_color="#274472"
    )
    block_button.pack(side="left", padx=10, pady=10)

    # Main frame for backup/restore
    frame = ctk.CTkFrame(root, fg_color="#1B263B")
    frame.pack(pady=10, side='top', fill="x")

    backup_button = ctk.CTkButton(
        frame, text="Backup Hosts", command=backup_hosts, fg_color="#1B98E0", hover_color="#247BA0"
    )
    backup_button.pack(side='left', padx=20, pady=20)

    restore_button = ctk.CTkButton(
        frame, text="Restore Hosts and Stop", command=restore_hosts, fg_color="#415A77", hover_color="#1B263B"
    )
    restore_button.pack(side='left', padx=20, pady=20)

    update = ctk.CTkButton(
        root, text="What's new ?", command=update_info, fg_color="#274472", hover_color="#1B263B"
    )
    update.pack(pady=5)

    copyright = ctk.CTkLabel(
        root,
        text="©2025 Anir El Haddaj (Objective:Virtual), this software is licensed under the MIT license.",
        font=("Calibri", 10),
        text_color="#A9B0B1"
    )
    copyright.pack(pady=10, side="bottom")

    threading.Thread(target=run_ad_blocker, daemon=True).start()
    root.mainloop()

    # Bro this looks pixelated and uglier than tkinter

    # See why Windows is superior to fedora ?

    # Ugh..

# Define hosts file path for windows
windows_hostsfile = r"C:\Windows\System32\drivers\etc\hosts"

# Redirect IP for blocked websites
redirect_ip = "0.0.0.0"
original_hosts_content = None
running = True
stop_event = threading.Event()
blacklist_file = r"C:\Program Files\ObjectiveVirtual\Zblock\blacklist.json" # Quit the addiction bro 💀
backup_hosts_file = "hosts.bak" # Isn't that a batch file ?
                                # Are you blind ? This a .bak file not a .bat file !

def update_info():
    messagebox.showinfo("Version 1.3 - Alpha (Untested)", "We redesigned the UI and improved the source code")
    # You don't know how to do shit right ?

def about():
    messagebox.showwarning("About ZBlock", "ZBlock is a software to help you manage and block ADs/websites system wide.") # This is an about message, take notes my friend.
    # messagebox.showwarning("About ZBlock", "ZBlock is a program that runs and blocks every AD on your whole Windows OS. DISCLAIMER: This is program is still in Alpha state which means it may not operate perfectly and can also block legitimate websites that diesn't have the purpose of showing any AD. I AM NOT RESPONSIBLE OF ANY DAMAGE CAUSED BY THE SOFTWARE TO YOUR COMPUTER!") PUBLIC SHAME >:D
    # Are you serious ?
    # Give better info bruh.

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
    # Core of the software, I spent months figuring it out.
    # BREAK IT AND I'LL FUCK YOUR ASS !

    # "Core of the software, I spent months figuring it out." 
    #                                       - A certified idiot
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