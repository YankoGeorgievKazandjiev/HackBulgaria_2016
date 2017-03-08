import random
import smtplib
import string
from settings import *
from settings import TAN_CODE_COUNT_PER_GENERATION as TAN_COUNT

#generate 10 random tan codes

def generate_tan_codes() -> set():
    tan_codes = []
    string1 = ''
    for index in range(TAN_COUNT):
        tan_codes.append(str(random.getrandbits(200)))
    return tan_codes

#send tan_codes to email when you registrated

def send_tan_codes(email, tan_codes):
    subject = "You need to use this Tan_codes!"
    FROM = bankMail
    TO = email
    SUBJECT = subject
    TEXT = tan_codes

    message = """From: {0}\nTo: {1}\nSubject: {2}\n\n{3}
    """.format(FROM,TO, SUBJECT, TEXT)

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
