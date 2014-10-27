# -*- encoding: utf-8 -*-
"""
AUTHOR  :   github/dfoyle
UPDATED :   2014-10-28

org.py
Main script.
"""

# == IMPORTS --------------------------------------------------------------
import classes as cs
import funcs as fn

# == SETTINGS -------------------------------------------------------------
filename = "temp.org"


def main():
    """
    Main function.
    """

    global filename

    doc = fn.parse_file(filename)
    fn.list_items(doc)


main()