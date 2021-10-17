# Import statements
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image


#Title and Subheader
st.title("Life Expectancy By Country")
st.write("Life Expectancy Data of India and USA from the year 1960 till 2016.")

# Multicolumn Support (add relative path to the image)
col1, col2 = st.beta_columns(2)
IN_flag = Image.open(r"xxxxxxxxxxxxxxx")
col1.header("INDIA")
col1.image(IN_flag, use_column_width=True)

US_flag = Image.open(r"xxxxxxxxxxxxxxxx")
col2.header("USA")
col2.image(US_flag, use_column_width=True)

# reading a csv and displaying the first six rows on the screen.
df = pd.read_csv('lf.csv')
st.write(df.head())

# Display full data base on checkbox.
if st.checkbox('show full data'):
    df
    
# Display Code
st.write('Displaying Code in Streamlit app')
with st.echo():
    # square function
    def square(x):
        print(x*x)
    # cube function
    def cube(x):
        print(x*x*x)
    square(5) #output 25
    cube(5) # output 125  
# Sidebar Column
st.sidebar.title('Sidebar Widgets')

rating = st.sidebar.radio('Are You Happy with the Example',('Yes','No','Not Sure'))
if rating == 'Yes':
    st.sidebar.success('Thank You for Selecting Yes')
elif rating =='No':
    st.sidebar.info('Thank You for Selecting No')
elif rating =='Not Sure':
    st.sidebar.info('Thank You for Selecting Not sure')

rating = st.sidebar.selectbox("How much would you rate this App? ",
                     ['5 Stars', '4 Stars', '3 Stars','2 Stars','1 Star'])

st.sidebar.success(rating)

st.sidebar.write('Find Square of a Number')
get_number = st.sidebar.slider("Select a Number", 1, 10)
st.sidebar.write('Square of Number',get_number, 'is', get_number*get_number)
# displaying API data
API_URL = 'https://cleanuri.com/api/v1/shorten'
st.subheader('URL SHORTNER')
_url = st.text_input('Enter URL')
pressed = st.button('Get Short Link')

if pressed:
    if _url !='':
        data = {'url': _url}
        r = requests.post(API_URL, data=data)
        st.write(r.json())
    else:
        st.write('Please enter the right URL first')
