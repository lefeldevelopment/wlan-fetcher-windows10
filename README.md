# Wlan Fetcher Windows10

## Description
A simple python-function, to gain all wlan passwords from stored wlan-profiles on a computer.

## Usage
This Script only works for __Windows 10__.
To get all wlan-profiles from your computer, simply run the file, or import it to your project.

_Make sure the file is stored locally to your project._
```python
from wlan_fetcher_windows10 import get_wlan_passwords

for profile in get_wlan_passwords():
    print(profile)
```

## Fixing errors
If your command line doesn't run in US, the script won't return values, because the output from the console is different. 
To fix this, manually run the commands and change the output to your language.
1. ``netsh wlan show profiles``
2. ``netsh wlan show profile NAME``
3. ``netsh wlan show profile NAME key=clear``

The strings that must be edited are marked with a comment.
