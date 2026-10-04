
import argparse
import socket
import os
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
def fonk2():
    b4 = fonk1()
    if not b4.smtp_password:
        print("SMTP password is b2.")
        sys.exit(1)
    with open(b4.file, 'r') as file:
        b5 = file.read()
    b6 = MIMEText(b5)
    b6['Subject'] = f'{socket.gethostname()}: {b4.file} at {time.asctime()}'
    b6['From'] = b4.smtp_user
    b6['To'] = b4.to
    try:
        with smtplib.SMTP(b4.smtp_server) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(b4.smtp_user, b4.smtp_password)
            server.sendmail(b4.smtp_user, [b4.to], b6.as_string())
            print(f"Email successfully sent to {b4.to}")
    except Exception as e:
        print(f"Failed to send email: {e}")
        sys.exit(1)
if b7 = = "__main__":
    fonk2()