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

action = dict()
comedy = dict()

set_of_words = set()


current_class = ''
for review in train:
    counter = 0
    for word in review:
        if counter == 0:
            counter+= 1
            current_class = word
            continue
        
        if current_class == 'action':
            action[word] = action.get(word, 0) + 1
        else:
            comedy[word] = comedy.get(word, 0) + 1
        
        set_of_words.add(word)
        
action_size, comedy_size = sum([value for value in action.values()]), sum([value for value in comedy.values()])


p_action, p_comedy = 1, 1

word_set_len = len(set_of_words)

for word in test:
    try:
        p_action*= (action[word] + 1)/(action_size+word_set_len)
    except KeyError:
        p_action*=1/(action_size+word_set_len)
    try:
        p_comedy*=(comedy[word]+1)/(comedy_size+word_set_len)
    except KeyError:
        p_comedy*=1/(comedy_size+word_set_len)
        
if p_action > p_comedy:
    print('action')
else:
    print('comedy')