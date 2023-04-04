#!/usr/bin/python3
"""

A module containing a function that prints a 2 new lines after each of these characters '.', '?' and ':'

"""


def text_indentation(text):
    """ The function takes only one arguements and prints two 2 new lines whenever it encounters '.', '?' and ':'
    
    Parameters:
        text: (string to be printed after '.', '?' and ':' is encountered)
        
    Raises:
        TypeError: If text is not a string
         
"""     
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    count = 0
    while count < len(text) and text[count] == " ":
        count = count + 1

    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count = count + 1
            while count < len(text) and text[count] == " ":
                count = count + 1
            continue
        count = count + 1
