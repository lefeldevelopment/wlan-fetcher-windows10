# -*- coding: utf-8 -*-
from __future__ import annotations
from subprocess import check_output, CalledProcessError
from re import findall, search

# EDITABLES
PROFILES_KEYWORD = "Profile"
KEY_CONTENT_KEYWORD = "Key Content"


def wifi_passwords(
        profiles_keyword: str = "Profile",
        key_content_keyword: str = "Key Content",
        return_errors: bool = False,
    ) -> dict | tuple[dict, list]:
    
    data = {}
    errors = []
    
    profiles_command = "netsh wlan show profiles"
    key_command = "netsh wlan show profiles name='{key}' key=clear"
    
    networks = check_output(
        profiles_command,
        shell=True
    ).decode("utf-8", "replace")

    for network in findall(f"(?:{profiles_keyword}\s*:\s)(.*)", networks):
        
        network = network.split('\r')[0]

        try:
            result = check_output(
                key_command.format(key=network),
                shell=True
            ).decode("utf-8", "ignore")
        except CalledProcessError:
            errors += [network]
            continue
        
        password = search(f"(?:{key_content_keyword}\s*:\s)(.*)", result)
        data[network] = password[1]
        
    if return_errors:
        return data, errors
    return data
  
if __name__ == "__main__":
  print(wifi_passwords(PROFILES_KEYWORD,KEY_CONTENT_KEYWORD,True))
