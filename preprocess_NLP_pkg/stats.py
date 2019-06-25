"""
This file contains the statistical functions and tests that are normally not available in other standard packages
"""
import numpy as np
from math import ceil
import logging


def trunc_mean(arr, n = 0.1):
    """
    Calculates truncated mean for a given numpy array
    :param arr: A numpy array
    :param n: Fraction of values to truncate
    :return: a mean value
    """
    if type(arr) is not np.ndarray:
        logging.error('arr type must be numpy array')
        return 
    flat_arr = list((arr.flatten()))
    flat_arr.sort()
    trunc_indices = ceil(flat_arr.__len__() * n)
    if n<=0 or trunc_indices <1  or (2 * trunc_indices +1) >= len(flat_arr) :
        logging.warning('Could not truncate1. Either arr length is too small or n value is too large')
        return sum(list(flat_arr))/len(flat_arr)
    else:
        start_index = trunc_indices - 1
        end_index = flat_arr.__len__() - trunc_indices
        if len(flat_arr[start_index:end_index])>0:
            return sum(flat_arr[start_index:end_index])/len(flat_arr[start_index:end_index])
        else:
            logging.warning('Could not truncate. Either arr length is too small or n value is too large')
            return sum(list(flat_arr)) / len(flat_arr)
