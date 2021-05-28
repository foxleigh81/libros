#! /usr/bin/env python3

import pymongo
from packages.get_dewey_category import get_category
from packages.get_dewey_subcategory import get_subcategory
from packages.get_book_from_oclc import get_book

""" Adds a single book to the database

Usage:

    python3 add_book_to_library.py
"""
def add_book_to_library():
    client = pymongo.MongoClient('10.56.1.30', 27017)
    libaro_db = client["libaro"]
    books = libaro_db['books']

    barcode = input("Scan book barcode: ")

    book_data = get_book(barcode)

    try:
        # Get book
        book = book_data[1].attrib

        # Get dewey number
        dewey = book_data[5][0][1].attrib['sfa']
    except:
        print('Unable to parse book data')

    try:
        _, cat_name, cat_colour = get_category(dewey)
    except:
        print('Unable to retrieve category')
    try:
        subcat_name = get_subcategory(dewey)
    except:
        print('Unable to retreive subcategory')

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
        print(f'New book added to the library:\n {book["title"]}')
        print(f'Please give it a {cat_colour} sticker and the number: "{dewey}"')
        print(f'Once done, add the book to the "{cat_name}" section under "{subcat_name}"')
        

    except:
        print('Error posting to database')

if __name__ == '__main__':
    add_book_to_library()
