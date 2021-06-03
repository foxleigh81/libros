#! /usr/bin/env python3

import pymongo
import readchar
from colorama import Fore, Style

""" Updates a book record to show that it has been lent to person x

Usage:

    python3 loan_book_from_library.py
"""
def loan_book(barcode):
    try:
        client = pymongo.MongoClient('10.56.1.30', 27017)
        libaro_db = client["libaro"]
        books = libaro_db['books']

        book_to_update = books.find_one({'isbn': barcode})
        print()
        print(Fore.GREEN + book_to_update['title'])
        print()
        print(Fore.CYAN + 'Confirm Loaning book')
        print('Press' + Fore.GREEN + ' 1 ' + Style.RESET_ALL + 'to confirm or any other key to cancel\n')
        confirm = readchar.readkey()
        if (confirm == '1'):
            try:
                person = input('Please type the name of the person you are loaning the book to and then press enter.\n')
                books.update_one({'isbn': barcode}, {"$set": { "held_by": person}})
                print(f"{book_to_update['title']} has been loaned to {person}")
                print('Press any key to return to the main menu')
                any_key = readchar.readkey()
                if (any_key):
                    pass
            except:
                print('Loaning failed')
        else:
            print('Loaning cancelled')
    except:
        print(f'Cannot find a book with isbn: "{barcode}"')

if __name__ == '__main__':
    loan_book()
