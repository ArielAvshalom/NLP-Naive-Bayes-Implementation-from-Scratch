#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 14:03:22 2021
@author: arielavshalom
"""
import os, string, pickle

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
    try:
    
        with open(file_path, 'r') as file:
            for line in file:
                text = "".join([text, line])
    except FileNotFoundError:
        print(f'file name {file_path} not found.')
        
    except IsADirectoryError:
        print('what is going on?')
    
    return text.lower().translate(str.maketrans('', '', string.punctuation))


#update the dictionary of words for each class using the class dictionary and current cleaned text file.
def bag_of_words_update(dictionary_of_words, cleaned_up_text):
    for word in cleaned_up_text.split(' '):
        dictionary_of_words[word] = dictionary_of_words.get(word, 0)+1
    return dictionary_of_words

#generate the vocabulary set and return the size of the set.
def generate_vocab_set(vocab_file):
    vocab = set()
    
    with open(vocab_file, 'r') as file:
        for word in file:
            vocab.add(word[:-1])
    
    vocab_size = len(vocab)
    
    return vocab_size

def convert_cleaned_file_to_list(class_name, cleaned_file):
    file_list = []
    for word in cleaned_file.split(' '):
        file_list.append(word)
    file_list.append(class_name)
    
    return file_list

def turn_test_files_into_vector_format(class_name, list_of_files):
    list_of_examples = []
    
    for file in list_of_files:
        cleaned_file = clean_file(file)
        list_of_examples.append(convert_cleaned_file_to_list(class_name, cleaned_file))
    
    return list_of_examples
        


##############Main

def main():
    pos_train_dictionary, neg_train_dictionary = dict(), dict()
    
    pos_train, neg_train = lociCollect(path_to_pos_train), lociCollect(path_to_neg_train)
    
    for file in pos_train:
        current_file = clean_file(file)
        
        bag_of_words_update(pos_train_dictionary, current_file)
    
    for file in neg_train:
        current_file = clean_file(file)
        
        bag_of_words_update(neg_train_dictionary, current_file)
        
    return pos_train_dictionary, neg_train_dictionary


if __name__ == '__main__':
    pos_dict, neg_dict = main()
    
    pos_test_vector = turn_test_files_into_vector_format('pos', lociCollect(path_to_pos_test))
    
    neg_test_vector = turn_test_files_into_vector_format('neg', lociCollect(path_to_neg_test))
    
    with open(r'pos_train_dict.pickle', 'wb') as file:
        pickle.dump(pos_dict, file)
        
    with open(r'neg_train_dict.pickle', 'wb') as file:
        pickle.dump(neg_dict, file)
        
    
    with open(r'pos_test_vector.pickle', 'wb') as file:
        pickle.dump(pos_test_vector, file)
        
    with open(r'neg_test_vector.pickle', 'wb') as file:
        pickle.dump(neg_test_vector, file)
    
    

    
    
        






    



