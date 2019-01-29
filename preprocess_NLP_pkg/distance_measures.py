"""This file contains functions for calculating similarity or distance measures
"""

from math import sqrt
from decimal import Decimal


def euclidean_distance(x, y):
    """ Calculates the euclidean distance between the vectors x and y
        x,y -- the vectors between which the distance is to be calculated
    """
    return sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))


def inverse_euclidean_similarity(x, y):
    """ Calculates the inverse euclidean similarity between the vectors x and y
        x,y -- the vectors between which the similarity is to be calculated
    """
    return float(1/(1+ euclidean_distance(x,y)))


def manhattan_distance(x, y):
    """ Calculates the manhattan distance between the vectors x and y
        x,y -- the vectors between which the distance is to be calculated
    """
    return sum(abs(a - b) for a, b in zip(x, y))

def inverse_manhattan_similarity(x, y):
    """ Calculates the inverse euclidean similarity between the vectors x and y
        x,y -- the vectors between which the similarity is to be calculated
    """
    return float(1/(1+ manhattan_distance(x,y)))

def nth_root(value, n_root):
    """ Calculates the nth root of a value
        value -- value for which the nth root is to be calculated
    """
    root_value = 1 / float(n_root)
    return round(Decimal(value) ** Decimal(root_value), 3)


def minkowski_distance(x, y, p_value):
    """ Calculates the minskowski's distance between the vectors x and y
        x,y -- the vectors between which the distance is to be calculated
    """
    return nth_root(sum(pow(abs(a - b), p_value) for a, b in zip(x, y)), p_value)


def square_root_sum(x):
    """ Calculates the square root of the squared sum of a vector
            x -- input vector
    """
    return sqrt(sum([a * a for a in x]))


def cosine_similarity(x, y):
    """ Calculates the minskowski's distance between the vectors x and y
            x,y -- the vectors between which the distance is to be calculated
        """
    numerator = sum(a * b for a, b in zip(x, y))
    denominator = square_root_sum(x) * square_root_sum(y)
    if denominator == 0:
        print("Error! Division by zero attempted")
        return
    return numerator / float(denominator)


def jaccard_similarity(x, y):
    """ Calculates the minskowski's distance between the vectors x and y
            x,y -- the vectors between which the distance is to be calculated
        """
    intersection = len(set.intersection(*[set(x), set(y)]))
    union = len(set.union(*[set(x), set(y)]))
    return intersection / float(union)
