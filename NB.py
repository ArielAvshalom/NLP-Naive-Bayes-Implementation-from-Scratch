#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 14:33:07 2021

@author: arielavshalom
"""

import pickle, time, math, csv, random

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
    
combined_test_set = []
combined_test_set.extend(pos_test_vector)
combined_test_set.extend(neg_test_vector)

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
    
    missing_test_results = len(combined_test_set)
    
    vocab_size = generate_vocab_set(vocab_file)
    
    pos_dict_size, neg_dict_size = sum([value for value in pos_train_dict.values()]), sum([value for value in neg_train_dict.values()])
    
    test_results = []
    
    for test in combined_test_set:
        
        #variables which reset for every test
        test_result = []
        test_result.append(test.pop())
        p_pos, p_neg = 1, 1 #probability set to a large number because messing with logs and absolutes would be annoying below. Precision can be pretty annoying.
        
        for word in test:
            try: #no add one smoothing on this section.
                p_pos*= math.log((pos_train_dict[word] + 1)/(pos_dict_size+vocab_size), 60)
            except KeyError:
                p_pos*= math.log(1/(pos_dict_size+vocab_size), 60)
                
            try: #no add one smoothing on thi
                p_neg*= math.log((neg_train_dict[word] + 1)/(neg_dict_size+vocab_size), 60)
            except KeyError:
                p_neg*=math.log(1/(neg_dict_size+vocab_size), 60)
            
            #print(p_pos, p_neg)
        #time.sleep(2)
        test_result.append(abs(p_pos))
        test_result.append(abs(p_neg))
        
        if p_pos > p_neg:
            test_result.append('pos')
        elif p_neg < p_pos:
            test_result.append('neg')
        else:
            test_result.append(random.choice(['pos', 'neg']))
            missing_test_results-=1
            
            
        test_results.append(test_result)
        
    
    number_of_correct_predictions = 0
    
    for result in test_results:
        if result[0] == result[-1]:
            number_of_correct_predictions += 1
    
    print(number_of_correct_predictions)
    print(f"approximately {len(combined_test_set) - missing_test_results} predictions had errors because we approached a value that Python couldn't measure (precision error). \nThese results were randomly assigned pos or neg class. ")
    
    return test_results, number_of_correct_predictions/len(combined_test_set)
            
            
test_results, percent_prediction = main()

if __name__ == "__main__":
    
    with open('test_results.csv', mode='w') as test_file:
        writer = csv.writer(test_file, delimiter=',')

        writer.writerow(['actual class', 'positive class choice', 'negative class choice','prediction'])
        
        for test in test_results:
            writer.writerow(test)
    