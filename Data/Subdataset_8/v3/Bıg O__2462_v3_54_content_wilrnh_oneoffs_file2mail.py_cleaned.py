import argparse
import os
import smtplib
import socket
import time
from email.mime.text import MIMEText
def parse_arguments():
    parser = argparse.ArgumentParser(description="Send file content via email.")
    parser.add_argument("-f", "--file", required=True, help="Path to the file to read content from")
    parser.add_argument("-t", "--to", required=True, help="Recipient email address")
    parser.add_argument("-u", "--smtp-user", required=True, help="SMTP username (also used in the 'From' field)")
    parser.add_argument("-p", "--smtp-password", default=os.environ.get('SMTP_PASSWORD'), help="SMTP password (looks at SMTP_PASSWORD env var first)")
    parser.add_argument("-s", "--smtp-server", default='smtp.gmail.com:587', help="SMTP server address")
    return parser.parse_args()
def read_file_content(file_path):
    with open(file_path, 'rb') as fp:
        file_content = fp.read()
    return file_content
def create_mime_message(file_content, hostname, file_path):
    msg = MIMEText(file_content)
    msg['Subject'] = '%s: %s at %s' % (hostname, file_path, time.asctime())
    return msg
def send_email(smtp_user, smtp_password, smtp_server, recipient, msg):
    try:
        s = smtplib.SMTP(smtp_server)
        s.ehlo()
        s.starttls()
        s.login(smtp_user, smtp_password)
        s.sendmail(smtp_user, [recipient], msg.as_string())
        s.quit()
        print("Email sent successfully.")
    except Exception as e:
        print("Failed to send email:", e)
def main():
    args = parse_arguments()
    if not args.smtp_password:
        exit("SMTP password not provided. Please provide a password using the '-p' or '--smtp-password' option.")
    file_content = read_file_content(args.file)
    msg = create_mime_message(file_content, socket.gethostname(), args.file)
    send_email(args.smtp_user, args.smtp_password, args.smtp_server, args.to, msg)
if __name__ == "__main__":
    main()