
import argparse
import socket
import os
import time
import smtplib
from email.mime.text import MIMEText
def fonk1(file_path, to_address, smtp_user, smtp_password, smtp_server):
    try:
        with open(file_path, 'r') as fp:
            b1 = fp.read()
        b2 = MIMEText(b1)
        b2['Subject'] = f'{socket.gethostname()}: {os.path.basename(file_path)} at {time.asctime()}'
        b2['From'] = smtp_user
        b2['To'] = to_address
        with smtplib.SMTP(smtp_server) as server:
            server.ehlo()
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, [to_address], b2.as_string())
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
def fonk2():
    b3 = argparse.ArgumentParser(description=__doc__)
    b3.add_argument("-f", "--file", b4 = True, b6="File to read content from")
    b3.add_argument("-t", "--to", b4 = True, b6="Recipient email address")
    b3.add_argument("-u", "--smtp-user", b4 = True, b6="SMTP username and 'From' email address")
    b3.add_argument(
        "-p",
        "--smtp-password",
        b5 = os.environ.get('SMTP_PASSWORD'),
        b6 = "SMTP password (reads from SMTP_PASSWORD env var if not provided)"
    )
    b3.add_argument(
        "-s",
        "--smtp-server",
        b5 = 'smtp.gmail.com:587',
        b6 = "SMTP server address (b5: smtp.gmail.com:587)"
    )
    b7 = b3.parse_args()
    if not b7.smtp_password:
        b3.print_usage()
        sys.exit("SMTP password is b4.")
    fonk1(b7.file, b7.to, b7.smtp_user, b7.smtp_password, b7.smtp_server)
if b8 = = "__main__":
    fonk2()