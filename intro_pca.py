"""This file contains a set of functions to implement using PCA.

All of them take at least a dataframe df as argument. To test your functions
locally, we recommend using the wine dataset that you can load from sklearn by
importing sklearn.datasets.load_wine"""


def get_cumulated_variance(df, scale):
    """Apply PCA on a DataFrame and return a new DataFrame containing
    the cumulated explained variance from with only the first component,
    up to using all components together. Values should be expressed as
    a percentage of the total variance explained.

    The DataFrame will have one row and each column should correspond to a
    principal component.

    Example:
             PC1        PC2        PC3        PC4    PC5
    0  36.198848  55.406338  66.529969  73.598999  100.0

    If scale is True, you should standardise the data first
    Tip: use the StandardScaler from sklearn

    :param df: pandas DataFrame
    :param scale: boolean, whether to scale or not
    :return: a new DataFrame with cumulated variance in percent
    """
    import pandas as pd
    import numpy as np
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    
    # check if data needs scaling
    if scale:
        std_scale = StandardScaler()
        scaled_data = std_scale.fit_transform(df)
        df = pd.DataFrame(data = scaled_data, columns = df.columns)

    # fit pca 
    pca_obj = PCA()
    pca_obj.fit(df)
    
    # pull explained variance and scaled it, then get percentage and cumulative sum.
    variance_data = np.cumsum(pca_obj.explained_variance_ / sum(pca_obj.explained_variance_)) * 100

    # make columns for output
    columns = [ ("PC" + str(ind + 1)) for ind in range(len(df.columns))]

    # make output df and insert data 
    output = pd.DataFrame(columns = columns)
    output.loc[0] = variance_data

    return output


def get_coordinates_of_first_two(df, scale):
    """Apply PCA on a given DataFrame df and return a new DataFrame
    containing the coordinates of the first two principal components
    expressed in the original basis (with the original columns).

    Example:
    if the original DataFrame was:

          A    B
    0   1.3  1.2
    1  27.0  2.1
    2   3.3  6.8
    3   5.1  3.2

    we want the components PC1 and PC2 expressed as a linear combination
    of A and B, presented in a table as:

              A      B
    PC1    0.99  -0.06
    PC2    0.06   0.99

    If scale is True, you should standardise the data first
    Tip: use the StandardScaler from sklearn

    :param df: pandas DataFrame
    :param scale: boolean, whether to scale or not
    :return: a new DataFrame with coordinates of PC1 and PC2
    """

    import pandas as pd
    import numpy as np
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    
    # check if data needs scaling
    if scale:
        std_scale = StandardScaler()
        scaled_data = std_scale.fit_transform(df)
        df = pd.DataFrame(data = scaled_data, columns = df.columns)

    # fit pca 
    pca_obj = PCA()
    pca_obj.fit(df)

    # make names for rows (PC1, PC2, etc)
    rows = ['PC1', 'PC2']

    # output principle components of PCA as a df
    return pd.DataFrame(data = pca_obj.components_[0:2,:], columns = df.columns, index = rows)


def get_most_important_two(df, scale):
    """Apply PCA on a given DataFrame df and use it to determine the
    'most important' features in your dataset. To do so we will focus
    on the principal component that exhibits the highest explained
    variance (that's PC1).

    PC1 can be expressed as a vector with weight on each of the original
    columns. Here we want to return the names of the two features that
    have the highest weights in PC1 (in absolute value).

    Example:
        if the original DataFrame was:

          A    B     C
     0  1.3  1.2   0.1
     1  2.0  2.1   1.2
     2  3.3  6.8  23.4
     3  5.1  3.2   4.5

    and PC1 can be written as [0.05, 0.22, 0.97] in [A, B, C].

    Then you should return C, B as the two most important features.

    If scale is True, you should standardise the data first
    Tip: use the StandardScaler from sklearn

    :param df: pandas DataFrame
    :param scale: boolean, whether to scale or not
    :return: names of the two most important features as a tuple
    """

    raise NotImplementedError


def distance_in_n_dimensions(df, point_a, point_b, n, scale):
    """Write a function that applies PCA on a given DataFrame df in order to find
    a new subspace of dimension n.

    Transform the two points point_a and point_b to be represented into that 
    n dimensions space, compute the Euclidean distance between the points in 
    that space and return it.

    Example:
        if the original DataFrame was:

          A    B     C
     0  1.3  1.2   0.1
     1  2.0  2.1   1.2
     2  3.3  6.8  23.4
     3  5.1  3.2   4.5

    and n = 2, you can learn a new subspace with two columns [PC1, PC2].

    Then given two points:

    point_a = [1, 2, 3]
    point_b = [2, 3, 4]
    expressed in [A, B, C]

    Transform them to be expressed in [PC1, PC2], here we would have:
    point_a -> [-4.57, -1.74]
    point_b -> [-3.33, -0.65]

    and return the Euclidean distance between the points
    in that space.

    If scale is True, you should standardise the data first
    Tip: use the StandardScaler from sklearn

    :param df: pandas DataFrame
    :param point_a: a numpy vector expressed in the same basis as df
    :param point_b: a numpy vector expressed in the same basis as df
    :param n: number of dimensions of the new space
    :param scale: whether to scale data or not
    :return: distance between points in the subspace
    """

    raise NotImplementedError


def find_outliers_pca(df, n, scale):
    """Apply PCA on a given DataFrame df and transform all the data to be expressed
    on the first principal component (you can discard other components)

    With all those points in a one-dimension space, find outliers by looking for points
    that lie at more than n standard deviations from the mean.

    You should return a new dataframe containing all the rows of the original dataset
    that have been found to be outliers when projected.

    Example:
        if the original DataFrame was:

          A    B     C
     0  1.3  1.2   0.1
     1  2.0  2.1   1.2
     2  3.3  6.8  23.4
     3  5.1  3.2   4.5

    Once projected on PC1 it will be:
          PC1
    0   -7.56
    1   -6.26
    2   16.46
    3   -2.65

    Compute the mean of this one dimensional dataset and find all rows that lie at more
    than n standard deviations from it.

    Note that the formula for the standard deviation varies, depending on whether we
    want an unbiased estimator of the variance of the infinite population, or a maximum
    likelihood estimate of the variance for a normally distributed variable.
    Specifically, in the case of an unbiased estimator, the average squared deviation is
    calculated as x.sum() / N - 1. For a maximum likelihood estimate, the formula is
    x.sum() / N. While pandas uses the former, numpy uses the latter which can lead to
    unexpected differences. For this exercise, use the unbiased estimator.

    Here, if n==1, only the row 2 is an outlier.

    So you should return:
         A    B     C
    2  3.3  6.8  23.4


    If scale is True, you should standardise the data first
    Tip: use the StandardScaler from sklearn

    :param df: pandas DataFrame
    :param n: number of standard deviations from the mean to be considered outlier
    :param scale: whether to scale data or not
    :return: pandas DataFrame containing outliers only
    """

    raise NotImplementedError

