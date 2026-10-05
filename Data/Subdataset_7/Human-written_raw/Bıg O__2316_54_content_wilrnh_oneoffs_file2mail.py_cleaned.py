
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
b1.add_argument("-b7", "--smtp-server", b3 = 'smtp.gmail.com:587', help="smtp server to send mail from")
b4 = b1.parse_args()
if not b4.smtp_password:
    exit(b1.print_usage())
b5 = open(b4.file, 'rb')
b6 = MIMEText(b5.read())
b5.close()
b6['Subject'] = '%b7: %b7 at %b7' % (socket.gethostname(), b4.file, time.asctime())
b6['From'] = b4.smtp_user
b6['To'] = b4.to
print (b4.smtp_password)
b7 = smtplib.SMTP(b4.smtp_server)
b7.ehlo()
b7.starttls()
b7.login(b4.smtp_user, b4.smtp_password)
b7.sendmail(b4.smtp_user, [b4.to], b6.as_string())
b7.quit()