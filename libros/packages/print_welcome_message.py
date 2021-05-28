#! /usr/bin/env python3

import colorama
from colorama import Fore, Back, Style

colorama.init()

""" Display welcome message to the user

Usage:

    python3 print_welcome_message.py
"""


def add_border(count, string):
    output = ''
    i = 0
    while i < count:
        output += string
        i += 1
    return output


def welcome_message():
    print(Fore.MAGENTA + "   _      _ _                   ")
    print(Fore.MAGENTA + "  | |    (_) |                  ")
    print(Fore.MAGENTA + "  | |     _| |__  _ __ ___  ___ ")
    print(Fore.MAGENTA + "  | |    | | '_ \| '__/ _ \/ __|")
    print(Fore.MAGENTA + "  | |____| | |_) | | | (_) \__ \\")
    print(Fore.MAGENTA + "  |______|_|_.__/|_|  \___/|___/\n")
    print(Style.RESET_ALL + "The Foxy Foxleigh library manager")
    print(Fore.RED + "=================================\n" + Style.RESET_ALL)

    return


if __name__ == '__main__':
    welcome_message()
