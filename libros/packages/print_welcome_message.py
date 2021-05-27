#! /usr/bin/env python3

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
    """ Prints out a predefined string to the console    
    """

    welcome_message = 'Welcome To Libros'

    character_count = len(welcome_message)
    border_string = add_border(character_count, '#')

    output = f'{border_string}\n{welcome_message}\n{border_string}\n\n'

    print(output)
    return


if __name__ == '__main__':
    welcome_message()
