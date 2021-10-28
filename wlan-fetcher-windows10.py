from typing import Any
# using subprocess to run command-line
import subprocess
# using re to analyse cmd-line output 
import re

def _run_process(cmd: "list[str]") -> Any:
    """A helper function to run the subprocess and return its output.

    Args:
        cmd (list[str]): The list of command-arguments, to run by subprecess

    Returns:
        Any: Output from subprocess
    """
    return subprocess.run(cmd, capture_output=True).stdout.decode("cp850")


def get_wlan_passwords() -> "list[dict]":
    """A function, that runs simple prompt commands, to gain all passwords from saved wlan-profiles.

    Returns:
        list[dict["ssid","password"]]: A list, containing a dictionary for each wlan profile, we were able to get the password from.
    """
    # create a list to store all dictionarys with its ssid and password
    wlan_list = []
    
    # looping through all wlan profiles
    for ssid in re.findall("All User Profile     : (.*)\r",
                           _run_process(["netsh", "wlan", "show", "profiles"])):
        # checking if profile contains a key
        if not re.search("Security key           : Absent",
                         _run_process(["netsh", "wlan", "show", "profile", ssid])):
            # making key visible with key=clear
            password = re.search("Key Content            : (.*)\r", _run_process(
                ["netsh", "wlan", "show", "profile", ssid, "key=clear"]))
            # adding profile to wlan_list if a password could be found
            if password:
                wlan_list.append({"ssid": ssid, "key": password[1]})
    # returning all profiles, after loop is done
    return wlan_list

if __name__ == "__main__":
    for profile in get_wlan_passwords():
        print(profile)