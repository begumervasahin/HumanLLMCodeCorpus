
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
def read_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        raise Exception(f"Failed to read file: {e}")
def create_email_message(file_content, smtp_user, recipient):
    msg = MIMEText(file_content)
    msg['Subject'] = f'{socket.gethostname()}: {os.path.basename(file_content)} at {time.asctime()}'
    msg['From'] = smtp_user
    msg['To'] = recipient
    return msg
def send_email(smtp_server, smtp_user, smtp_password, recipient, msg):
    try:
        with smtplib.SMTP(smtp_server) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, [recipient], msg.as_string())
            print(f"Email successfully sent to {recipient}")
    except Exception as e:
        raise Exception(f"Failed to send email: {e}")
def main():
    args = parse_arguments()
    if not args.smtp_password:
        print("SMTP password is required.")
        sys.exit(1)
    try:
        file_content = read_file_content(args.file)
    except Exception as e:
        print(e)
        sys.exit(1)
    msg = create_email_message(file_content, args.smtp_user, args.to)
    try:
        send_email(args.smtp_server, args.smtp_user, args.smtp_password, args.to, msg)
    except Exception as e:
        print(e)
        sys.exit(1)
if __name__ == "__main__":
    main()