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


def get_freq_dist_from_corpus(text):
    """Given a text, extract the types and their frequency
        Keyword arguments:
            text -- given text
    """
    words = tokenize.word_tokenize(text.lower())
    return FreqDist(words)


def get_words_with_freq_at_least_n(text, n = 2):
    """Given a list of documents, extracts a list of words having frequency greater than or equal to the occurrence mentioned
        Keyword arguments:
            doc_names_list -- list of document names
            n - those words are selected which have frequency greater than or equal to n
    """
    word_freq_dists = get_freq_dist_from_corpus(text)
    selected_words = [word for word,freq in word_freq_dists if freq >= n]
    return selected_words


def get_complete_text(doc_list):
    """Given a list of documents, returns the concatenated text contained in all of them
        Keyword arguments:
            text -- given text
            window_size - number of characters in a window
            step_size - number of characters to skip before beginning next windows
    """
    complete_text = ""
    for doc in doc_list:
        text = read_file( doc, mode='rb', ignore_comments= False).decode('utf-8')
        complete_text = complete_text + text
    return complete_text


def append_folder_path_to_doc_list(doc_list, folder_path):
    """Given a list of documents, returns the concatenated text contained in all of them
        Keyword arguments:
            text -- given text
            window_size - number of characters in a window
            step_size - number of characters to skip before beginning next windows
    """
    doc_paths =[]
    for doc in doc_list:
        doc_paths.append(folder_path + doc)
    return  doc_paths

