
######################### ESSENTIALS #########################

import random
import pandas as pd
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer, make_column_transformer

######################### NLP #########################
import string
from nltk import word_tokenize
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import stopwords


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
    random.shuffle(clean_txt)

    return clean_txt
