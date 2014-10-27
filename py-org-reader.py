
"""
org-reader
version : 0.010
author : github/dfoyle
last updated : 2014-10-24

reads a simple org file and collects the headings as Heading objects.
"""

# imports
from heading import Heading
from functions import *

# location of the org file to be used.
filename = "temp.org"
f = open(filename, "r")


def main():
    """
    the main function. Nothing fancy so far.
    """

    global f
    lines = f.readlines()
    populate_heading(lines)


def zort():
    """
    just a silly temporary function used when debugging.
    """

    for x in Heading.headlines:
        print x

main()
