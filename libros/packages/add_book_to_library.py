#! /usr/bin/env python3


import requests
import pymongo
import xml.etree.cElementTree as ET
from pprint import pprint as pp


""" Adds a single book to the database

Usage:

    python3 add_book_to_library.py
"""

oclc_endpoint = 'http://classify.oclc.org/classify2/Classify?summary=true'

client = pymongo.MongoClient('10.56.1.30', 27017)
libaro = client["libaro"]
books = libaro['books']

barcode = input("Scan barcode: ")

complete_endpoint = f'{oclc_endpoint}&isbn={barcode}'

prime_categories = {
    ('000', 'Computer Science, Information, and General Works', 'blue'),
    ('100', 'Philosophy and Psychology', 'red'),
    ('200', 'Religion', 'black'),
    ('300', 'Social Sciences', 'purple'),
    ('400', 'Language', 'green'),
    ('500', 'Science', 'orange'),
    ('600', 'Technology', 'pink'),
    ('700', 'Arts and Recreation', 'yellow'),
    ('800', 'Literature', 'brown'),
    ('900', 'History and Geography', 'white'),
}

# TODO: Regex barcode
req = requests.get(complete_endpoint)
root = ET.fromstring(req.content)

# Get book data from API
# TODO: add try/catch block
book = root[1].attrib

# Get dewey number
dewey = root[5][0][1].attrib['sfa']

# TODO: Get dewey subcategory from db


def get_category(dewey):
    for pc in prime_categories:
        if (pc[0][0] == dewey[0]):
            return pc


data = {
    'title': book['title'],
    'author': book['author'],
    'dewey': dewey,
    'category': get_category(dewey),
}

# TODO: Post into db
print(pp(data))
