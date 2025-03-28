# ZBlock

ZBlock is a simple desktop app for Windows that helps you block most annoying ADs you see on your browser.

![Zblock Logo Idea](https://github.com/user-attachments/assets/3002e563-610b-4d40-8f5d-146eb8b7c080)

## Introduction

ZBlock modifies your system hosts file by adding a lot of advertisement domains that the system must block once you click on block ADs. Unfortunately, this will also block legitimate websites that don't have the purpose to show any AD.

## Installation

1. Download the latest release from the [releases page](https://github.com/ObjectiveVirtual/ZBlock/releases).
2. Unzip the downloaded file.
3. Run the `setup.exe` file and follow the installation instructions.

## Usage

### Blocking Ads

1. Open ZBlock.
2. Click on the "Block ADs" button.
3. ZBlock will modify your hosts file to block advertisement domains.

   ![image](https://github.com/user-attachments/assets/608c2843-b9f5-4e4e-ba45-619b79e60fec)

### Backing Up Hosts File

1. Shut down ZBlock if it is running.
2. Open File Explorer and navigate to `C:\Windows\System32\drivers\etc`.
3. Copy the `hosts` file and paste it in a safe location.

   ![image](https://github.com/user-attachments/assets/443447b7-c2d0-42b7-a536-483e6634cf64)

## Troubleshooting

### Common Issue

- **Issue:** ZBlock is not blocking ads.
  - **Solution:** Ensure ZBlock has the necessary permissions to modify the hosts file. Run ZBlock as an administrator.
