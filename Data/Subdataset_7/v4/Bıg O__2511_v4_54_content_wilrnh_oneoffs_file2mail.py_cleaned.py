import argparse
import os
import socket
import smtplib
import time
from email.mime.text import MIMEText
b1 = argparse.ArgumentParser(description=)
b1.add_argument("-f", "--file", b2 = True, help="File to read content from.")
b1.add_argument("-t", "--to", b2 = True, help="Email address to send file content to.")
b1.add_argument("-u", "--smtp-user", b2 = True, help="Username used to login to SMTP server. Also the email used in the From: field.")
b1.add_argument("-p", "--smtp-password", b3 = os.environ.get('SMTP_PASSWORD'), help="Password used to login to SMTP server. Looks at SMTP_PASSWORD environment variable first. REQUIRED.")
b1.add_argument("-s", "--smtp-server", b3 = 'smtp.gmail.com:587', help="SMTP server to send mail from.")
b4 = b1.parse_args()
if not b4.smtp_password:
    exit(b1.print_usage())
with open(b4.file, 'rb') as fp:
    b5 = MIMEText(fp.read())
b5['Subject'] = '%s: %s at %s' % (socket.gethostname(), b4.file, time.asctime())
b5['From'] = b4.smtp_user
b5['To'] = b4.to
b6 = smtplib.SMTP(b4.b6)
b6.ehlo()
b6.starttls()
b6.login(b4.smtp_user, b4.smtp_password)
b6.sendmail(b4.smtp_user, [b4.to], b5.as_string())
b6.quit()