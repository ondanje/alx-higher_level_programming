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
    words = ""
    for delimeter in ".?:":
        words = (delimeter + "\n\n").join(
                [index.strip(" ") for index in words.split(delimeter)])


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
