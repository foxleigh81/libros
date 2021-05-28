#! /usr/bin/env python3

import pymongo
import readchar
import colorama
from packages.clear_console import clear_console
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

""" Finds book information in the library

Usage:

    python3 find_a_book.py
"""

def find_book():
    clear_console()
    try:
        client = pymongo.MongoClient('10.56.1.30', 27017)
        libaro_db = client["libaro"]
        books = libaro_db['books']

        print('What do you know about the book?')
        print()
        print(Fore.GREEN + '1:' + Style.RESET_ALL + ' I know the barcode/isbn')
        print(Fore.GREEN + '2:' + Style.RESET_ALL + ' I know the title')
        print(Fore.GREEN + '3:' + Style.RESET_ALL + ' I know the author')
        print(Fore.GREEN + '4:' + Style.RESET_ALL + ' Show me all the books')

        selection = readchar.readkey()
        book_array = []

        if (selection == '1'):
            barcode = input("Scan book barcode: ")
            book_array = books.find({'isbn': barcode})
        
        if (selection == '2'):
            print('\nType the title of the book and press enter\n')
            print(Style.DIM + '(You can enter part of a title but this may yield multiple results)\n')
            title = input('')
            book_array = books.find({'title' : {
                "$regex": f"{title}",
                "$options": "i"
                }
                })
        
        if (selection == '3'):
            print('\nType the name of the author and press enter\n')
            print(Style.DIM + '(You can enter part of a name but this may yield multiple results)\n')
            author = input('')
            book_array = books.find({'author' :  {
                "$regex": f"{author}",
                "$options": "i"
                }
                })
        
        if(selection == '4'):
            book_array = books.find()

        for book in book_array:
            print(Fore.BLUE +'==================================')
            print(Fore.CYAN + f"Title: {Style.RESET_ALL + book['title']}")
            print(Fore.CYAN + f"Author: {Style.RESET_ALL +book['author']}")
            print(Fore.CYAN + f"Category: {Style.RESET_ALL +book['category']}")
            print(Fore.CYAN + f"Colour: {Style.RESET_ALL +book['colour']}")
            print(Fore.CYAN + f"DDC: {Style.RESET_ALL +book['ddc']}")
            print(Fore.CYAN + f"ISBN: {Style.RESET_ALL +book['isbn']}")
            print(Fore.BLUE +'==================================')
        
        print('\nPress any key to return to the main menu...')

        return_to_menu = readchar.readkey()
        if (return_to_menu == '1'):
            pass

    except:
        print(f'There was an error retrieving data from the database')

if __name__ == '__main__':
    find_book()
