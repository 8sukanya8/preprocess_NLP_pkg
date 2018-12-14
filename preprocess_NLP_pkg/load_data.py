"""This file contains functions for reading in text data in different formats
"""
import lzma


def read_file(filepath, mode = 'r'): # rb for raw binary
    """Read the contents of a file
        filepath -- path to a file to be read
    """
    f = open(filepath, mode)# encoding = encoding)
    file_content = ""
    try:
        file_content = f.read()
    finally:
        f.close()
    return file_content




def read_compressed_lzma_file(character_seq):
    lzma.open(character_seq, mode="rb")
    lzma.LZMAFile(filename=character_seq, mode="r")