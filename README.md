# ZBlock

![Zblock Logo Idea](https://github.com/user-attachments/assets/3002e563-610b-4d40-8f5d-146eb8b7c080)
ZBlock is a simple desktop app for Windows that helps you block most annoying ADs you see on your whole Windows Machine, written in python.

# Introduction

ZBlock modifies your system hosts file by adding a lot of advertisement domains that the system must block by redirecting them to a computer that doesn't exist once you click on block ADs on the UI. Unfortunately, this will also block legitimate websites that don't have the purpose to show any AD.

# Disclaimer
>  I am not responsible of damage caused to your computer. If do you want a safe, efficace & reliable experience, pls do not choose versions flagged as unstable. They're too heavy, they contain large amount of informations that can break the internet access feature on your PC, yet unreliable. These kind of versions are meant for educationnal/experimental purposes, not for actual use. Use them at your own risk.

### Types of versions + comparaison
ZBlock comes with different types of versions, Stable & Unstable. Let's see what does each one of them offer and what are the trade offs !

| Version type | Benefits                         | Trade offs                                            |
|--------------|----------------------------------|-------------------------------------------------------|
| **Stable**   | - Performant                     | - Limited                                             |
|              | - Lightweight                    | - No early access to brand new features               |
|              | - Efficace                       | - Non-suitable for educationnal/experimental purposes |
|              | - Easy to manage / troubleshoot  |                                                       |
| **Unstable** | - Early access to new features   | - Heavier, bad for low end devices                    |
|              | - Early access to a new polished | - Likely to break device built-in features.           |
|              | UI.                              | - Can cause damage to the computer                    |
|              | - Comes with databases containing| - Quickly becomes unresponsive.                       |
|              | more domain names. Useful for ppl|                                                       |
|              | interested in this.              |                                                       |
|              | - For experimental/educationnal  |                                                       |
|              | purposes.                        |                                                       |

# Installation

1. Download the latest release from the [releases page](https://github.com/ObjectiveVirtual/ZBlock/releases).
2. Unzip the downloaded file and follow the instructions on the `NOTICE.txt` file to prove it's authenticity.
3. Run the `setup.exe` file and follow the installation instructions on your screen.

# Usage
Please visit our wiki for more information about how this software works. [See this](https://github.com/ObjectiveVirtual/ZBlock/wiki/)

# Troubleshooting

## Common Issues:

- **Issue:** ZBlock is not blocking ads.
  - **Solution:** Ensure ZBlock has the necessary permissions to modify the hosts file. Run ZBlock as an administrator.
- **Issue:** ZBlock is still blocking ads after shut down.
  - **Solution:** You will have to clear your hosts file from blocked advertising domains.
- **Issue:** I lost access to some legitimate websites, e.g : Samsung.com
  - **Solution:** Open your hosts file, find the legitimate website (Samsung.com in our case), remove the line with the domain on it, then save and exit the hosts file editor.
- **Issue:** I can't clear my hosts file.
  - **Solution:** Boot your PC into Safe Mode, then clear it, normally on Safe Mode you're alr in Admin mode so nothing will stop you.

# License

This project is licensed under the MIT Licesne
