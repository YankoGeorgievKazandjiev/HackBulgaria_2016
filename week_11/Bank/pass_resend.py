import smtplib
import uuid
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import DB_NAME
from sqlalchemy import *
from module import *
from settings import *

Session = sessionmaker(bind = engine)
session = Session()

# Here we tanke email from user and database and send hashed pass to user's email

def send_email():
    subject = "Retrieve pass!!!"
    os.system('clear')
    print("Enter email:")
    email  = input('>')
    password = session.query(BankUser.password).filter(email == email).first()
    body = 'Hashed pass: {}'.format(password)
    FROM = bankMail
    TO = email
    SUBJECT = subject
    TEXT = body

    message = """From: {0}\nTo: {1}\nSubject: {2}\n\n{3}
    """.format(FROM, TO, SUBJECT, TEXT)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(bankMail, mail_pass)
        server.sendmail(FROM, TO, message)
        server.close()
        print('Successfully sent the mail')
        return True
    except:
        print("Failed to send mail")
        return False
