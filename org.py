# -*- coding: utf-8 -*-
"""
    org
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    The main script for OrgPy. So far, it just calls :func:'parse_file()'
    from :file:'funcs.py'

    Eventually, it'll included some loop and functions for a command line
    commands to the features of OrgPy.

    :author: dfoyle @ github.com
    :updated: 2014-11-03
"""

#: IMPORTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import classes as cs
import funcs as fn

#: SETTINGS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
filename = "temp.org"


def main():
    """
    Main function.
    """

    global filename

    doc = fn.parse_file(filename)

    return doc

# Temporary...
x = main()
y = fn.flatten_org(x, sort=True)

for a in y:
    print "*" * a.stars, a.title
