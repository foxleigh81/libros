#! /usr/bin/env python3

""" Display a list of options to the user

Usage:

    python3 print_options_list.py
"""

options = [
    (1, 'Check out a book'),
    (2, 'Return a book'),
    (3, 'Add a new book to the library'),
    (4, 'Delete a book from the library'),
]


def provide_options():
    print('Select an option below to continue\n')
    for option in options:
        number, name = option
        print(f'{number}: {name}')
    print('\nAny other key will reset this menu\n')
    return


if __name__ == '__main__':
    provide_options()
