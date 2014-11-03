# -*- coding: utf-8 -*-
"""
    funcs
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Contains functions that work with classes in :module:'classes'.

    Main sections:
    Parsing, Listing, Writing, Helper.

    :author: dfoyle @ github.com
    :updated: 2014-11-03
"""

#: IMPORTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import classes as cs

#: SETTINGS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
filename = "temp.org"

#: FUNCTIONS-PARSING ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def parse_file(filename):
    """Parse an 'org' file into :class:DocNode.

    Reads through lines and parses them according to the 'org-mode' file
    structure. Currently supporting: title, star count, org-mode settings,
    lines that comes before the first headline, headline content.
    """

    # TODO: Directly accesses class attributes. Make it use getters etc.

    # The document to hold the headlines other stuff.
    doc = cs.DocNode()

    lines = text_to_lines(filename)
    kids = []
    # Am I right?
    # Kids is needed for some juggling to find the last read headline etc.

    for line in lines:
        if is_headline(line):
            title = line[star_count(line)+1:]
            if len(kids) == 0:
            # Case 1: It's the first headline of the document.
                new = cs.ElementNode(doc)
                new.set_title(title)
                kids.append(new)
            else:
            # Case 2: It's not the first headline of the document.
            # Compare the star counts to see if line is a child.
                if star_count(line) > kids[-1].stars:
                # Case 2.1: It's a children of the last entry.
                    parent = kids[-1]
                    new = cs.ElementNode(parent)
                    new.set_title(title)
                    kids.append(new)
                elif star_count(line) == kids[-1].stars:
                # Case 2.2: It's a sibling of the last entry.
                    parent = kids[-1].parent
                    new = cs.ElementNode(parent)
                    new.set_title(title)
                    kids.append(new)
                else:
                # Case 2.3: star_count(line) < kids[-1].stars()
                # This part is tricky. Need to find the sibling.
                # We reverse the list and traverse back to find the
                # sibling added last.
                    r_list = kids[:]
                    r_list.reverse()
                    x = star_count(line)

                    i = -1
                    while kids[i].stars != x:
                        i -= 1
                    sibling = kids[i]
                    parent = sibling.parent
                    new = cs.ElementNode(parent)
                    new.title = title
                    kids.append(new)

        elif is_setting(line):
            # Appending setting lines into the doc node.
            doc.settings.append(line)

        elif not is_setting(line) and not is_headline(line) and len(kids) == 0:
        # The line is a header. (Comes before the first headline
        # of the document.
            doc.header.append(line)

        else:
            # It's content.
            target = kids[-1]
            target.add_to_content(line)

    # We're done here.
    return doc


#: FUNCTIONS-LISTING ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def list_items(element):
    """A temporary function used to print the items in
    a node.
    """

    # TODO: Should eventually get rid of this function.

    for child in element.children:
        print "*"*child.stars, " ", child.title
        for line in child.content:
            print line
        if len(child.children) > 0:
            list_items(child)


def return_children(element, initial=[]):
    """Return the list of element's children recursively.
    """

    result = initial

    for child in element.children:
        result.append(child)
        print "Appending: ", child.title
        if len(child.children) > 0:
            temp = child
            return_children(temp, result)

    return result


#: FUNCTIONS-WRITING ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#: FUNCTIONS-HELPER ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def text_to_lines(filename):
    """Read a text file into lines and return list :var:'lines'.
    """

    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    return lines


def star_count(line):
    """Return the number of stars in a headline line.

    Basic 'org-mode' headline has a structure like this:
        * Title  :tag1:tag2:
        :PROPERTIES:
        :property-1: value
        :END:

        Content.
    """

    sc = 0
    if is_headline(line):
        sc = line.find(" ")
    return sc


def is_headline(line):
    """Check a line to see if it's a headline."""

    result = True

    # If it doesn't start with *, then it's not a headline.
    # Likely to cause some bugs in the future.
    # TODO: Create a function to remove spaces before '*' in headlines.
    # to prevent bugs resulting from user input.
    if line[0] != "*":
        result = False
    else:
    # In org-mode bold objects are written between *'s. So a line
    # can start with something like "*Important*"
        space = line.find(" ")
        for char in line[:space]:
            if char != "*":
                result = False

    return result


def is_comment(line):
    """Check a line to see if it's a comment, and NOT a setting."""

    result = False
    if is_setting(line) is False and line[0] == "#":
        result = True

    return result


def is_setting(line):
    """Checks a line to see if it's a org-mode setting."""

    result = False

    """'org-mode' uses '#+' to include settings in the file. But '#+' is also
    used to include source code or other blocks.

        #+TITLE:                  this is a setting.
        #+BEGIN_SRC python        this is the start of a block.
    """

    if line[:2] == "#+" and line.find(":") > 0:
        result = True

    return result


#: FUNCTIONS-TEMPORARY ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def read_settings(line):
    """Read a line containing a setting and return its values
    in a dictionary.

    Examples:
        #+TITLE: Document Title
        {'TITLE' : ["Document Title"]

        #+OPTIONS: H:3 num:1 toc:1
        {'OPTIONS' : [("h", "3"), ("num", "1"), ("toc", "1")]
    """


def add_headline(parent, title):
    """Add a headline to a parent node."""

    # TODO: Flesh this one out.
    item = cs.ElementNode(parent)
    item.set_title(title)
