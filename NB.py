#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 14:33:07 2021

@author: arielavshalom
"""

import pickle

#############Train Dictionaries


with open(r'neg_train_dict.pickle', 'rb') as file:
    neg_train_dict = pickle.load()
    
with open(r'pos_train_dict.pickle', 'rb') as file:
    pos_train_dict = pickle.load()
    
