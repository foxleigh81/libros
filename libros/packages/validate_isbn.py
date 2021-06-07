#! /usr/bin/env python3

import re

def validate_isbn(code):
    if (re.search("^(?=(?:\D*\d){10}(?:(?:\D*\d){3})?$)[\d-]+$", code)):
        return code
    else:
        raise Exception('Barcode is not a valid ISBN number')

if __name__ == '__main__':
    validate_isbn()
