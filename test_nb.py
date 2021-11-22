#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 23:06:02 2021

@author: arielavshalom
"""

train = [['comedy', 'fun', 'couple', 'love', 'love'],
['action','fast','furious','shoot'],
['comedy', 'couple','fly','fast','fun','fun'],
['action','furious','shoot','shoot','fun'],
['action','fly','fast','shoot','love']]

test = ['fast','couple','shoot','fly']

train_vocab= set([word for review in train for word in review[1:]])

word_dict = dict()

for review in train:
    counter = 0
    for word in review:
        if counter == 0:
            print('smth')
            counter+= 1
            continue
        print('nthg')
        word_dict[word] = word_dict.get(word, 0) + 1
        counter+= 1

