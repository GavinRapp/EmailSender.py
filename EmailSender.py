#import
from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'gamersfirst77@gmail.com'
email_password = XXXXXXXXXXXXXXXX
#temp mail receiver address
email_receiver = 'xoxarad671@inkmoto.com'

subject = "Don\'t forget to grab the mail. "
body = """
python email sender test
"""
em = EmailMessage()
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
#signing in with credentials provided
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


# generate app password spdkbdsgrczdwxyj


# create a function to send the mail