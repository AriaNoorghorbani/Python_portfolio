import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Aria Noorghorbani")
    content = """As a dedicated Frontend Developer, I specialize in crafting functional and user-friendly 
    applications that cater to diverse client needs. With four years of hands-on experience in JavaScript 
    development, I've honed my skills in Angular, Node.js, and Bootstrap to deliver top-notch solutions.

My journey began with a background in Physics. Still, my passion for computer science led me to a transformative 
decision - I left my university course to pursue a career in web development. Along the way, I've accumulated 
multiple certifications from reputable platforms like Meta, Udemy, LinkedIn, and Coursera.

I thrive on learning, evolving, and embracing new concepts and technologies. My commitment to helping others and 
resolving challenges with innovative solutions is at the core of my professional ethos. I'm a proactive and 
collaborative team player, driven by the pursuit of excellence in every project."""
    st.write(content)

content2 = """I thrive on learning, evolving, and embracing new concepts and technologies. My commitment to helping 
oI thrive on learning, evolving, and embracing new concepts and technologies. My commitment to helping o"""
st.write(content2)

col3, empty_space, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(image=f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(image=f"images/{row['image']}")
