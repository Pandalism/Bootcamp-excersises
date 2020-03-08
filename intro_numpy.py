"""A set of numpy exercises"""


def zero_insert(x):
    """
    Write a function that takes in a vector and returns a new vector where
    every element is separated by 4 consecutive zeros.

    Example:
    [4, 2, 1] --> [4, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1]

    :param x: input vector
    :type x: numpy.array
    :return: input vector with elements separated by 4 zeros
    :rtype: numpy.array
    """
    import numpy as np

    # constants
    insertlen = 4

    # create initial return array and inserted zeros
    tempoutput = x[0:1]
    insert = np.zeros(insertlen)

    # loop and build output
    if len(x) == 1:
        output = tempoutput
    else:
        for i in range(len(x)-1):
            tempoutput = np.concatenate((tempoutput, insert))
            tempoutput = np.concatenate((tempoutput, x[i+1:i+2]))
        output = tempoutput
    
    # output
    return output


def return_closest(x, val):
    """
    Write a function that takes in a vector and returns the value contained in
    the vector that is closest to a given value.
    If two values are equidistant from val, return the one that comes first in
    the vector.

    Example:
    ([3, 4, 5], 2) --> 3

    :param x: input vector
    :type x: numpy.array of int/float
    :param val: input value
    :type val: int | float
    :return: value from x closest to val
    :rtype: int | float
    :raise ValueError:
    """
    import numpy as np

    # subtract the desired number, find the absolute, then find the index of the min
    mask = np.argmin(abs(x - val))
    
    return x[mask]


def cauchy(x, y):
    """
    Write a function that takes in two vectors and returns the associated Cauchy
    matrix with entries a_ij = 1/(x_i-y_j).

    Example:
    ([1, 2], [3, 4]) --> [[-1/2, -1/3], [-1, -1/2]]

    Note: the function should raise an error of type ValueError if there is a
    pair (i,j) such that x_i=y_j

    :param x: input vector
    :type x: numpy.array of int/float
    :param y: input vector
    :type y: numpy.array of int/float
    :return: Cauchy matrix with entries 1/(x_i-y_j)
    :rtype: numpy.array of float
    :raise ValueError:
    """
    import numpy as np

    output = np.zeros((len(x),len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            if (x[i] - y[j] == 0):
                raise ValueError
            output[i, j] = 1 / (x[i] - y[j])

    return output


def most_similar(x, v_list):
    """
    Write a function that takes in a vector x and a list of vectors and finds,
    in the list, the index of the vector that is most similar to x using
    cosine similarity.

    Example:
    ([1, 1], [[1, 0.9], [-1, 1]]) --> 0 (corresponding to [1,0.9])

    :param x: input vector
    :type x: numpy.array of int/float
    :param v_list: list of vectors
    :type v_list: list of numpy.array
    :return: index of element in list that is closest to x in cosine-simv_
    :rtype: int
    """
    #imports 
    import numpy as np

    # set up cosine similarity lambda
    cossim = lambda a, b: np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    # set up similarity array
    cossim_results = np.zeros(len(v_list))

    # run through array building similarities
    for i in range(len(v_list)):
        cossim_results[i] = cossim(x, v_list[i])
    
    # return closest to 1
    return np.argmin(abs(cossim_results - 1))


def gradient_descent(x_0, learning_rate, tol):
    """
    Write a function that does gradient descent with a fixed learning_rate
    on function f with gradient g and stops when the update has magnitude
    under a given tolerance level (i.e. when |xk-x(k-1)| < tol).
    Return a tuple with the position, the value of f at that position and the
    magnitude of the last update.
    h(x) = (x-1)^2 + exp(-x^2/2)
    f(x) = log(h(x))
    g(x) = (2(x-1) - x exp(-x^2/2)) / h(x)

    Example:
    (1.0, 0.1, 1e-3) --> approximately (1.2807, -0.6555, 0.0008)

    :param x_0: initial point
    :type x_0: float
    :param learning_rate: fixed learning_rate
    :type learning_rate: float
    :param tol: tolerance for the magnitude of the update
    :type tol: float
    :return: the position, the value at that position and the latest update
    :rtype: tuple of three float
    """

    raise NotImplementedError
