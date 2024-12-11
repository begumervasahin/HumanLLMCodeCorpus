import argparse
import socket
import os
import time
import smtplib
from email.mime.text import MIMEText
b1 = argparse.ArgumentParser(description="Send file content via email.")
b1.add_argument("-f", "--file", b2 = True, help="Path to the file to read content from")
b1.add_argument("-t", "--to", b2 = True, help="Recipient email address")
b1.add_argument("-u", "--smtp-user", b2 = True, help="SMTP username (also used in the 'From' field)")
b1.add_argument("-p", "--smtp-password", b3 = os.environ.get('SMTP_PASSWORD'), help="SMTP password (looks at SMTP_PASSWORD env var first)")
b1.add_argument("-b7", "--smtp-server", b3 = 'smtp.gmail.com:587', help="SMTP server address")
b4 = b1.parse_args()
if not b4.smtp_password:
    exit(b1.print_usage())
with open(b4.file, 'rb') as fp:
    b5 = fp.read()
b6 = MIMEText(b5)
b6['Subject'] = '%b7: %b7 at %b7' % (socket.gethostname(), b4.file, time.asctime())
b6['From'] = b4.smtp_user
b6['To'] = b4.to
b7 = smtplib.SMTP(b4.smtp_server)
b7.ehlo()
b7.starttls()
b7.login(b4.smtp_user, b4.smtp_password)
b7.sendmail(b4.smtp_user, [b4.to], b6.as_string())
b7.quit()