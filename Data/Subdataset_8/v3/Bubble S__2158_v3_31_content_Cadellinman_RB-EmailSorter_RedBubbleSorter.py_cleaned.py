import imaplib
imap_server = imaplib.IMAP4_SSL('imap.gmail.com')
email_address = 'youremail@example.com'
password = 'yourpassword'
destination_folder = 'yourdestinationfolder'
try:
    imap_server.login(email_address, password)
    print("Logged in successfully")
except imaplib.IMAP4.error:
    print("Failed to log in")
imap_server.select("INBOX")
monetary_amounts = []
email_dates = []
status, email_ids = imap_server.search(None, '(FROM "congratulations@redbubble.com")')
for email_id in email_ids[0].split():
    imap_server.store(email_id, '+X-GM-LABELS', destination_folder)
    imap_server.store(email_id, '+FLAGS', '\\Deleted')
    status, email_data = imap_server.fetch(email_id, '(BODY.PEEK[HEADER.FIELDS (SUBJECT)])')
    subject = str(email_data[-1])
    if "=28=C2=A3" in subject:
        monetary_data = subject.split('=28=C2=A3')[-1].split('=')[0]
    elif "=28=E2=82=AC" in subject:
        monetary_data = float(subject.split('=28=E2=82=AC')[-1].split('=')[0]) * 0.88
    else:
        monetary_data = float(subject.split('(US$')[-1].split(')')[0]) * 0.77
    monetary_amounts.append(round(float(monetary_data), 2))
    status, date_data = imap_server.fetch(email_id, '(BODY[HEADER.FIELDS (RECEIVED DATE)])')
    received_date = str(date_data[-1])
    date_parts = received_date.split(' ')
    formatted_date = f"{date_parts[8]} {date_parts[9]} {date_parts[10]}".replace('\\r\\n', '')
    email_dates.append(formatted_date)
for i in reversed(range(len(email_dates) - 1)):
    if email_dates[i] == email_dates[i + 1]:
        monetary_amounts[i] = str(round(float(monetary_amounts[i]) + float(monetary_amounts[i + 1]), 2))
        monetary_amounts[i + 1] = str(0)
monetary_amounts = [amount for amount in monetary_amounts if amount != "0" and amount != "0.0"]
email_dates = [date for i, date in enumerate(email_dates) if monetary_amounts[i] != "0" and monetary_amounts[i] != "0.0"]
for i in range(len(email_dates)):
    print(f"{email_dates[i]}: £{monetary_amounts[i]}")
imap_server.expunge()
imap_server.close()
imap_server.logout()