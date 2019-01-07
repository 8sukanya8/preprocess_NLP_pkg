"""This file contains functions for reading in text data in different formats
"""
import lzma


def read_file(filepath, mode = 'r', ignore_comments = True): # rb for raw binary
    """Read the contents of a file
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
    lzma.open(character_seq, mode="rb")
    lzma.LZMAFile(filename=character_seq, mode="r")


def write_file(filepath, text, mode = 'w'):
    """Write a text into a file
        filepath -- path to a file to be written
        text -- text to be written
        mode -- mode of writing, default is overwrite
    """
    f = open(filepath, mode)
    f.write(text)
    f.close()