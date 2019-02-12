"""This file contains functions for selecting features
"""

import nltk
from nltk.probability import FreqDist
import numpy as np
import collections
import re
# from nltk.book import *


def convert_dict_to_numpy_array(dictionary):
    """Converts a dict into a numpy array.
        Keyword arguments:
            dictionary - the dict to be converted
    """
    if type(dictionary) == dict:
        return np.array(list(dictionary.items()))
    else:
        print("Error!! Wrong input. Input should be a dictionary!")


def select_features(feature_list, candidate_dict):
    """Returns a new dictionary created by selecting keys in a given candidate dictionary with respect to a given feature list
        Keyword arguments:
            feature_list -- list of desired features
            candidate_dict - base dictionary
    """
    feature_dict = {key: candidate_dict.get(key) for key in feature_list}
    for key in feature_dict.keys():
        if feature_dict.get(key) is None:
            feature_dict[key] = 0
    return feature_dict


""" Lexical features: Such features consider a text as a mere sequence of word-tokens
"""


def max_word_length(text):
    """Returns the length of the longest word in the text
        Keyword arguments:
            text: text
    """
    word_list = nltk.tokenize.word_tokenize(text)
    return len(max(word_list))


def average_word_length(text):
    """Returns the average length of all the words in the text
        Keyword arguments:
            text: text
    """
    word_list = nltk.tokenize.word_tokenize(text)
    return sum([len(word) for word in word_list]) / len(word_list)


def max_sentence_length(text):
    """Returns the length of the longest sentence in the text
        Keyword arguments:
            text: text
    """
    sentences = nltk.tokenize.sent_tokenize(text) # note that english is by default, for other languages set in the config
    return len(max(sentences))


def average_sentence_length(text):
    """Returns the average length of all the sentences in the text
        Keyword arguments:
            text: text
    """
    sentences = nltk.tokenize.sent_tokenize(text)
    return sum([len(sentence) for sentence in sentences]) / len(sentences)


def yules_k(text):
    """Returns the yules_k of the text
        Keyword arguments:
            text: text
    """
    word_list = nltk.tokenize.word_tokenize(text)
    s1 = len(word_list)
    word_freq_dist = FreqDist(nltk.tokenize.word_tokenize(text))
    s2 = sum([freq ** 2 for freq in word_freq_dist.values()])
    K = 10000 * (s2-s1)/(s1**2)
    return K


def ttr(text):
    """Returns the text to token ratio of the text
        Keyword arguments:
            text: text
    """
    word_list = nltk.tokenize.word_tokenize(text)
    word_freq_dist = FreqDist(nltk.tokenize.word_tokenize(text))
    tokens = word_freq_dist.keys()
    lexical_density = len(tokens)/len(word_list)*100
    return lexical_density


def word_freq_count(text, number_of_terms=0):
    """Returns a dictionary of word frequency given a text
        text -- the text from which the word frequencies are to be extracted
        number_of_terms -- number of terms to extract
    """
    word_freq = FreqDist(nltk.tokenize.word_tokenize(text))
    if number_of_terms <= 0:
        return  dict(word_freq)
    else:
        return dict(word_freq.most_common(number_of_terms))


def select_word_vector(word_freq_dict, selected_word_list):
    """Given a list of selected most common keyword_list, Returns a dictionary of frequent word_list. Note that if a selected keyword is not present, 0 is returened as the key value.
        word_freq_dict -- a dictionary of word frequency
        selected_word_list -- a list of word_list to check against
    """
    word_freq_dict_selected = {}
    for key in selected_word_list:
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


""" Character features: Such features consider a text as a mere sequence of characters
"""

#def select_ngram_vector(word_freq_dict, text, selected_word_list):
    ## implementation required.


## need to test the functions
def char_ngram_freq(text, n):
    #word_grams = nltk.ngrams(text.split(), n)
    char_ngrams = [text[i:i + n] for i in range(len(text) - n + 1)]
    char_ngrams_freq = collections.Counter(char_ngrams)
    return char_ngrams_freq


def most_common_ngrams(text, n, number_of_terms=0):
    """Returns the most common ngrams as a dictionary
        text -- the text from which the ngrams are to be extracted
        number_of_terms -- number of terms to extract
    """
    all_ngrams = char_ngram_freq(text, n)
    if number_of_terms == 0:
        return all_ngrams.most_common()
    elif number_of_terms >0 :
        return all_ngrams.most_common(number_of_terms)
    else:
        print("Error! Cannot have negative number of ngrams returned")


def alphabet_chars_count(text):
    """Returns the number of alphabetic characters in the text
        Keyword arguments:
            text: text
    """
    return re.findall("[a-z]", text.lower()).__len__()


def uppercase_chars_count(text):
    """Returns the number of the uppercase alphabetic characters in the text
        Keyword arguments:
            text: text
    """
    return re.findall("[A-Z]", text).__len__()


def lowercase_chars_count(text):
    """Returns the number of the lowercase alphabetic characters in the text
        Keyword arguments:
            text: text
    """
    return re.findall("[A-Z]", text).__len__()


def digits_count(text):
    """Returns the number of the numeric characters in the text
        Keyword arguments:
            text: text
    """
    return re.findall("[0-9]", text).__len__()

