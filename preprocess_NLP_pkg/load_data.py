"""This file contains functions for reading in text data in different formats
"""
import lzma
import os
import fnmatch


def read_file(filepath, mode = 'r', ignore_comments = True): # rb for raw binary, note that rb can only be used if ignore_comments==False . Also, remember to decode using '.decode('utf-8')
    """Read the contents of a file
        Keyword arguments:
            filepath -- path to a file to be read
    """
    f = open(filepath, mode)# encoding = encoding)
    file_content = ""
    try:
        if ignore_comments is False:
            file_content = f.read()
        else:
            for line in f:
                if not line.startswith("#"):
                    file_content = file_content + line
    finally:
        f.close()
    return file_content


def read_compressed_lzma_file(character_seq):
    """Read the contents of a compressed lzma_file
        Keyword arguments:
            filepath -- path to a file to be read
    """
    lzma.open(character_seq, mode="rb")
    lzma.LZMAFile(filename=character_seq, mode="r")


def write_file(filepath, text, mode = 'w'):
    """Write a text into a file
        Keyword arguments:
            filepath -- path to a file to be written
            text -- text to be written
            mode -- mode of writing, default is overwrite
    """
    f = open(filepath, mode)
    f.write(text)
    f.close()

def load_files_from_dir(dir, pattern = "*"):
    """Given a directory, load files. If pattern is mentioned, load files with given pattern
        Keyword arguments:
            text -- given text
            delimiter - type of delimiter to be used, default value is '\n\n'
    """
    try:
        return(fnmatch.filter(os.listdir(dir), pattern))
    except TypeError:
        print("Error! pattern should be a string or bytes like object. Returning None")
        return None
