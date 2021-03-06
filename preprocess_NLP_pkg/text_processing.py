"""This file contains functions for tokenizing, normalising, removing special characters etc.
"""

import re, unicodedata
import inflect
from nltk.stem import LancasterStemmer, WordNetLemmatizer


def tokenize(character_seq, delimiter, remove_chars = None):
    """Removes given characters from a character sequence and splits according to the given delimiter
        Keyword arguments:
            character_seq -- character sequence to be split
            delimiter -- to split the character sequence
            remove_chars = the characters to remove
    """
    if remove_chars.len is not None:
        for i in remove_chars:
            re.sub(i, "", character_seq)
    tokens = character_seq.split(delimiter)
    return tokens


def paragraph_tokenizer(text, delimiter = '\n\n'):
    """Given a text, break it down into paragraphs
        Keyword arguments:
            text -- given text
            delimiter - type of delimiter to be used, default value is '\n\n'
    """
    paragraphs = text.split(delimiter)
    return paragraphs


def remove_non_ascii(word_list):
    """Remove non-ASCII characters from list of tokenized word_list
        Keyword arguments:
            word_list: list of words
    """
    new_word_list = []
    for word in word_list:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_word_list.append(new_word)
    return new_word_list


def to_lowercase(word_list):
    """Convert all characters to lowercase from list of tokenized word_list
        Keyword arguments:
            word_list: list of words
    """
    lowercase_word_list = [word.lower() for word in word_list]
    return lowercase_word_list


def remove_punctuation(word_list):
    """Remove punctuation from list of tokenized word_list
        Keyword arguments:
            word_list: list of words
    """
    new_word_list = []
    #[re.sub(r'[^\w\s]', '', word) for word in word_list if re.sub(r'[^\w\s]', '', word) != '']
    for word in word_list:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_word_list.append(new_word)
    return new_word_list


def replace_numbers(word_list):
    """Replace all interger occurrences in list of tokenized word_list with textual representation
        Keyword arguments:
            word_list: list of words
    """
    p = inflect.engine()
    new_word_list = []
    for word in word_list:
        if word.isdigit():
            new_word = p.number_to_word_list(word)
            new_word_list.append(new_word)
        else:
            new_word_list.append(word)
    return new_word_list


'''
def remove_stopword_list(word_list):
    """Remove stop word_list from list of tokenized word_list"""
    new_word_list = []
    for word in word_list:
        if word not in stopword_list.word_list('english'):
            new_word_list.append(word)
    return new_word_list

'''


def stem_word_list(word_list):
    """Stem word_list in list of tokenized word_list
        Keyword arguments:
            word_list: list of words
    """
    stemmer = LancasterStemmer()
    stems = []
    for word in word_list:
        stem = stemmer.stem(word)
        stems.append(stem)
    return stems


def lemmatize_verbs(word_list):
    """Lemmatize verbs in list of tokenized word_list
        Keyword arguments:
            word_list: list of words
    """
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word, pos='v') for word in word_list]


def process_word_list(word_list):
    """Process the word list with different techniques such as non ascii removal, conversion to lowercase, removing punctuation etc.
        Keyword arguments:
            word_list: list of words
    """
    word_list = remove_non_ascii(word_list)
    word_list = to_lowercase(word_list)
    word_list = remove_punctuation(word_list)
    word_list = replace_numbers(word_list)
    #word_list = remove_stopword_list(word_list)
    return word_list


def window_tokenizer(text, window_size = 5000, step_size = 100):
    """Given a text, break it down into windows of mentioned size, skipping characters mentioned in step size
        Keyword arguments:
            text -- given text
            window_size - number of characters in a window
            step_size - number of characters to skip before beginning next windows
    """
    windows = []
    i = 0
    while i < (len(text)-window_size + step_size):
        window = text[i:i + window_size]
        windows.append(window)
        i = i + step_size
    return windows

