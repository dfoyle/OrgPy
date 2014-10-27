# -*- encoding: utf-8 -*-
"""
AUTHOR  :   github/dfoyle
UPDATED :   2014-10-28

classes.py
Contains the necessary classes and their methods.
"""


class DocNode(object):
    """
    The document.
    """

    def __init__(self):
        """
        Inits a new doc with following attributes.
        """

        """
        An org file might not always start with a headline.
        "settings"    : for org-mode settings. (#+SETTING: ...)
        "header"      : Comments or simple text elements before the headlines.
        """

        self.title = "Root"
        self.settings = []
        self.header = []
        self.children = []
        self.stars = 0

    # == GETTERS ----------------------------------------------------------

    def settings(self):
        """
        Return a list of settings.
        """

        return self.settings

    def header(self):
        """
        Return a list of elements before the first headline.
        """

        return self.header

    def children(self):
        """
        Return the list of elements.
        """

        return self.children

    def stars(self):
        """
        Return stars.
        """

        return self.stars

    # == SETTERS ---------------------------------------------------------

    # == METHODS ----------------------------------------------------------

    def append(self, child):
        """
        Append the Doc with an ElementNode child.
        """

        self.children.append(child)
        # update the element's parent. Just in case.
        child.set_parent(self)

    def append_settings(self, setting):
        """
        Append the setting attribute.
        """

        self.settings.append(setting)

    def append_header(self, head):
        """
        Append the header attribute.
        """

        self.header.append(head)

    def yield_stuff(self, attr):
        """
        Yielding through the members of list attributes.
        - yield_stuff(element_node.elements())
        """

        types = [list, tuple, dict, set]
        if type(attr) in types:
            for item in attr:
                yield item


class ElementNode(object):
    """
    generic elements.
    """

    def __init__(self, parent):
        """
        Basic init.
        """

        self.parent = parent
        parent.append(self)
        self.stars = parent.stars + 1
        self.children = []
        self.content = []
        self.title = ""

    # == GETTERS ---------------------------------------------------------

    def parent(self):
        """
        Return parent.
        """

        return self.parent

    def stars(self):
        """
        Return stars.
        """

        return self.stars

    def children(self):
        """
        Return a list of children.
        """

        return self.children

    def content(self):
        """
        Return a list of content.
        """

        return self.content

    def title(self):
        """
        Returns the title.
        """

        return self.title
        
    # == SETTERS ---------------------------------------------------------

    def set_parent(self, parent):
        """
        Set the parent.
        """

        self.parent = parent

    def set_title(self, title):
        """
        Set the title.
        """

        self.title = title

    # == METHODS ---------------------------------------------------------

    def append(self, child):
        """
        Append child into self.children.
        """

        self.children.append(child)
        child.set_parent(self)

    def yield_stuff(self, attr):
        """
        Yielding through the members of list attributes.
        - yield_stuff(element_node.elements())
        """

        types = [list, tuple, dict, set]
        if type(attr) in types:
            for item in attr:
                yield item

    def add_to_content(self, cont):
        """
        Append cont into the content list attribute.
        """

        self.content.append(cont)

# Following classes are for things related to the ElementNodes


class AttNode(object):
    """
    generic attribute nodes.
    """


class SettingNode(object):
    """
    org mode settings.
    """


class CommentNode(object):
    """
    comments.
    """


class TagNode(AttNode):
    """
    tags for elements.
    """


class PropertiesNode(AttNode):
    """
    properties.
    """


class DateNode(AttNode):
    """
    date elements.
    """