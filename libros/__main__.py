#! /usr/bin/env python3

import os
from packages.print_welcome_message import welcome_message
from packages.print_options_list import provide_options


def clearConsole():
    """ clears the users console """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


clearConsole()
welcome_message()
provide_options()

option = input('Select option:  ')

if (option == '1'):
    print("You're checking out a book")
elif (option == '2'):
    print("You're returning a book")
elif (option == '3'):
    print("you're adding a new book")
elif (option == '4'):
    print("You're deleting a book")
else:
    print("You cancelled the operation")
