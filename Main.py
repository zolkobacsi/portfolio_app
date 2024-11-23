import streamlit as st
import pandas


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("Images/photo.jpg", )

with col2:
    st.title("Zoltan")
    content = """
    Hi, my name is Zoltan and I want to show you some of the projects that I have been working on.
    """
    st.info(content)

content2 = """
Below you can see my projects in a specified order.
"""

st.title(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source code](https://github.com/zolkobacsi)")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])