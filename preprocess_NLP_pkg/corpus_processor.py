"""This file contains functions for creating dictionary of files for each respective author
To be used only for private processing
"""

import os
import re
from preprocess_NLP_pkg.load_data import read_file
from nltk.probability import FreqDist
from nltk import tokenize

def author_dictionary (corpus_token_path, correct_author_path):
    """Take a path to a folder of token files and a file of correct authors
        and for each author, create a dictionary of words for all respective tokens
        (works for french and english corpora)
        Keyword arguments:
        corpus_token_path -- folder path of tokens
        correct_author_path -- a file of correct authors
    """
    token_files = os.listdir(corpus_token_path)
    correct_author = read_file(correct_author_path).split("\n")
    author_name_token_dict = {}
    for i in range(0, correct_author.__len__()):
        if correct_author[i] not in author_name_token_dict.keys():
            author_name_token_dict[correct_author[i]] = [token_files[i]]
            #print(author_name_token_dict[french_correct_author[i]])
        else:
            existing_token_files = author_name_token_dict[correct_author[i]]
            if existing_token_files is not None:
                author_name_token_dict[correct_author[i]].append(token_files[i])
    return author_name_token_dict

def author_dictionary_italian(corpus_token_path):
    """Take a path to a folder of token files and a file of correct authors
            and for each author, create a dictionary of words for all respective tokens
            (works for Italian corpora)
            Keyword arguments:
            corpus_token_path -- folder path of tokens
            correct_author_path -- a file of correct authors
        """
    token_files = os.listdir(corpus_token_path)
    correct_author = [filename.split('_')[0] for filename in token_files]
    author_name_token_dict = {}
    for i in range(0, correct_author.__len__()):
        if correct_author[i] not in author_name_token_dict.keys():
            author_name_token_dict[correct_author[i]] = [token_files[i]]
            # print(author_name_token_dict[french_correct_author[i]])
        else:
            existing_token_files = author_name_token_dict[correct_author[i]]
            if existing_token_files is not None:
                author_name_token_dict[correct_author[i]].append(token_files[i])
    return author_name_token_dict

def most_common_words_from_file(filepath, col_num = 1, word_separator = "\t",line_separator = "\n"):
    lines = read_file(filepath).split(line_separator)
    selected_column = []
    for line in lines:
        words = line.split(word_separator)
        if(words.__len__() > col_num):
            selected_column.append(words[col_num])
    return selected_column


def most_common_words_from_corpus(text, occurence = 2):
    """Given a text, extract the types and their frequency, returns those types which have at least given number of occurences.
        Say a word occurs twice, and occurence = 3, then the word is not selected.
        Keyword arguments:
            text -- given text
            occurence - those words are allowed which have a minimum occurence as specified
    """
    words = tokenize.word_tokenize(text.lower())
    word_frequency = FreqDist(words)
    selected_words = [key for key in word_frequency.keys() if word_frequency.get(key) >= occurence]
    return selected_words