"""
AUTHOR  :   github/dfoyle
UPDATED :   2014-10-28

funcs.py
A collection of functions that interact with the classes inside classes.py
"""

# == IMPORTS --------------------------------------------------------------
import classes as cs

# == SETTINGS -------------------------------------------------------------
filename = "temp.org"

# == FUNCTIONS -----------------------------------------------------------


def parse_file(filename):
    """
    Parses an org file and reads headlines into the appropriate classes.
    """

    # Creating the document class.
    doc = cs.DocNode()

    lines = text_to_lines(filename)
    kids = []
    # Am I right?
    # kids is needed for some juggling to find the last read headline etc.

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
            doc.header.append(line)

    # We're done here.
    return doc


def text_to_lines(filename):
    """
    Reads a text file into lines.
    """

    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    return lines


def star_count(line):
    """
    Returns the star_count of a headline. Basic org headline has a structure
    like this:
    * Title
    """

    sc = 0
    if is_headline(line):
        sc = line.find(" ")
    return sc


def is_headline(line):
    """
    Checks a line to see if it's headline element.
    """

    result = True

    # If it doesn't start with *, then it's not a headline.
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
    """
    Checks a line to see if it's a comment, and not a setting.
    """

    result = False
    if is_setting(line) is False and line[0] == "#":
        result = True

    return result


def is_setting(line):
    """
    Checks a line to see if it's a org-mode setting.
    """

    result = False
    """
    #+SETTING: This is a setting.
    #+BEGIN_SRC python, this is an insert.
    """
    if line[:2] == "#+" and line.find(":") > 0:
        result = True

    return result


def read_settings(line):
    """
    Reads a line containing setting and returns a list.

    TODO: Make this happen.
    """


def list_items(element):
    """
    A temporary function used to print the items in
    a node.
    """

    for child in element.children:
        print "*"*child.stars, " ", child.title
        if len(child.children) > 0:
            list_items(child)


def return_children(element, initial=[]):
    """
    Returns a list of element's children recursively.
    """

    result = initial

    for child in element.children:
        result.append(child)
        print "Appending: ", child.title
        if len(child.children) > 0:
            temp = child
            return_children(temp, result)

    return result


def add_headline(parent, title):
    """
    Adds a headline to a parent node.
    """

    item = cs.ElementNode(parent)
    item.set_title(title)

