import threading
import json
import tkinter as tk
from tkinter import messagebox
import shutil

messagebox.showwarning("DISCLAIMER", "Using this software without any knowledge about how it works can make your computer unable to access the internet or may slow down your browser. We recommend you to read our wiki on GitHub for more information or consult the manual provided with the software if you have it. Remember that I AM NOT RESPONSIBLE FOR DAMAGE CAUSED TO YOUR COMPUTER.")

# Define hosts file paths for different operating systems
windows_hostsfile = r"C:\Windows\System32\drivers\etc\hosts"
default_hostsfile = windows_hostsfile

# Redirect IP for blocked websites
redirect_ip = "0.0.0.0"
original_hosts_content = None
running = True
stop_event = threading.Event()
blacklist_file = r"C:\Program Files\ObjectiveVirtual\Zblock\blacklist.json"
backup_hosts_file = "hosts.bak"

def update_info():
    messagebox.showinfo("Version 1.1 - Alpha (STABLE)", "Optimized protection against ADs and especially against trackers. Stabilized the version to prevent breaking internet access feature.")

def about():
    messagebox.showwarning("About ZBlock", "ZBlock is a program that runs and blocks every AD on your whole Windows OS. DISCLAIMER: This is program is still in Alpha state which means it may not operate perfectly and can also block legitimate websites that diesn't have the purpose of showing any AD. I AM NOT RESPONSIBLE OF ANY DAMAGE CAUSED BY THE SOFTWARE TO YOUR COMPUTER!")

def load_blacklist():
    #Loads the blacklist from the JSON file.
    try:
        with open(blacklist_file, "r") as f:
            return json.load(f), None
    except FileNotFoundError:
        return [], f"Oh no! {blacklist_file} can't be found. ADs won't be blocked."
    except json.JSONDecodeError as e:
        return [], f"Oh no! {blacklist_file} is corrupted, this code can help you troubleshoot that: {e}"

def backup_hosts():
    #Backs up the original hosts file.
    try:
        shutil.copy2(default_hostsfile, backup_hosts_file)
        return "Hosts file backed up successfully."
    except Exception as e:
        return f"Uh... Something didn't go as expected and we couldn't back up your hosts file. This error code can help to find more about the issue: {e}"

def restore_hosts():
    #Restores the original hosts file and stops the adblocker.
    global original_hosts_content, running, stop_event
    try:
        shutil.copy2(backup_hosts_file, default_hostsfile)
        running = False
        stop_event.set()
        return "Original hosts file restored. Quitting ZBlock"
    except FileNotFoundError:
        running = False
        stop_event.set()
        return "Oh no! Something went wrong, and we couldn't restore your hosts file. Make you have backed them up first !"
    except Exception as e:
        running = False
        stop_event.set()
        return f"Umm... Looks like we can't restore your hosts file. This error code can help: {e}"

def block_ads():
    #Blocks websites in the blacklist.
    global original_hosts_content
    blacklist_data, error_message = load_blacklist()

    if error_message:
        return error_message

    blacklist = blacklist_data

    try:
        with open(default_hostsfile, "r+") as hostfile:
            if original_hosts_content is None:
                original_hosts_content = hostfile.readlines()
            hostfile.seek(0)
            cleaned_hosts = [host for host in hostfile.readlines() if not any(site in host for site in blacklist)]
            hostfile.writelines(cleaned_hosts)
            for site in blacklist:
                hostfile.write(f"{redirect_ip} {site}\n")
            hostfile.truncate()
        return "Hosts file configured successfully! ADs will be blocked soon :)"
    except PermissionError:
        return "Permission Denied. Make sure to run this program as an administrator."
    except FileNotFoundError:
        return f"Error: Hosts file not found at {default_hostsfile}. ADs won't be blocked then. :("

def backup_hosts_gui():
    result = backup_hosts()
    messagebox.showinfo("Zblock - Backup", result)

def restore_hosts_gui():
    result = restore_hosts()
    messagebox.showinfo("ZBlock - Restore Hosts file", result)
    root.destroy()

def block_ads_gui():
    result = block_ads()
    messagebox.showinfo("ZBlock - Block ADs", result)

def run_ad_blocker():
    block_ads()
    while running:
        if stop_event.wait(60 * 60 * 24):
            break
        if running:
            block_ads()

if __name__ == "__main__":
    #Window configuration
    root = tk.Tk()
    root.title("ZBlock V.1.1 - Alpha")
    root.geometry("470x165")
    root.configure(bg='#1B1C1D')
    root.resizable(False, False)
    root.iconbitmap(r"C:\Program Files\ObjectiveVirtual\ZBlock\icons\Zblock-icon.ico")
    
    frame2 = tk.Frame(root)
    frame2.pack(fill="x", side='top')
    frame2.configure(bg='white')

    frame = tk.Frame(root)
    frame.pack(pady=10, side='top')
    frame.configure(bg = '#1B1C1D')

    backup_button = tk.Button(frame, text="Backup Hosts", command=backup_hosts_gui, relief="flat", highlightthickness=0, borderwidth=0)
    backup_button.pack(pady=10, side='left')
    backup_button.configure(bg='Orange', fg='white')

    block_button = tk.Button(frame2, text="Block Ads", command=block_ads_gui, relief="flat", highlightthickness=0, borderwidth=0)
    block_button.pack(padx=10, pady=5, side='left')
    block_button.configure(bg='#A52A2A', fg='white')

    restore_button = tk.Button(frame, text="Restore Hosts and Stop", command=restore_hosts_gui, relief="flat", highlightthickness=0, borderwidth=0)
    restore_button.pack(pady=10, side='left', padx=10)
    restore_button.configure(bg='#418ABB', fg='white')

    update = tk.Button(root, text="What's new ?", command=update_info, relief="flat", highlightthickness=0, borderwidth=0)
    update.pack(pady=10, side='top')
    update.configure(bg="gray", fg='white')

    copyright = tk.Label(root, text="©2025 Anir El Haddaj (Objective:Virtual), this software is licensed under the MIT license.")
    copyright.configure(bg='#1B1C1D', fg="#A9B0B1")
    copyright.pack(pady=10, side="bottom")

    objectivevirtual = tk.Label(frame2, text="Objective:Virtual", bg='white', font=("Calibri", 14, "bold"))
    objectivevirtual.pack(side="right")

    ZBlock = tk.Button(frame2, text="About ZBlock", command=about, relief="flat", highlightthickness=0, borderwidth=0)
    ZBlock.pack(padx=10, pady=5, side='left')
    ZBlock.configure(bg="gray", fg='white')


    threading.Thread(target=run_ad_blocker, daemon=True).start()

    root.mainloop()
