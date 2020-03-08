"""Some exercises that can be done with numpy (but you don't have to)"""
import numpy as np


def all_unique_chars(string):
    """
    Write a function to determine if a string is only made of unique
    characters and returns True if that's the case, False otherwise.
    Upper case and lower case should be considered as the same character.

    Example:
    "qwr#!" --> True, "q Qdf" --> False

    :param string: input string
    :type string:  string
    :return:      true or false if string is made of unique characters
    :rtype:        bool
    """

    # make string lower case so we will match lower and upper case characters
    lc_string = string.lower()

    # convert to a list of char
    full_string = list(lc_string)

    # make a list with only unique values
    uniq_string = np.unique(full_string)

    # return true if unique and full are the same length
    return len(uniq_string) == len(full_string)


def find_element(sq_mat, val):
    """
    Write a function that takes a square matrix of integers and returns a set of all valid
    positions (i,j) of a value. Each position should be returned as a tuple of two
    integers.

    The matrix is structured in the following way:
    - each row has strictly decreasing values with the column index increasing
    - each column has strictly decreasing values with the row index increasing
    The following matrix is an example:

    Example 1 :
    mat = [ [10, 7, 5],
            [ 9, 4, 2],
            [ 5, 2, 1] ]
    find_element(mat, 4) --> {(1, 1)}

    Example 2 :
    mat = [ [10, 7, 5],
            [ 9, 4, 2],
            [ 5, 2, 1] ]
    find_element(mat, 5) --> {(0, 2), (2, 0)}

    The function should raise an exception ValueError if the value isn't found.

    :param sq_mat: the square input matrix with decreasing rows and columns
    :type sq_mat:  numpy.array of int
    :param val:    the value to be found in the matrix
    :type val:     int
    :return:       all positions of the value in the matrix
    :rtype:        set of tuple of int
    :raise ValueError:
    """
    results = set()
    for i in range(sq_mat.shape[0]):
        for j in range(sq_mat.shape[1]):
            if sq_mat[i, j] == val:
                results.add((i, j))

    if len(results) == 0:
        raise ValueError

    return results


def filter_matrix(mat):
    """
    Write a function that takes an n x p matrix of integers and sets the rows
    and columns of every zero-entry to zero.

    Example:
    [ [1, 2, 3, 1],        [ [0, 2, 0, 1],
      [5, 2, 0, 2],   -->    [0, 0, 0, 0],
      [0, 1, 3, 3] ]         [0, 0, 0, 0] ]

    :param mat: input matrix
    :type mat:  numpy.array of int
    :return:   a matrix where rows and columns of zero entries in mat are zero
    :rtype:    numpy.array
    """
    # define helper function
    def find_element_list(sq_mat, val):
        results = []
        for i in range(sq_mat.shape[0]):
            for j in range(sq_mat.shape[1]):
                if sq_mat[i, j] == val:
                    results.append((i, j))

        return results

    # find position of zeros
    zeros = list(find_element_list(mat, 0))

    # find unique col and rows to convert to 0

    uniq_col = []
    uniq_row = []

    for tuples in zeros:
        if tuples[0] not in uniq_row:
            uniq_row.append(tuples[0])
        if tuples[1] not in uniq_col:
            uniq_col.append(tuples[1])

    for i in uniq_row:
        mat[i, :] = 0

    for j in uniq_col:
        mat[:, j] = 0

    return mat


def largest_sum(intlist):
    """
    Write a function that takes in a list of integers,
    finds the sublist of contiguous values with at least one
    element that has the largest sum and returns the sum.
    If the list is empty, 0 should be returned.

    Example:
    [-1, 2, 7, -3] --> the sublist with larger sum is [2, 7], the sum is 9.

    :param intlist: input list of integers
    :type intlist:  list of int
    :return:       the largest sum
    :rtype:         int
    """
    # numpy the list
    A = np.array(intlist)

    # make mask for positive numbers only
    x = [a > 0 for a in A]

    # case if intlist is empty
    if len(x) == 0:
        output = 0

    # case if all numbers are negative
    elif sum(x) == 0:
        output = max(A)

    # case if all numbers are positive
    elif sum(x) == len(x):
        output = sum(A)

    # case where sublists need to be found
    else:
        sum_list = []
        temp_sum_pos = 0
        temp_sum = 0
        for i, ai in enumerate(A):
            # add up numbers as marching down the lane
            temp_sum += ai
            # add only if positive
            if ai > 0:
                temp_sum_pos += ai
            if temp_sum <= 0:
                sum_list.append(temp_sum_pos)
                temp_sum = 0
                temp_sum_pos = 0

        output = max(sum_list)
    return output
