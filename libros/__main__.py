#! /usr/bin/env python3

import readchar

from packages.print_welcome_message import welcome_message
from packages.print_options_list import provide_options
from packages.add_book_to_library import add_book
from packages.delete_book_from_library import delete_book
from packages.find_a_book import find_book
from packages.loan_book_from_library import loan_book
from packages.return_book_to_library import return_book
from packages.scan_book_barcode import scan_barcode
from packages.clear_console import clear_console

def main():
    clear_console()
    welcome_message()
    provide_options()
    option = readchar.readkey()

    if (option == '1'):
        print('Find a book:\n')
        find_book()
        main()
    elif (option == '2'):
        print('Loaning a book:\n')
        loan_book(scan_barcode())
        main()
    elif (option == '3'):
        print('Returning a book:\n')
        return_book(scan_barcode())
        main()
    elif (option == '4'):
        print('Adding a new book:\n')
        add_book(scan_barcode())
        main()
    elif (option == '5'):
        print('Deleting a book:\n')
        delete_book(scan_barcode())
        main()
    elif (option == '@'):
        return
    else:
        print("That key does nothing.")
        main()

main()