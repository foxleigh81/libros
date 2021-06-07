#! /usr/bin/env python3

from packages.validate_isbn import validate_isbn

def scan_barcode():

    barcode = input('Scan book barcode: ')

    isbn = validate_isbn(barcode)

    return isbn

if __name__ == '__main__':
    scan_barcode()
