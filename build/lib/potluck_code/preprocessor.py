
######################### ESSENTIALS #########################

######################### NLP #########################
import string



def remove_num(text):
    return ''.join(char for char in text if not char.isdigit())

def remove_punct_list(ingr_list):
    cleaned_list = []
    for word in ingr_list:
        for punctuation in string.punctuation:
            word = word.replace(punctuation, '')
        cleaned_list.append(word)
    return cleaned_list

#preprocessing for df: to be replaced with updated vsn from jupyer notebook
def preprocess_text(text):
    pass


#preprocessing for user input
def preproc_input(user_input):
    #preproces input same way as df

    #1.lowercase
    user_input = [i.lower() for i in user_input]

    #2. remove numbers
    user_input = [remove_num(i) for i in user_input]

    #3. remove spaces
    user_input =  [i.strip() for i in user_input]

    #4. remove special chars
    user_input = remove_punct_list(user_input)

    #5. join words with underscores
    user_input = [i.replace(' ', '_') for i in user_input]

    #6. add in generic ingredients (instead of removing stopwords)
    user_input = user_input + ['water', 'salt', 'pepper']

    #7. change to set -> maybe leave it for now?
    user_input = set(user_input)

    return user_input
