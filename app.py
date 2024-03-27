import streamlit as st

x = st.slider('Select a valie')
st.write(x, 'squared is', x*x)