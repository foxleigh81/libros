#! /usr/bin/env python3

import readchar

from packages.print_welcome_message import welcome_message
from packages.print_options_list import provide_options
from packages.add_book_to_library import add_book_to_library
from packages.delete_book_from_library import delete_book
from packages.find_a_book import find_book
from packages.clear_console import clear_console

def main():
    clear_console()
    welcome_message()
    provide_options()
    option = readchar.readkey()

    if (option == '1'):
        find_book()
        main()
    elif (option == '2'):
        print("You're loaning out a book")
        main()
    elif (option == '3'):
        print("You're returning a book")
        main()
    elif (option == '4'):
        add_book_to_library()
        main()
    elif (option == '5'):
        delete_book()
        main()
    elif (option == '@'):
        return
    else:
        print("That key does nothing.")
        main()

main()