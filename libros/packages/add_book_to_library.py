#! /usr/bin/env python3

import pymongo
import readchar
from colorama import Fore, Style

from packages.get_dewey_category import get_category
from packages.get_dewey_subcategory import get_subcategory
from packages.get_book_from_oclc import get_book

""" Adds a single book to the database

Usage:

    python3 add_book_to_library.py
"""
def add_book(barcode):
    client = pymongo.MongoClient('10.56.1.30', 27017)
    libaro_db = client["libaro"]
    books = libaro_db['books']

    book_data = get_book(barcode)

    existing_copy = books.find_one({'isbn': barcode})

    add_book = True

    if (existing_copy):
        print(Fore.RED + 'This book already exists in the library.\n')
        print('Press' + Fore.GREEN + ' 1 ' + Style.RESET_ALL + 'to add another copy or any other key to return to the main menu\n')
    
        add_new_book = readchar.readkey()

        if not (add_new_book == '1'):
            add_book = False

    if add_book:
        try:
            # Get book
            book = book_data[1].attrib

            # Get dewey number
            dewey = book_data[5][0][1].attrib['sfa']
        except:
            print(Fore.RED + 'Unable to parse book data')

        try:
            _, cat_name, cat_colour = get_category(dewey)
        except:
            print(Fore.RED + 'Unable to retrieve category')
        try:
            subcat_name = get_subcategory(dewey)
        except:
            print(Fore.RED + 'Unable to retreive subcategory')

        data = {
            'isbn': barcode,
            'title': book['title'],
            'author': book['author'],
            'ddc': dewey,
            'category': cat_name,
            'subcategory': subcat_name,
            'colour': cat_colour,
            'held_by': 'Library' # A book will be held by the library by when added
        }

        try:
            books.insert_one(data)
            print(Fore.GREEN + f'New book added to the library:\n {Style.BRIGHT + book["title"]}\n')
            print(f'Please give it a {Style.BRIGHT + cat_colour + Style.RESET_ALL} sticker and the number: "{Style.BRIGHT + dewey + Style.RESET_ALL}"\n')
            print(f'Once done, add the book to the "{Style.BRIGHT + cat_name + Style.RESET_ALL}" section under "{Style.BRIGHT + subcat_name + Style.RESET_ALL}"\n')
            print('Press 1 to add another book or any other key to return to the menu:\n')
            confirm = readchar.readkey()
            if (confirm == '1'):
                add_book()
            else:
                pass
        except:
            print(Fore.RED +'Error posting to database')

if __name__ == '__main__':
    add_book()
