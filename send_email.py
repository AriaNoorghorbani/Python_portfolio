import smtplib, ssl
import os
from enviremnet import my_env

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "valentino.tarantino@gmail.com"
    # password = os.getenv("VALENTINO_SEND_EMAIL_PASSWORD")
    password = my_env.VALENTINO_SEND_EMAIL_PASSWORD

    receiver = "valentino.tarantino@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
