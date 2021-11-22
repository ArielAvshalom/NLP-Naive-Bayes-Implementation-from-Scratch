#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 14:03:22 2021

@author: arielavshalom

    
"""

import os, string

vocab_file = r'movie-review-HW2/aclImdb/imdb.vocab'

vocab = set()

with open(vocab_file, 'r') as file:
    for word in file:
        vocab.add(word[:-1])

vocab_size = len(vocab)


def lociCollect(lociPath: str) -> list:
    listofFiles = []
    
    for root, dirname, fname in os.walk(lociPath):
        dirname.sort(reverse = True)
        for file in fname:
            filepath = os.path.join(root, file)
            listofFiles.append(filepath)
    return(listofFiles)


pos_train = lociCollect(path_to_pos_train)

def clean_file(file_path):
    text = ''
    with open(file_path, 'r') as file:
        for line in file:
            text = "".join([text, line])
    
    return text.lower().translate(str.maketrans('', '', string.punctuation))
