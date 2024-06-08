import streamlit as st
import pandas as pd
import numpy as np

firstname = st.text_input("Enter firstname: ", key="firstname")

a = st.slider("Number 1")
b = st.slider("Number 2")
st.write("Sum is:", a + b)

show_name = st.checkbox("Show firstname")

if show_name:
  st.write("Firstname is", firstname)

number = st.selectbox("Select a number", [1,2,3,4,5])
number

st.button("Click me")
