#!/usr/bin/python3
"""

function that prints 2 new lines after ".?:" characters

"""


def text_indentation(text):
    """prints 2 new lines after ".?:" characters

    Arguments:
             text: input string


    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

    for c in ".?:":
        list_text = s.split(c)
        s = ""
        for j in list_text:
            j = j.strip(" ")
            s = j + c if s is "" else s + "\n\n" + j + c

    print(s[:-3], end="")
