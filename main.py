import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")
with col2:
    st.title("Noel Saido")
    content = ("""Hi, I am Noel a python programmer passionate in software development. I like to play with codes and result in the best output from my
    work. I can solve problems analytically and face any complex situation to fix them with full vividness. In addition,
    I treat consumers with friendliness while remaining professional. As a result, I promise my passion for work and
    my unwavering commitment to completing my job is a priority""")
    st.info(content)

st.write("""Below you can find some of the apps I have built in python. Feel free to contact me!""")

df = pandas.read_csv("data.csv", sep=";")

col3, col4 = st.columns(2)

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])