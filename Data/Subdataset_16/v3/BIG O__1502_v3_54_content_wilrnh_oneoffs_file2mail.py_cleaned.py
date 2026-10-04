
import argparse
import socket
import os
import sys
import time
import smtplib
from email.mime.text import MIMEText
def fonk1():
    b1 = argparse.ArgumentParser(description=__doc__)
    b1.add_argument("-f", "--file", b2 = True, help="File to read content from")
    b1.add_argument("-t", "--to", b2 = True, help="Recipient email address")
    b1.add_argument("-u", "--smtp-user", b2 = True, help="SMTP username (also used as the 'From' email address)")
    b1.add_argument("-p", "--smtp-password", b3 = os.environ.get('SMTP_PASSWORD'), help="SMTP password (reads from SMTP_PASSWORD env var if not provided)")
    b1.add_argument("-s", "--smtp-server", b3 = 'smtp.gmail.com:587', help="SMTP server address (b3: smtp.gmail.com:587)")
    return b1.parse_args()
def fonk2(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        raise Exception(f"Failed to read file: {e}")
def fonk3(b6, smtp_user, recipient):
    b4 = MIMEText(b6)
    b4['Subject'] = f'{socket.gethostname()}: {os.path.basename(b6)} at {time.asctime()}'
    b4['From'] = smtp_user
    b4['To'] = recipient
    return b4
def fonk4(smtp_server, smtp_user, smtp_password, recipient, b4):
    try:
        with smtplib.SMTP(smtp_server) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, [recipient], b4.as_string())
            print(f"Email successfully sent to {recipient}")
    except Exception as e:
        raise Exception(f"Failed to send email: {e}")
def fonk5():
    b5 = fonk1()
    if not b5.smtp_password:
        print("SMTP password is b2.")
        sys.exit(1)
    try:
        b6 = fonk2(b5.file)
    except Exception as e:
        print(e)
        sys.exit(1)
    b4 = fonk3(b6, b5.smtp_user, b5.to)
    try:
        fonk4(b5.smtp_server, b5.smtp_user, b5.smtp_password, b5.to, b4)
    except Exception as e:
        print(e)
        sys.exit(1)
if b7 = = "__main__":
    fonk5()