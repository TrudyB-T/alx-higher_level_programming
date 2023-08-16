#!/usr/bin/python3
"""Insert a line of text into file"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each
    line containing a specific string
    Arguments:
        filename (str): File name
        search_string (str): String to search for within the file.
        new_string (str): String to insert.
    """

    insert = []
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            insert += [line]
            if line.find(search_string) != -1:
                insert += [new_string]

    with open(filename, 'w', encoding="utf-8") as file:
        file.write("".join(insert))
