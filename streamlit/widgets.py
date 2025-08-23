import streamlit as st
import pandas as pd


st.title("Streamlit Text as Input")

name=st.text_input("Enter Your name")
age=st.slider("select your age:", 0, 100, 25)

option = ["Python", "Java", "C++", "JavaScript"]

choice = st.selectbox("Coose yout favorite language:", option)


if name:
    st.write(f"Hello, {name}")

    st.write(f"Your age is {age}")

    st.write(f"You selected {choice} as your favorite Programming Language")


data={
    "Name": ["John", "jane", "Jake", "jill"],
    "Age": [28,24,35,40],
    "City": ["New York", "Loss Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sample.csv")
st.write(df)

uploaded_file=st.file_uploader("Choose csv file", type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)