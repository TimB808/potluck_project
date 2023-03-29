# import preproc fn

from potluck_code.preprocessor import preproc_input


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

def easy_search(model, df, user_input, k, num_ing=1):

    # Preproc
    preprocced_input = preproc_input(user_input)

    # word2vec search function - to get extended list of similar ings
    ext_set = word2vec_search(preprocced_input, model, k)

    # define recipe_df as full search results
    recipe_df = df[df['search_ingredients'].apply(lambda x: x.issubset(ext_set))]

    # return filtered recipe_df
    return recipe_df[recipe_df['n_ingredients'] >= num_ing]
