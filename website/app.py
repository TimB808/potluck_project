import requests
import streamlit as st
from streamlit_lottie import st_lottie
from website.prediction import predict

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

local_css('../style/style.css')

# LOAD ASSETS
lottie_coding = load_lottieurl('https://assets3.lottiefiles.com/packages/lf20_fefIZO.json')

# HEADER SECTION
with st.container():
    st.title('Welcome to Pot Luck :stew:')
    st.write('---')

# INTRO CONTENT
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader('Here to make your meal time more interesting...')
        st.write('Created by Tim, Eva, Omar and Alex, Pot Luck is here to help make the most of what is in your cupboards. Not had time to go shopping yet this week? Do you have a numerous random ingredients leftover that you are not sure what to do with? Pot Luck will offer a solution...')

    with right_column:
        st_lottie(lottie_coding, height=300, key='coding')

st.write('---')

# SEARCH FUNCTION AND SUGGESTION
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        with st.form('Where the magic happens...'):
            ingredients = st.text_area('Enter your indregients here...', 'honey')
            # function to convert data format ?

            st.form_submit_button('Im feeling lucky')
            prediction = predict(ingredients)

    with right_column:
        st.subheader('Where the recipes are returned')
        # returns prediction, check data type
