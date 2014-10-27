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
# filename = "python.org"
# filename = "keybindings.org"
f = open(filename, "r")


def main():
    """
    the main function. Nothing fancy so far.
    """

    global f
    lines = f.readlines()

    # an org file might not start with a heading.
    # this parts appends stuff that comes before the first
    # heading into Heading.header
    ind = 0
    for line in lines:
        if stars(line) == 1:
            ind = lines.index(line)
            break

    stuff = lines[:ind]
    for element in stuff:
        Heading.header.append(element)

    populate_heading(lines)


def zort():
    """
    just a silly temporary function used when debugging.
    """

    for x in Heading.headlines:
        print x

main()
write_to_file("new.org")
