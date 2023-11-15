import streamlit as st

st.header("Contact Me")

with st.form(key="contact-me"):
    email = st.text_input("Your Email:")
    message = st.text_area(label="Write your message:")
    submit_btn = st.form_submit_button("Submit")

    if submit_btn:
        print("Submited")