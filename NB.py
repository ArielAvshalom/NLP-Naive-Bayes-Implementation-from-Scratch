#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 14:33:07 2021

@author: arielavshalom
"""

import pickle

#############Train Dictionaries


with open(r'neg_train_dict.pickle', 'rb') as file:
    neg_train_dict = pickle.load(file)
    
with open(r'pos_train_dict.pickle', 'rb') as file:
    pos_train_dict = pickle.load(file)
    
#############Test Vectors

with open(r'pos_test_vector.pickle', 'rb') as file:
    pos_test_vector= pickle.load(file)
    
with open(r'neg_test_vector.pickle', 'rb') as file:
    neg_test_vector = pickle.load(file)
    
combined_test_set = pos_test_vector.extend(neg_test_vector)

#############Vocab File

vocab_file = r'movie-review-HW2/aclImdb/imdb.vocab'
    
#############Helper Functions

#generate the vocabulary set and return the size of the set.
def generate_vocab_set(vocab_file):
    vocab = set()
    
    with open(vocab_file, 'r') as file:
        for word in file:
            vocab.add(word[:-1])
    
    vocab_size = len(vocab)
    
    return vocab_size





#############Main

def main():
    
    vocab_size = generate_vocab_set(vocab_file)
    
    pos_dict_size, neg_dict_size = sum([value for value in pos_train_dict.values()]), sum([value for value in neg_train_dict.values()])
    
    
    
    
    