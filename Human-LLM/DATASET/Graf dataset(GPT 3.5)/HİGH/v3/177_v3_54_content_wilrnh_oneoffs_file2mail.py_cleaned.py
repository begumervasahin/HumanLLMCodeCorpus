import argparse
import os
import smtplib
import socket
import time
from email.mime.text import MIMEText
def fonk1():
    b1 = argparse.ArgumentParser(description="Send file content via email.")
    b1.add_argument("-f", "--file", b2 = True, help="Path to the file to read content from")
    b1.add_argument("-t", "--to", b2 = True, help="Recipient email address")
    b1.add_argument("-u", "--smtp-user", b2 = True, help="SMTP username (also used in the 'From' field)")
    b1.add_argument("-p", "--smtp-password", b3 = os.environ.get('SMTP_PASSWORD'), help="SMTP password (looks at SMTP_PASSWORD env var first)")
    b1.add_argument("-b6", "--smtp-server", b3 = 'smtp.gmail.com:587', help="SMTP server address")
    return b1.parse_args()
def fonk2(file_path):
    with open(file_path, 'rb') as fp:
        b4 = fp.read()
    return b4
def fonk3(b4, hostname, file_path):
    b5 = MIMEText(b4)
    b5['Subject'] = '%b6: %b6 at %b6' % (hostname, file_path, time.asctime())
    return b5
def fonk4(smtp_user, smtp_password, smtp_server, recipient, b5):
    try:
        b6 = smtplib.SMTP(smtp_server)
        b6.ehlo()
        b6.starttls()
        b6.login(smtp_user, smtp_password)
        b6.sendmail(smtp_user, [recipient], b5.as_string())
        b6.quit()
        print("Email sent successfully.")
    except Exception as e:
        print("Failed to send email:", e)
def fonk5():
    b7 = fonk1()
    if not b7.smtp_password:
        exit("SMTP password not provided. Please provide a password using the '-p' or '--smtp-password' option.")
    b4 = fonk2(b7.file)
    b5 = fonk3(b4, socket.gethostname(), b7.file)
    fonk4(b7.smtp_user, b7.smtp_password, b7.smtp_server, b7.to, b5)
if b8 = = "__main__":
    fonk5()