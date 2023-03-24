
# import preproc fn
import pandas as pd

from potluck_code.logic.preprocessor import preproc_input

from gensim.models import Word2Vec

import os

## embedding - in case needed later

#download the data from github
#wget https://github.com/ChantalMP/Exploiting-Food-Embeddings-for-Ingredient-Substitution/releases/download/0.1/food2vec_models.zip
#unzip -qq food2vec_models.zip


#extend user input by the nearest ingredients found in the model

def word2vec_search(user_input, model, k):
    extended_input = list(user_input)
    for ingr in list(user_input):
        try:
            k_nearest_ingr = model.wv.most_similar(ingr, topn=k)
            k_nearest_list = [i[0] for i in k_nearest_ingr]
        except KeyError:
            continue
        extended_input += k_nearest_list
    return set(extended_input)



# define search function

def easy_search(user_input, k):
    # load baseline df
    data_path = os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd())))+'raw_data/baseline_df_short.csv'
    baseline_df = pd.read_pickle(data_path)

    # Preproc
    preprocced_input = preproc_input(user_input)

    #load the model
    root_dir = os.path.dirname(__file__)
    data_path2 = root_dir+'/food2vec_models/model.bin'
    model = Word2Vec.load(data_path2)

    # word2vec search function - to get extended list of similar ings
    ext_set = word2vec_search(preprocced_input, model, k)

    # search after applying preproc
    return baseline_df[baseline_df['clean_ingredients_set'].apply(lambda x: x.issubset(ext_set))]
