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
    
#############Helper Functions
