import imaplib
import email
from email.header import decode_header
EMAIL = 'youremailinhere'
PASSWORD = 'yourpasswordinhere'
IMAP_SERVER = 'imap.gmail.com'
def login_to_email():
    M = imaplib.IMAP4_SSL(IMAP_SERVER)
    try:
        M.login(EMAIL, PASSWORD)
        print("Logged in")
    except imaplib.IMAP4.error:
        print("Login failed")
        return None
    return M
def search_emails(M, sender):
    M.select("INBOX")
    typ, data = M.search(None, f'(FROM "{sender}")')
    return data[0].split()
def process_email_body(data):
    data = str(data)
    if "=28=C2=A3" in data:
        amount = data.split('=28=C2=A3')[-1].split('=')[0]
    elif "=28=E2=82=AC" in data:
        amount = data.split('=28=E2=82=AC')[-1].split('=')[0]
        amount = float(amount) * 0.88
    else:
        amount = data.split('(US$')[-1].split(')')[0]
        amount = float(amount) * 0.77
    return round(float(amount), 2)
def fetch_email_subject(M, num):
    typ, data = M.fetch(num, '(BODY.PEEK[HEADER.FIELDS (SUBJECT)])')
    return [x[-1] for x in data]
def fetch_email_date(M, num):
    typ, data = M.fetch(num, '(BODY.PEEK[HEADER.FIELDS (DATE)])')
    msg = email.message_from_bytes(data[0][1])
    date_tuple = email.utils.parsedate_tz(msg["Date"])
    return email.utils.formatdate(email.utils.mktime_tz(date_tuple), localtime=True)
def label_and_delete_email(M, num, label):
    M.store(num, '+X-GM-LABELS', label)
    M.store(num, '+FLAGS', '\\Deleted')
def main():
    M = login_to_email()
    if M is None:
        return
    sender = "congratulations@redbubble.com"
    email_numbers = search_emails(M, sender)
    amounts = []
    dates = []
    for num in email_numbers:
        subject_data = fetch_email_subject(M, num)
        amount = process_email_body(subject_data)
        date = fetch_email_date(M, num)
        amounts.append(amount)
        dates.append(date)
        label_and_delete_email(M, num, "yourdestinationfolder")
    unique_dates = list(set(dates))
    date_amount_dict = {date: 0 for date in unique_dates}
    for i, date in enumerate(dates):
        date_amount_dict[date] += amounts[i]
    for date, amount in date_amount_dict.items():
        print(f"{date}: £{amount:.2f}")
    M.expunge()
    M.close()
    M.logout()
if __name__ == '__main__':
    main()