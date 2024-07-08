import smtplib
import ssl


def send_email(user_message):
    host = "smtp.gmail.com"
    port = 465
    username = "rishil13123@gmail.com"
    password = "lkiwaktwxjxutjom"
    receiver = "rishil13123@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, user_message)
