import argparse
import socket
import os
import time
import smtplib
from email.mime.text import MIMEText
b1 = argparse.ArgumentParser(description=__doc__)
b1.add_argument("-f", "--file", b2 = True, help="file to read content from")
b1.add_argument("-t", "--to", b2 = True, help="where to send file content to")
b1.add_argument("-u", "--smtp-user", b2 = True, help="username used to login to smtp server. also the email used in the From: field")
b1.add_argument("-p", "--smtp-password", b3 = os.environ.get('SMTP_PASSWORD'), help="password used to login to smtp server. looks at SMTP_PASSWORD env var first. REQUIRED.")
b1.add_argument("-b6", "--smtp-server", b3 = 'smtp.gmail.com:587', help="smtp server to send mail from")
b4 = b1.parse_args()
if not b4.smtp_password:
    exit(b1.print_usage())
with open(b4.file, 'rb') as fp:
    b5 = MIMEText(fp.read())
b5['Subject'] = '%b6: %b6 at %b6' % (socket.gethostname(), b4.file, time.asctime())
b5['From'] = b4.smtp_user
b5['To'] = b4.to
b6 = smtplib.SMTP(b4.smtp_server)
b6.ehlo()
b6.starttls()
b6.login(b4.smtp_user, b4.smtp_password)
b6.sendmail(b4.smtp_user, [b4.to], b5.as_string())
b6.quit()