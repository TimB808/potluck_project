import joblib
from matplotlib.pyplot import clf
from potluck_code.logic import model


def predict(ingredients, mix):
    clf = model.easy_search(ingredients, mix)
    return clf

# testing the predict function
if __name__=='__main__':
    print(predict(['water', 'salt', 'tomatoes'], 3))
    # print('Please enter some ingredients')
