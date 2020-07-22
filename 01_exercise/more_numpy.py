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
    Write a function that takes a square matrix of integers and returns a
    set of all valid positions (i,j) of a value. Each position should be
    returned as a tuple of two integers.

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

    if not results:
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
    # helper function find_element_list moved to being outside of function

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
    # check if intlist is empty, note breaks with np.array
    if not intlist:
        return 0

    # make bool list of signs of the intlist
    intlist_positive = [a > 0 for a in intlist]

    # check if all positive
    if sum(intlist_positive) == len(intlist_positive):
        return sum(intlist)

    # check if all negative
    elif sum(intlist_positive) == 0:
        return max(intlist)

    # case where sublists need to be found
    simplified_list = simplify_list(intlist)

    sublists = []
    running_sum = 0

    for item in simplified_list:
        # check if new value added makes it less than zero
        if running_sum + item <= 0:
            sublists.append(running_sum)
            running_sum = 0
        else:
            running_sum = running_sum + item

    sublists.append(running_sum)

    return max(sublists)


def simplify_list(input_list):
    """
    Function that coaleses both positive and negative numbers together
    """
    # check if current sign is positive
    crrnt_sign_plus = (input_list[0] > 0)
    # make empty vars
    output_list = []
    temp_var = 0
    # loop through list
    for enumer_i in input_list:
        # check if sign change
        if (enumer_i > 0) ^ crrnt_sign_plus:
            output_list.append(temp_var)
            temp_var = enumer_i
            crrnt_sign_plus = (enumer_i > 0)
        else:
            temp_var += enumer_i
    output_list.append(temp_var)
    return output_list


def find_element_list(sq_mat, val):
    results = []
    for i in range(sq_mat.shape[0]):
        for j in range(sq_mat.shape[1]):
            if sq_mat[i, j] == val:
                results.append((i, j))

    return results
