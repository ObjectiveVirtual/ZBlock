# ZBlock

ZBlock is a simple desktop app for Windows that helps you block most annoying ADs you see on your browser.

![Zblock Logo Idea](https://github.com/user-attachments/assets/3002e563-610b-4d40-8f5d-146eb8b7c080)

## Introduction

ZBlock modifies your system hosts file by adding a lot of advertisement domains that the system must block by redirecting them to a computer that doesn't exist once you click on block ADs on the UI. Unfortunately, this will also block legitimate websites that don't have the purpose to show any AD.

## Installation

1. Download the latest release from the [releases page](https://github.com/ObjectiveVirtual/ZBlock/releases).
2. Unzip the downloaded file and follow the instructions on the `NOTICE.txt` file to prove it's authenticity.
3. Run the `setup.exe` file and follow the installation instructions.

## Usage

### Blocking Ads

1. Open ZBlock.
2. Click on the "Block ADs" button.
3. ZBlock will modify your hosts file to block advertisement domains.

<img width="602" height="327" alt="Capture" src="https://github.com/user-attachments/assets/459dfb63-880a-4e9c-bc6d-4d31c0ef2042" />

### Backing Up Hosts File

1. Shut down ZBlock if it is running.
2. Open File Explorer and navigate to `C:\Windows\System32\drivers\etc`.
3. Copy the `hosts` file and paste it in a safe location.

   ![image](https://github.com/user-attachments/assets/443447b7-c2d0-42b7-a536-483e6634cf64)

## Troubleshooting

### Common Issue

- **Issue:** ZBlock is not blocking ads.
  - **Solution:** Ensure ZBlock has the necessary permissions to modify the hosts file. Run ZBlock as an administrator.
- **Issue:** ZBlock is still blocking ads after shut down.
  - **Solution:** You will have to clear your hosts file from blocked advertising domains.
- **Issue:** I lost access to some legitimate websites, e.g : Samsung.com
  - **Solution:** Open your hosts file, find the legitimate website (Samsung.com in our case), remove the line with the domain on it, then save and exit the hosts file editor.

# License

This project is licensed under the MIT Licesne
