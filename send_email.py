import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "valentino.tarantino@gmail.com"
password = "yync kmtp voxf qssj"

receiver = "valentino.tarantino@gmail.com"
context = ssl.create_default_context()

message = """\
subject: Answer Email
Hi
How are you?
Bye
"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)