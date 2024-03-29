#! /usr/bin/env python3

import sys
import requests
import xml.etree.cElementTree as ET

from packages.validate_isbn import validate_isbn

""" Gets the book data from the OCLC database

Usage:

    python3 get_book_from_oclc.py barcode
"""

oclc_endpoint = 'http://classify.oclc.org/classify2/Classify?summary=true'


def get_book(barcode):
    isbn = validate_isbn(barcode)
    complete_endpoint = f'{oclc_endpoint}&isbn={isbn}'
    try:
        request = requests.get(complete_endpoint)
        root = ET.fromstring(request.content)
        if not 'code' in root[1].attrib:
            return root
        else:
            raise Exception('No book found with that barcode')
    except:
        print('Book lookup failed')


if __name__ == '__main__':
    get_book(barcode=sys.argv[1])
