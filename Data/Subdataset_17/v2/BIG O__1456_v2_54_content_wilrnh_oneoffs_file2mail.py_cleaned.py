
import argparse
import socket
import os
import sys
import time
import smtplib
from email.mime.text import MIMEText
def parse_arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-f", "--file", required=True, help="File to read content from")
    parser.add_argument("-t", "--to", required=True, help="Recipient email address")
    parser.add_argument("-u", "--smtp-user", required=True, help="SMTP username (also used as the 'From' email address)")
    parser.add_argument("-p", "--smtp-password", default=os.environ.get('SMTP_PASSWORD'), help="SMTP password (reads from SMTP_PASSWORD env var if not provided)")
    parser.add_argument("-s", "--smtp-server", default='smtp.gmail.com:587', help="SMTP server address (default: smtp.gmail.com:587)")
    return parser.parse_args()
def main():
    args = parse_arguments()
    if not args.smtp_password:
        print("SMTP password is required.")
        sys.exit(1)
    try:
        with open(args.file, 'r') as file:
            file_content = file.read()
    except Exception as e:
        print(f"Failed to read file: {e}")
        sys.exit(1)
    msg = MIMEText(file_content)
    msg['Subject'] = f'{socket.gethostname()}: {args.file} at {time.asctime()}'
    msg['From'] = args.smtp_user
    msg['To'] = args.to
    try:
        with smtplib.SMTP(args.smtp_server) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(args.smtp_user, args.smtp_password)
            server.sendmail(args.smtp_user, [args.to], msg.as_string())
            print(f"Email successfully sent to {args.to}")
    except Exception as e:
        print(f"Failed to send email: {e}")
        sys.exit(1)
if __name__ == "__main__":
    main()