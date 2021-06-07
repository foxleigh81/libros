#! /usr/bin/env python3

import os

def clear_console():
    """ clears the users console """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

if __name__ == '__main__':
    clear_console()