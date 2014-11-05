# -*- coding: utf-8 -*-
"""
    classes
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Contains the necessary classes and their methods for reading
    ´org´ files.

    :author: dfoyle @ github.com
    :updated: 2014-11-03
"""


class DocNode(object):
    """For the root of the document. Holds the top headlines in a
    list of :attr:'children'.
    """

    def __init__(self):
        """Inits a new doc with following attributes.

        An org file might not always start with a headline.

        :attr:'settings' for org-mode settings, usually on the top of
        the file and starting with '#+': '#+TITLE:' etc.

        :attr:'header' for comments or text that comes before the
        first top headline.
        """

        self.title = "Root"
        self.settings = []
        self.header = []
        self.children = []
        self.stars = 0

    #: GETTERS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # not really used at the moment. Most of the functions directly
    # access the attributes.

    # TODO: Write getters and revise code to use them.
    def settings(self):
        """Return a list of settings."""

        return self.settings

    def header(self):
        """Return a list of elements before the first headline.
        :attr:'header'
        """

        return self.header

    def children(self):
        """ Return the list :attr:'children'."""

        return self.children

    def stars(self):
        """Return :attr:'stars'."""

        return self.stars

    #: SETTERS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #: METHODS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def append(self, child):
        """Append the Doc with a :class:'ElementNode' child."""

        self.children.append(child)
        # Update the element's parent. Just in case.
        child.set_parent(self)

    def append_settings(self, setting):
        """Append :attr:'settings'"""

        self.settings.append(setting)

    def append_header(self, head):
        """Append the list :attr:'header'."""

        self.header.append(head)

    def yield_stuff(self, attr):
        """Yield the members of a list attribute.

        Usage:
        doc.yield_stuff(children)
        """

        types = [list, tuple, dict, set]

        if type(attr) in types:
            for item in attr:
                yield item


class ElementNode(object):
    """For headlines."""

    def __init__(self, parent):
        """Basic init."""

        self.parent = parent
        parent.append(self)
        self.stars = parent.stars + 1
        self.children = []
        self.content = []
        self.title = ""

    def __cmp__(self, other):
        """For sorting by title.
        """

        if self.title != "" and other.title != "":
            return cmp(self.title.lower(), other.title.lower())

    #: GETTERS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # TODO: Similarly to :class:'DocNode', fix attributes
    # and the functions call them.

    def parent(self):
        """Return :attr:'parent'."""

        return self.parent

    def stars(self):
        """Return :attr:'stars'."""

        return self.stars

    def children(self):
        """Return a list of :attr:'children'."""

        return self.children

    def content(self):
        """Return a list of :attr:'content'."""

        return self.content

    def title(self):
        """Returns the :attr:'title'."""

        return self.title

    #: SETTERS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def set_parent(self, parent):
        """Set the :attr:'parent'."""

        self.parent = parent

    def set_title(self, title):
        """Set the :attr:'title'."""

        self.title = title

    #: METHODS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def append(self, child):
        """Append child into :attr:'children'."""

        self.children.append(child)
        child.set_parent(self)

    def yield_stuff(self, attr):
        """Yielding through the members of list attributes.

        Usage:
        headline.yield_stuff(title)
        """

        types = [list, tuple, dict, set]

        if type(attr) in types:
            for item in attr:
                yield item

    def add_to_content(self, cont):
        """Append content into the list :attr:'content'."""

        self.content.append(cont)


# Following classes are not implemented yet. They are to be used
# with :class:'ElementNode'.


class Tags(object):
    """For headline tags.
    """


class Properties(object):
    """For headline properties.
    """


class Comments(object):
    """For headline comments.
    """
