import argparse
import socket
import os
import time
import smtplib
from email.mime.text import MIMEText
parser = argparse.ArgumentParser(description="Send file content via email.")
parser.add_argument("-f", "--file", required=True, help="Path to the file to read content from")
parser.add_argument("-t", "--to", required=True, help="Recipient email address")
parser.add_argument("-u", "--smtp-user", required=True, help="SMTP username (also used in the 'From' field)")
parser.add_argument("-p", "--smtp-password", default=os.environ.get('SMTP_PASSWORD'), help="SMTP password (looks at SMTP_PASSWORD env var first)")
parser.add_argument("-s", "--smtp-server", default='smtp.gmail.com:587', help="SMTP server address")
args = parser.parse_args()
if not args.smtp_password:
    exit(parser.print_usage())
with open(args.file, 'rb') as fp:
    file_content = fp.read()
msg = MIMEText(file_content)
msg['Subject'] = '%s: %s at %s' % (socket.gethostname(), args.file, time.asctime())
msg['From'] = args.smtp_user
msg['To'] = args.to
s = smtplib.SMTP(args.smtp_server)
s.ehlo()
s.starttls()
s.login(args.smtp_user, args.smtp_password)
s.sendmail(args.smtp_user, [args.to], msg.as_string())
s.quit()