import requests
import json
import pickle
import streamlit as st
from streamlit_lottie import st_lottie
import json

from potluck_code.model import easy_search
import pandas as pd
from gensim.models import Word2Vec

#from google.oauth2 import service_account
#from google.cloud import storage

# Create API client.
#credentials = service_account.Credentials.from_service_account_info(
#   st.secrets["gcp_service_account"]
#)



# ---add heading---

st.set_page_config(page_title="Pot Luck", page_icon=":stew:", layout="wide")

@st.cache_resource
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

@st.cache_resource
def load_lottiefile(path):
    with open(path, 'r') as f:
        return json.load(f)

# USE LOCAL CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(F"<style>{f.read()}</style>", unsafe_allow_html=True)

css_path = "style/style.css"

local_css(css_path)

# LOAD ASSETS

#lottie_coding = load_lottieurl('https://assets3.lottiefiles.com/packages/lf20_fefIZO.json')
lottie_coding = load_lottiefile('style/lottie_animation.json')



# code for local loading
@st.cache_data
def load_df():
    data_path = 'raw_data/clean_df.pkl'
    df = pd.read_pickle(data_path)
    return df
df = load_df()



# GCS code to add - to replace load_df function; what to put instead of 'download_as_string'?:
# @st.cache_resource
# def read_file(bucket_name, file_path):
#     client = storage.Client(credentials=credentials)
#     bucket = client.bucket(bucket_name)
#     blob = bucket.blob(file_path)
#     # content = bucket.blob(file_path).download_as_string()

#     pickle_in = blob.download_as_string()
#     df = pickle.loads(pickle_in)
#     # df = pd.read_pickle(pickle_in)

#     return df

# bucket_name = "potluck_bucket"
# file_path = "clean_df.pkl"

#df = read_file(bucket_name, file_path)




@st.cache_resource
def load_model():
    data_path2 = 'potluck_code/food2vec_models/model.bin'
    model = Word2Vec.load(data_path2)
    return model
model = load_model()

# HEADER SECTION & INTRO
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.title('Welcome to Pot Luck :stew:')
        st.subheader('Here to make your meal time more interesting...')
    with right_column:
        st.write('Created by Tim, Eva, Omar and Alex, Pot Luck is here to help make the most of what is in your cupboards.')
        st.write('Not had time to go shopping yet this week?')
        st.write('Do you have a numerous random ingredients leftover that you are not sure what to do with?')
        st.write('Pot Luck will offer a solution...')
    st.write('---')

# SEARCH FUNCTION
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:

        with st.form('Where the magic happens...'):
           # st.markdown(f'<h6 style="color:#fbe8a6">{"Enter your ingredients here, separated by a comma"}</h6>', unsafe_allow_html=True)
            ingredients = st.text_area(label='**Enter your ingredients here, separated by a comma**')
                                       #, label_visibility='hidden')

            mix = st.slider('**How adventurous are you feeling ?**', 0, 5, value=2)

            button_style = """
                            <style>
                            .stButton > button {
                                color: #fbe8a6;
                                background: #303c6c;
                                width: 200px;
                                height: 50px;
                            }
                            </style>
                            """

            st.markdown(button_style, unsafe_allow_html=True)
            submission = st.form_submit_button('**I am hungry...**')


            if submission and ingredients == '':
                st.write('Please enter some ingredients :tomato: :corn: :eggplant:')

            elif submission:
                prediction = easy_search(model, df, ingredients.split(','), int(mix))

                recipes = len(prediction)

    with right_column:
        st_lottie(lottie_coding, height=300, key='coding')

    st.write('---')

# RETURN RECIPES
with st.container():
    st.subheader('Here are some suggestions...')
    st.markdown('##')
    if submission and ingredients == '':
        st.write('No recipes available')
    elif submission and recipes > 0:
        wcols = 2
        cols = st.columns(wcols, gap='medium')
        for i in range(recipes):
            col = cols[i%wcols]
            with col:
                left, middle, right = st.columns([4,1,2])
                with left:
                    name = prediction.iloc[i]['name']
                    st.markdown(f'<h5 style="color:#f4976c">{name}</h5>', unsafe_allow_html=True)
                with right:
                    rating = f"Average Rating {prediction.iloc[i]['avg_rating']}:star:"
                    st.markdown(f'<p1 style="color:#f4976c">{rating}</p1>', unsafe_allow_html=True)
                with middle:
                    rating = f"{prediction.iloc[i]['minutes']} mins"
                    st.markdown(f'<p1 style="color:#f4976c">{rating}</p1>', unsafe_allow_html=True)
                with st.expander('Expand for full recipe'):
                    st.write('Ingredients\n', prediction.iloc[i]['ingredients'])
                    st.text('')
                    st.write('Steps\n', prediction.iloc[i]['steps'])
                st.markdown('#')

    elif submission:
        st.write('Sorry no recipes, might be time to go to the shops..! :blush:')
