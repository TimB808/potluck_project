from potluck_code.logic import model


def predict(food2vec, df, ingredients, mix, num_ing):
    return model.easy_search(food2vec, df, ingredients, mix, num_ing)

# testing the predict function
if __name__=='__main__':
    print(predict(['water', 'salt', 'tomatoes'], 3))
    # print('Please enter some ingredients')
