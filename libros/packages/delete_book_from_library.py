#! /usr/bin/env python3

import pymongo
import readchar

""" Removes a single book from the database

Usage:

    python3 delete_book_from_library.py
"""
def delete_book():
    try:
        client = pymongo.MongoClient('10.56.1.30', 27017)
        libaro_db = client["libaro"]
        books = libaro_db['books']

        barcode = input("Scan book barcode: ")
        doomed_book = books.find_one({'isbn': barcode})
        print()
        print(doomed_book['title'])
        print()
        print('Confirm delete book')
        print('Press 1 to confirm or any other key to cancel\n')
        confirm = readchar.readkey()
        if (confirm == '1'):
            try:
                books.remove({'isbn': barcode})
                print(f"{doomed_book['title']} has been deleted")
            except:
                print('Deletion failed')
        else:
            print('Deletion cancelled')
    except:
        print(f'Cannot find a book with isbn: "{barcode}"')

if __name__ == '__main__':
    delete_book()
