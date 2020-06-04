#!/usr/bin/python3
###############################################################################
# Script      : edgeswitch.py
# Author      : David Velez
# Date        : 06/03/2020
# Description : Connected to my EdgeSwitch 8-150W via Netmiko, send a command
#               to the switch, and return results via TextFSM into a list
###############################################################################

# Imports
from netmiko import ConnectHandler
from getpass import getpass


def main():
    header()
    connect_to_switch()



def header():
    print("-" * 30)
    print("  Netmiko/TextFSM to ES8 App")
    print("-" * 30)
    print()


def connect_to_switch():

    # Variables needed to connect
    username = input("What is the username to your EdgeSwitch? ")
    password = getpass()
    ip_addr = input("What is the IP Address of your EdgeSwitch? ")
    device = 'ubiquiti_edgeswitch'

    # Connect to EdgeSwitch
    net_connect = ConnectHandler(device_type=device, 
            ip=ip_addr,
            username=username,
            password=password,
            secret=password)

    # Show Prompt
    print()
    print("-" * 25)
    print("         PROMPT")
    print("-" * 25)
    print(net_connect.find_prompt())
    print()

    # Show and Print VLANs
    vlans = net_connect.send_command("show vlan")
    print(vlans)

    # Use TextFSM to put words into a list
    print("-" * 25)
    print("    VLANs via TextFSM")
    print("-" * 25)
    vlans_tfsm = net_connect.send_command("show vlan", use_textfsm=True)
    print(vlans_tfsm)


# Invoke main
if __name__ == "__main__":
    main()
