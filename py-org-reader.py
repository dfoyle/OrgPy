"""
org-reader
version : 0.010
author : github/dfoyle
last updated : 2014-10-24

reads a simple org file and collects the headings as Heading objects.
"""

# location of the org file to be used.
filename = "temp.org"
f = open(filename, "r")


# class and methods.
class Heading(object):
    """
    class object for headlines contained in an *.org file.
    """

    # because slicing lists starts at 0
    # and this makes it easier to assign id's.
    headlines = [None]
    last_id = 0

    def __init__(self, id=0, stars=0, parent_id=0, title="", content=""):
        """
        class init.
        """

        self.id = Heading.last_id + 1
        # TODO: Heading.headlines[-1].id + 1 ???

        self.stars = stars

        # parent_id needs some juggling.
        if self.stars == 1:
            # if it's a main heading.
            # >>> * Heading title.
            self.parent_id = 0
        else:
            # if it's a child.
            if self.stars > Heading.headlines[-1].stars:
                # self.parent_id = Heading.last_id
                # TODO: how about this?
                self.parent_id = Heading.headlines[-1].id
                # seems more fool-proof.
            # if it's a sibling.
            elif self.stars == Heading.headlines[-1].stars:
                self.parent_id = Heading.headlines[-1].parent_id
            else:
                # reverse the headlines list and traverse back
                # until you reach a Heading object with the same star attr
                # with self and assign its parent_id.
                # in short find its sibling.
                r_headlines = Heading.headlines[:]
                r_headlines.reverse()
                i = -1
                while Heading.headlines[i].stars != self.stars:
                    i -= 1
                self.parent_id = Heading.headlines[i].parent_id

        self.title = title

        self.content = content

        # since we're about to add to the headlines,
        # we need to increment the last_id as well.
        Heading.last_id += 1
        Heading.headlines.append(self)

    def __str__(self):
        """
        a string representation for a quick look.
        """

        return "id \t: %d \nparent \t: %d \nstars \t: %d \ntitle \t: %s \nContent:\n%s" % (
            self.id, self.parent_id, self.stars, self.title, self.content)

    def get_id(self):
        return self.id

    def get_stars(self):
        return self.stars

    def get_parent_id(self):
        return self.parent_id

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def add_to_content(self, line):
        """
        adds the line to self.content
        """

        self.content += line

# END OF: CLASS HEADING() =================================


# ==========================================================
# FUNCTIONS
# ==========================================================


def stars(line):
    """
    returns the number of stars a heading has.
    """

    if "*" in line:
        start = line.find("*")
        line = line[start:]
        end = line.find(" ")
        x = end
    else:
        x = 0

    return x


def populate_heading(lines):
    """
    reads through the org file and populates
    the Heading() accordingly.
    """

    for line in lines:
        line_stars = stars(line)
        if line_stars > 0:
            line_title = line[line_stars+1:]
            heading = Heading(stars=line_stars, title=line_title)

        if line_stars <= 0 and len(Heading.headlines) > 1:
        # in case the first line isn't a heading. Otherwise
        # headlines[-1] pulls a NoneType.
            last_heading = Heading.headlines[-1]
            last_heading.add_to_content(line)


def pick_heading(hid):
    """
    returns a heading by its id.
    """

    target = None
    for element in Heading.headlines[1:]:
        if element.get_id() == hid:
            target = element

    return target


def remove_heading(hid):
    """
    removes a heading and its children.
    """

    target = pick_heading(hid)

    print "Warning: This delete %s and all its children." % target.get_title()
    raw_input("Continue:")

    find_and_delete_children(hid)
    delete_heading(hid)


def find_and_delete_children(hid):
    """
    finds a headings children.
    """

    target = pick_heading(hid)
    found_children = False

    for element in Heading.headlines[1:]:
        if element.get_parent_id() == target.get_id():
            found_children = True
            found = element
            print "deleting...", found.get_title()
            find_and_delete_children(found.get_id())
            ind = Heading.headlines.index(found)
            del Heading.headlines[ind]

    if found_children is False:
        return "Done"


def delete_heading(hid):
    """
    deletes the heading itself.
    """

    target = pick_heading(hid)
    print "deleting...", target.get_title()
    ind = Heading.headlines.index(target)
    del Heading.headlines[ind]


def main():
    global f
    lines = f.readlines()
    populate_heading(lines)


def zort():
    for x in Heading.headlines:
        print x

# lines = f.readlines()

# populate_heading(lines)
main()
zort()

print Heading.headlines[1]
print Heading.headlines[2]
