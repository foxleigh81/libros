#! /usr/bin/env python3

import os
import readchar

from packages.print_welcome_message import welcome_message
from packages.print_options_list import provide_options
from packages.add_book_to_library import add_book_to_library
from packages.delete_book_from_library import delete_book

def clearConsole():
    """ clears the users console """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


clearConsole()
welcome_message()
provide_options()

option = readchar.readkey()

if (option == '1'):
    print("You're checking out a book")
elif (option == '2'):
    print("You're returning a book")
elif (option == '3'):
    add_book_to_library()
elif (option == '4'):
    delete_book()
else:
    print("You cancelled the operation")
