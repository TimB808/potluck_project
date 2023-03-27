import requests
import streamlit as st
import os
from streamlit_lottie import st_lottie
from website.prediction import predict
import os


st.set_page_config(page_title="Pot Luck", page_icon=":stew:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# USE LOCAL CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(F"<style>{f.read()}</style>", unsafe_allow_html=True)

root_dir = os.path.dirname(__file__)
css_path = root_dir+"/style/style.css"

local_css(css_path)

# LOAD ASSETS
lottie_coding = load_lottieurl('https://assets3.lottiefiles.com/packages/lf20_fefIZO.json')

# HEADER SECTION
with st.container():
    st.title('Welcome to Pot Luck :stew:')
    st.write('---')

# INTRO AND SEARCH FUNCTION
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader('Here to make your meal time more interesting...')
        st.write('Created by Tim, Eva, Omar and Alex, Pot Luck is here to help make the most of what is in your cupboards. Not had time to go shopping yet this week? Do you have a numerous random ingredients leftover that you are not sure what to do with? Pot Luck will offer a solution...')

        with st.form('Where the magic happens...'):
            ingredients = st.text_area('Enter your ingredients here, separated by a comma')
            mix = st.slider('How adventurous are you feeling ?', 1, 5, value=3)

            submission = st.form_submit_button('I am hungry...')

            if submission and ingredients == '':
                st.caption('Please enter some ingredients :tomato: :corn: :eggplant:')

            elif submission:
                prediction = predict(ingredients.split(','), int(mix))

                recipes = len(prediction)

    with right_column:
        st_lottie(lottie_coding, height=300, key='coding')

    st.write('---')

# RETURN RECIPES
with st.container():
    st.subheader('Here are some suggestions...')
    if submission and ingredients == '':
        st.write('No recipes available')
    elif submission and recipes > 0:
        wcols = 3
        cols = st.columns(wcols)

        for i in range(recipes):
            col = cols[i%wcols]

            with col:
                st.markdown(prediction.iloc[i]['name'])
                with st.expander('Expand for full recipe'):
                    st.write(prediction.iloc[i]['steps'])
    elif submission:
        st.caption('Sorry no recipes, might be time to go to the shops..! :blush:')
