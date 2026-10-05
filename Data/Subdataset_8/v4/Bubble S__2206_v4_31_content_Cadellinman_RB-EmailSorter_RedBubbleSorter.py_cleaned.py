import imaplib
M = imaplib.IMAP4_SSL('imap.gmail.com')
try:
    M.login('youremailinhere', 'yourpasswordinhere')
    print("Logged in successfully")
except imaplib.IMAP4.error:
    print("Login failed")
M.select("INBOX")
list_dates = []
list_amounts = []
typ, data_raw = M.search(None, '(FROM "congratulations@redbubble.com")')
for num in data_raw[0].split():
    M.store(num, '+X-GM-LABELS', 'yourdestinationfolder')
    M.store(num, '+FLAGS', '\\Deleted')
    typ, data = M.fetch(num, '(BODY.PEEK[HEADER.FIELDS (SUBJECT)])')
    subject_data = data[-1][0].decode('utf-8')
    if "=28=C2=A3" in subject_data:
        data = subject_data.split('=28=C2=A3')[-1].split('=')[0]
    elif "=28=E2=82=AC" in subject_data:
        data = float(subject_data.split('=28=E2=82=AC')[-1].split('=')[0]) * 0.88
    else:
        data = float(subject_data.split('(US$')[-1].split(')')[0]) * 0.77
    list_amounts.append(round(float(data), 2))
    typ, dates = M.fetch(num, '(BODY[HEADER.FIELDS (RECEIVED DATE)])')
    received_date = dates[-1][0].decode('utf-8').split(' ')[8:11]
    received_date = ' '.join(received_date).replace('\\r\\n', '')
    list_dates.append(received_date)
for i in range(len(list_dates) - 1):
    if list_dates[i] == list_dates[i + 1]:
        list_amounts[i] = str(round(float(list_amounts[i]) + float(list_amounts[i + 1]), 2))
        list_amounts[i + 1] = str(0)
list_dates = [d for d, a in zip(list_dates, list_amounts) if a != "0" and a != "0.0"]
list_amounts = [a for a in list_amounts if a != "0" and a != "0.0"]
for date, amount in zip(list_dates, list_amounts):
    print(f"{date}: £{amount}")
M.expunge()
M.close()
M.logout()