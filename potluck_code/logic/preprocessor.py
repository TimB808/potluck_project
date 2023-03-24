
######################### ESSENTIALS #########################

import pandas as pd
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer, make_column_transformer

######################### NLP #########################
import string

'''
from nltk import word_tokenize
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import stopwords
'''

def remove_num(text):
    text = ''.join(char for char in text if not char.isdigit())
    return text

def remove_punct_list(text):
    cleaned_text = []
    for word in text:
        for punctuation in string.punctuation:
            word = word.replace(punctuation, '')
        cleaned_text.append(word)
    return cleaned_text


def tokenize(ingr_list):
    tokenized_list = []
    for ingr in ingr_list:
        tokenized_list += ingr.split(' ')
    return tokenized_list

#preprocessing for df
def preprocess_text(text):

    # make string lowercase
    text = text.lower()

    # remove num
    text = ''.join(char for char in text if not char.isdigit())

    # change str to list
    str_to_list = text.strip('[]').split(',')

    # remove spaces
    clean_txt = [text.strip() for text in str_to_list]

    # remove punct from list
    clean_txt = remove_punct_list(clean_txt)

    # Tokenize
    clean_txt = tokenize(clean_txt)

    # convert list to set and shuffle
    clean_txt = set(clean_txt)

    return clean_txt

#preprocessing for user input

def preproc_input(user_input):
    # lowercase
    my_ing = [ingr.lower() for ingr in user_input]
    # print(f'{my_ing}  lowercased. Type is {type(my_ing)}')

    # remove numbers and spaces
    my_ing = [remove_num(ingr).strip() for ingr in my_ing]
    # print(f'{my_ing} removed nums. Type is {type(my_ing)}')

    #remove spaces
    #my_ing = [text.strip() for text in my_ing]

    #remove punctuation
    my_ing = remove_punct_list(my_ing)
    #print(f'{my_ing} removed punct. Type is {type(my_ing)}')

    #tokenize
    my_ing = tokenize(my_ing)
    #print(f'{my_ing} tokenize. Type is {type(my_ing)}')
    ## insert the following to replace tokenise
    # my_ing = [i.replace(' ', '_') for i in my_ing]

    # add in generic ingredients (instead of removing stopwords)
    my_ing = my_ing + ['water', 'salt', 'pepper']
    #print(f'{my_ing} - added generic ings. Type is {type(my_ing)}')

    return set(my_ing)
