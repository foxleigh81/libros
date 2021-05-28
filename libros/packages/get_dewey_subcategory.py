#! /usr/bin/env python3

import sys
import pymongo

""" Gets the subcategory from the dewey decimal system.
This list is long so we will retrieve it from the database.

Usage:

    python3 get_subcategory.py category_number
"""

client = pymongo.MongoClient('10.56.1.30', 27017)
libaro_db = client["libaro"]
ddc = libaro_db['ddc']

def get_subcategory(dewey):
    ddc_first_two_digits = dewey[:2]
    subcategory = ddc.find_one({
        'code': {'$regex': f'^{ddc_first_two_digits}' }
    })
    return subcategory['name']

if __name__ == '__main__':
    get_subcategory(dewey=sys.argv[1])
1