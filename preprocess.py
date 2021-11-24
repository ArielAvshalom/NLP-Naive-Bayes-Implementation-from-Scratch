#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 14:03:22 2021
@author: arielavshalom
"""
import os, string

##############Global Variables
#positive class of training data
path_to_pos_train = r'movie-review-HW2/aclImdb/train/pos'
#negative class of training data
path_to_neg_train = r'movie-review-HW2/aclImdb/train/neg'
#positive class of testing data
path_to_pos_test = r'movie-review-HW2/aclImdb/test/pos'
#negative class of testing data
path_to_neg_test = r'movie-review-HW2/aclImdb/test/neg'
#file with list of all expected vocabulary words
vocab_file = r'movie-review-HW2/aclImdb/imdb.vocab'
##############

##############Helper Functions
#collect all filepaths of a class. Can be easily modified to pass through whole dataset and automatically separate by classes and train/test.
def lociCollect(lociPath: str) -> list:
    listofFiles = []
    
    for root, dirname, fname in os.walk(lociPath):
        dirname.sort(reverse = True)
        for file in fname:
            filepath = os.path.join(root, file)
            listofFiles.append(filepath)
    return(listofFiles)

#lowercase every letter and remove all punctuation in a file. Returns text.
def clean_file(file_path):
    text = ''
    with open(file_path, 'r') as file:
        for line in file:
            text = "".join([text, line])
    
    return text.lower().translate(str.maketrans('', '', string.punctuation))

##############


vocab = set()

with open(vocab_file, 'r') as file:
    for word in file:
        vocab.add(word[:-1])
vocab_size = len(vocab)




pos_train = lociCollect(path_to_pos_train)




