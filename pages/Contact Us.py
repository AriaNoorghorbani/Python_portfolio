import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="contact-me"):
    email = st.text_input("Your Email:")
    raw_message = st.text_area(label="Write your message:")
    message = f"""\
Subject: New email form {email}

From: {email}
{raw_message}
"""

    submit_btn = st.form_submit_button("Submit")

    if submit_btn:
        send_email(message)
        st.info("Your email was sent successfully.")