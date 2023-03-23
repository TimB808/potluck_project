
# import preproc fn
import pandas as pd

from potluck_code.logic.preprocessor import preproc_input

from gensim.models import Word2Vec

## embedding

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



# define search

def easy_search(user_input, k):
    # load baseline df
    baseline_df = pd.read_pickle('/home/tim/code/TimB808/potluck_project/raw_data/baseline_df_short.csv')


    # Preproc
    preprocced_input = preproc_input(user_input)
    print(preprocced_input)

    #load the model
    model = Word2Vec.load('/home/tim/code/TimB808/potluck_project/potluck_code/logic/food2vec_models/model.bin')

    # word2vec search function - to get extended list of similar ings
    ext_set = word2vec_search(preprocced_input, model, k)

    # search after applying preproc
    return baseline_df[baseline_df['clean_ingredients_set'].apply(lambda x: x.issubset(ext_set))]
