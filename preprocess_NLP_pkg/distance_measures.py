"""This file contains functions for calculating similarity or distance measures
"""

from math import sqrt, log
from decimal import Decimal
import logging


def euclidean_distance(x, y):
    """Calculates the euclidean distance between the vectors x and y
        Keyword arguments:
            x,y -- the vectors between which the distance is to be calculated
    """
    try:
        iter(x)
    except TypeError:
        logging.warning( 'Argument x is not iterable. None is returned')
        return None
    try:
        iter(y)
    except TypeError:
        logging.warning( 'Argument y is not iterable. None is returned')
        return None
    return sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))


def inverse_euclidean_similarity(x, y):
    """Calculates the inverse euclidean similarity between the vectors x and y
        Keyword arguments:
            x,y -- the vectors between which the similarity is to be calculated
    """
    return float(1/(1+ euclidean_distance(x,y)))


def manhattan_distance(x, y):
    """Calculates the manhattan distance between the vectors x and y
        Keyword arguments:
            x,y -- the vectors between which the distance is to be calculated
    """
    try:
        iter(x)
    except TypeError:
        logging.warning( 'Argument x is not iterable. None is returned')
        return None
    try:
        iter(y)
    except TypeError:
        logging.warning( 'Argument y is not iterable. None is returned')
        return None
    return sum(abs(a - b) for a, b in zip(x, y))


def inverse_manhattan_similarity(x, y):
    """Calculates the inverse euclidean similarity between the vectors x and y
        Keyword arguments:
            x,y -- the vectors between which the similarity is to be calculated
    """
    return float(1/(1+ manhattan_distance(x,y)))


def nth_root(value, n_root):
    """Calculates the nth root of a value
        Keyword arguments:
            value -- value for which the nth root is to be calculated
            n_root -- the nth root to be calculated, n > 0
    """
    try:
        root_value = 1 / float(n_root)
        return round(Decimal(value) ** Decimal(root_value), 3)
    except ZeroDivisionError:
        logging.error("Error! n_root should be greater than 0")
        return None


def minkowski_distance(x, y, p_value):
    """Calculates the minskowski's distance between the vectors x and y
        Keyword arguments:
            x,y -- the vectors between which the distance is to be calculated
    """
    return nth_root(sum(pow(abs(a - b), p_value) for a, b in zip(x, y)), p_value)


def square_root_sum(x):
    """Calculates the square root of the squared sum of a vector
        Keyword arguments:
            x -- input vector
    """
    return sqrt(sum([a * a for a in x]))


def cosine_similarity(x, y):
    """Calculates the minskowski's distance between the vectors x and y
        Keyword arguments:
            x,y -- the vectors between which the distance is to be calculated
    """
    numerator = sum(a * b for a, b in zip(x, y))
    denominator = square_root_sum(x) * square_root_sum(y)
    if denominator == 0:
        print("Error! Division by zero attempted")
        return
    return numerator / float(denominator)


def jaccard_similarity(x, y):
    """Calculates the minskowski's distance between the vectors x and y
        Keyword arguments:
            x,y -- the vectors between which the distance is to be calculated
    """
    intersection = len(set.intersection(*[set(x), set(y)]))
    union = len(set.union(*[set(x), set(y)]))
    return intersection / float(union)


def tanimoto_distance(x,y):
    """Calculates the tanimoto (normalised manhattan) distance between the vectors x and y
            Keyword arguments:
                x,y -- the vectors between which the distance is to be calculated
    """
    try:
        iter(x)
    except TypeError:
        logging.warning( 'Argument x is not iterable. None is returned')
        return None
    try:
        iter(y)
    except TypeError:
        logging.warning( 'Argument y is not iterable. None is returned')
        return None
    numerator = sum(abs(a - b) for a, b in zip(x, y))
    denominator = sum(max(a, b) for a,b in zip(x,y))
    return numerator/denominator


def matusita_distance(x,y):
    """Calculates the matusita distance (euclidean distance variant) between the vectors x and y
            Keyword arguments:
                x,y -- the vectors between which the distance is to be calculated
    """
    try:
        iter(x)
    except TypeError:
        logging.warning( 'Argument x is not iterable. None is returned')
        return None
    try:
        iter(y)
    except TypeError:
        logging.warning( 'Argument y is not iterable. None is returned')
        return None
    return sqrt(sum(pow(sqrt(a) - sqrt(b), 2) for a, b in zip(x, y)))


def clark_distance(x,y):
    """Calculates the clark distance (euclidean distance variant) between the vectors x and y
            Keyword arguments:
                x,y -- the vectors between which the distance is to be calculated
    """
    try:
        iter(x)
    except TypeError:
        logging.warning( 'Argument x is not iterable. None is returned')
        return None
    try:
        iter(y)
    except TypeError:
        logging.warning( 'Argument y is not iterable. None is returned')
        return None
    return sqrt(sum(pow(abs(a - b)/(a + b), 2) for a, b in zip(x, y)))


def jeffrey_divergence(x,y):
    """Calculates the jeffrey divergence between the vectors x and y
            Keyword arguments:
                x,y -- the vectors between which the distance is to be calculated
    """
    try:
        iter(x)
    except TypeError:
        logging.warning('Argument x is not iterable. None is returned')
        return None
    try:
        iter(y)
    except TypeError:
        logging.warning('Argument y is not iterable. None is returned')
        return None
    return sum((a - b)*log(a/b) for a, b in zip(x, y))


def kullback_leibler_divergence(x,y, delta = 0.001):
    """Calculates the jeffrey divergence between the vectors x and y
            Keyword arguments:
                x,y -- the vectors between which the distance is to be calculated
                delta -- a very small value meant to replace 0, to prevent log(0). Actually, better called lambda but that is a keyword
    """
    try:
        iter(x)
    except TypeError:
        logging.warning('Argument x is not iterable. None is returned')
        return None
    try:
        iter(y)
    except TypeError:
        logging.warning('Argument y is not iterable. None is returned')
        return None
    y_modified = [delta if val == 0 else val for val in y] # modified to replace zero with a small value delta
    x_modified = [delta if val == 0 else val for val in x]
    return sum(a * log(a / b) for a, b in zip(x_modified, y_modified))


def symmetric_kullback_leibler_divergence(x,y, delta = 0.001):
    """Calculates the jeffrey divergence between the vectors x and y
            Keyword arguments:
                x,y -- the vectors between which the distance is to be calculated
                delta -- a very small value meant to replace 0, to prevent log(0). Actually, better called lambda but that is a keyword
    """
    kld_x_y = kullback_leibler_divergence(x,y, delta = 0.001)
    kld_y_x = kullback_leibler_divergence(y,x, delta = 0.001)
    return (kld_x_y + kld_y_x)/2
