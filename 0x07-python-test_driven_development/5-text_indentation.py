#!/usr/bin/python3
"""print text indentation"""


def text_indentation(text):
    """function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
    text: text to be printed
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')

    print("\n".join([line.strip() for line in text.split("\n")]), end="")
