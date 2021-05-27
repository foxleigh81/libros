#! /usr/bin/env python3


import requests
import pymongo
import xml.etree.cElementTree as ET


""" Adds a single book to the database

Usage:

    python3 add_book_to_library.py
"""

oclc_endpoint = 'http://classify.oclc.org/classify2/Classify?summary=true'

client = pymongo.MongoClient('10.56.1.30', 27017)
libaro = client["libaro"]
books = libaro['books']

barcode = input("Scan barcode now: ")

complete_endpoint = f'{oclc_endpoint}&isbn={barcode}'

# TODO: Regex barcode
req = requests.get(complete_endpoint)
root = ET.fromstring(req.content)

# Get book data from API
book = root[1].attrib

# Get dewey number
dewey = root[5][0][1].attrib['sfa']

data = {
    'title': book['title'],
    'author': book['author'],
    'dewey': dewey
}

print(data)
