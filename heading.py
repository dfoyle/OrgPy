# module for Heading class and its methods.


class Heading(object):
    """
    class object for headlines contained in an *.org file.
    """

    # because slicing lists starts at 0
    # and this makes it easier to assign id's.
    headlines = [None]
    last_id = 0

    def __init__(self, id=0, stars=0, parent_id=0, title="", content="", option="init"):
        """
        class init.
        """

        self.id = Heading.last_id + 1
        # TODO Heading.headlines[-1].id + 1 ???

        self.stars = stars

        # for creating new heading after the initial read through the file.
        if option == "new":
            self.parent_id = parent_id

        # this option will be used when the scripts reads through a file.
        if option == "init":
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
