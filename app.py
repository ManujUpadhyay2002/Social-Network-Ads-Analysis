import streamlit as st
import pickle as pkl
import pandas as pd

st.title("Social  Network  Ads  Analysis")

model = pkl.load(open('pipe.pkl', 'rb'))

sex = st.selectbox('Select Your Gender',('Male', 'Female'))
age = st.text_input('Enter Your Age' )
salary = st.text_input('Enter Your Salary')

data = pd.DataFrame([sex,age,salary]).transpose()
if st.button('Predict'):
    # 1. predict
    result = model.predict(data)
    # 2. display
    if result == 1:
        st.header("Customer Will Purchase Product")
    else:
        st.header("Customer Will Not Purchase Product")