#! /usr/bin/env python3

import sys

""" Gets the top level category from the dewey decimal system. 

Usage:

    python3 get_category.py category_number
"""

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


def get_category(dewey):
    for category in prime_categories:
        if (category[0][0] == dewey[0]):
            return category


if __name__ == '__main__':
    get_category(dewey=sys.argv[1])
