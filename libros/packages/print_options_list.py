#! /usr/bin/env python3

import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

""" Display a list of options to the user

Usage:

    python3 print_options_list.py
"""

options = [
    (1, 'Find a book'),
    (2, 'Loan out a book'),
    (3, 'Return a book'),
    (4, 'Add a new book to the library'),
    (5, 'Delete a book from the library'),
]


def provide_options():
    print('Select an option below to continue\n')
    for option in options:
        number, name = option
        print(f'{Fore.GREEN + str(number) + Style.RESET_ALL}: {name}')
    print('\nAny other key will reset this menu\n')
    return


if __name__ == '__main__':
    provide_options()
