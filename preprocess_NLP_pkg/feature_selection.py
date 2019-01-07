"""This file contains functions for selecting features
"""

import nltk
from nltk.probability import FreqDist
import numpy as np
import collections
# from nltk.book import *

def convert_dict_to_numpy_array(dictionary):
    """Converts a dict into a numpy array.
        dictionary - the dict to be converted
    """
    if type(dictionary) == dict:
        return np.array(list(dictionary.items()))
    else:
        print("Error!! Wrong input. Input should be a dictionary!")

def word_freq_count(text, number_of_terms = 0):
    """Returns a dictionary of word frequency given a text
        text -- the text from which the word frequencies are to be extracted
        number_of_terms -- number of terms to extract
    """
    word_freq = FreqDist(nltk.tokenize.word_tokenize(text))
    if number_of_terms <= 0:
        return  dict(word_freq)
    else:
        return dict(word_freq.most_common(number_of_terms))


def select_word_vector(word_freq_dict, text, selected_words):
    """Given a list of selected most common keywords, Returns a dictionary of frequent words. Note that if a selected keyword is not present, 0 is returened as the key value.
        word_freq_dict -- a dictionary of word frequency
        selected_words -- a list of words to check against
    """
    word_freq_dict_selected = {}
    for key in selected_words:
        value = 0
        if word_freq_dict.get(key) is not None:
            value = word_freq_dict.get(key)
        word_freq_dict_selected[key] = value
    return word_freq_dict_selected


def word_freq_count_normalised(text, number_of_terms = 0):
    """Returns a list of word frequencies given a text
        text -- the text from which the word frequencies are to be extracted
        nunumber_of_terms -- number of terms to extract
    """
    tokens = nltk.tokenize.word_tokenize(text)
    word_freq = FreqDist(tokens)
    for key in word_freq.keys():
        value = word_freq[key]
        word_freq[key] = value/tokens.__len__()
    if number_of_terms <= 0:
        return  dict(word_freq)
    else:
        return dict(word_freq.most_common(number_of_terms))

## need to test the functions
def char_ngram_freq(text, n):
    #word_grams = nltk.ngrams(text.split(), n)
    char_ngrams = [text[i:i + n] for i in range(len(text) - n + 1)]
    char_ngrams_freq = collections.Counter(char_ngrams)
    return char_ngrams_freq

def select_features(feature_list, candidate_dict):
    #extract_features = [key for key, value in candidate_dict.items() if key in feature_list]
    feature_dict = {key: candidate_dict.get(key) for key in feature_list}
    for key in feature_dict.keys():
        if feature_dict.get(key) is None:
            feature_dict.get(key) == 0
    return feature_dict