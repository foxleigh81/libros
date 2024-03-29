#! /usr/bin/env python3

import pymongo
import readchar
from colorama import Fore, Style

""" Removes a single book from the database

Usage:

    python3 delete_book_from_library.py
"""
def delete_book(barcode):
    try:
        client = pymongo.MongoClient('10.56.1.30', 27017)
        libaro_db = client["libaro"]
        books = libaro_db['books']

        book_to_delete = books.find_one({'isbn': barcode})
        print()
        print(Fore.GREEN + book_to_delete['title'])
        print()
        print(Fore.CYAN + 'Confirm Deleting book')
        print('Press' + Fore.GREEN + ' 1 ' + Style.RESET_ALL + 'to confirm or any other key to cancel\n')
        confirm = readchar.readkey()
        if (confirm == '1'):
            try:
                books.delete_one({'isbn': barcode})
                print(f"{book_to_delete['title']} has been deleted")
                print('Press any key to return to the main menu')
                any_key = readchar.readkey()
                if (any_key):
                    pass
            except:
                print('Deletion failed')
        else:
            print('Deletion cancelled')
    except:
        print(f'Cannot find a book with isbn: "{barcode}"')

if __name__ == '__main__':
    delete_book()
