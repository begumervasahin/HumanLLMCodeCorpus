import argparse
import os
import socket
import smtplib
import time
from email.mime.text import MIMEText
parser = argparse.ArgumentParser(description=)
parser.add_argument("-f", "--file", required=True, help="File to read content from.")
parser.add_argument("-t", "--to", required=True, help="Email address to send file content to.")
parser.add_argument("-u", "--smtp-user", required=True, help="Username used to login to SMTP server. Also the email used in the From: field.")
parser.add_argument("-p", "--smtp-password", default=os.environ.get('SMTP_PASSWORD'), help="Password used to login to SMTP server. Looks at SMTP_PASSWORD environment variable first. REQUIRED.")
parser.add_argument("-s", "--smtp-server", default='smtp.gmail.com:587', help="SMTP server to send mail from.")
args = parser.parse_args()
if not args.smtp_password:
    exit(parser.print_usage())
with open(args.file, 'rb') as fp:
    msg = MIMEText(fp.read())
msg['Subject'] = '%s: %s at %s' % (socket.gethostname(), args.file, time.asctime())
msg['From'] = args.smtp_user
msg['To'] = args.to
smtp_server = smtplib.SMTP(args.smtp_server)
smtp_server.ehlo()
smtp_server.starttls()
smtp_server.login(args.smtp_user, args.smtp_password)
smtp_server.sendmail(args.smtp_user, [args.to], msg.as_string())
smtp_server.quit()