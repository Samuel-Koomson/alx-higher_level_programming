#!/usr/bin/python3
"""

A module containing a function that divides a matrix making use of the division function.

"""


def matrix_divided(matrix, div):
    """ The function takes a matrix and divides all the elements by a specified number or input:
    
    Parameters:
        matrix (a list within a list whose elements could be a floats or integers)
        div (specified number which is dividing the matrix elements)
        
    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero
    Return:
        New matrix resulting from the matrix division 
"""     
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if not all(len(element) > 0 for element in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if not all(len(element) == len(matrix[0]) for element in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    for element in matrix:
        if not isinstance(element, list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if not all(isinstance(x, (int, float)) for x in element):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")

    if div == 0:
        if isinstance(div, bool):
            raise TypeError("div must be a number")
        raise ZeroDivisionError("division by zero")
    if isinstance(div, bool):
        raise TypeError("div must be a number")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    new_matrix = []
    for element in matrix:
        new_matrix.append(list(map(lambda n: round(n / div, 2), element)))

    return new_matrix
