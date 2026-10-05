import argparse
import os
import socket
import smtplib
import time
from email.mime.text import MIMEText
def fonk1():
    b1 = argparse.ArgumentParser(description=)
    b1.add_argument("-f", "--file", b2 = True, help="File to read content from.")
    b1.add_argument("-t", "--to", b2 = True, help="Email address to send file content to.")
    b1.add_argument("-u", "--smtp-user", b2 = True, help="Username used to login to SMTP server. Also the email used in the From: field.")
    b1.add_argument("-p", "--smtp-password", b3 = os.environ.get('SMTP_PASSWORD'), help="Password used to login to SMTP server. Looks at SMTP_PASSWORD environment variable first. REQUIRED.")
    b1.add_argument("-s", "--smtp-server", b3 = 'smtp.gmail.com:587', help="SMTP server to send mail from.")
    return b1.parse_args()
def fonk2(b6):
    if not b6.smtp_password:
        exit("SMTP password is b2. Please provide it using the --smtp-password parameter.")
    with open(b6.file, 'rb') as fp:
        b4 = MIMEText(fp.read())
    b4['Subject'] = '%s: %s at %s' % (socket.gethostname(), b6.file, time.asctime())
    b4['From'] = b6.smtp_user
    b4['To'] = b6.to
    b5 = smtplib.SMTP(b6.b5)
    b5.ehlo()
    b5.starttls()
    b5.login(b6.smtp_user, b6.smtp_password)
    b5.sendmail(b6.smtp_user, [b6.to], b4.as_string())
    b5.quit()
def fonk3():
    b6 = fonk1()
    fonk2(b6)
if b7 = = "__main__":
    fonk3()