import imaplib
M = imaplib.IMAP4_SSL('imap.gmail.com')
try:
    M.login('youremail@example.com', 'yourpassword')
    print("Logged in")
except imaplib.IMAP4.error:
    print("Login failed")
M.select("INBOX")
listy = []
listdates = []
typ, dataraw = M.search(None, '(FROM "congratulations@redbubble.com")')
for num in dataraw[0].split():
    M.store(num, '+X-GM-LABELS', 'yourdestinationfolder')
    M.store(num, '+FLAGS', '\\Deleted')
    typ, data = M.fetch(num, '(BODY.PEEK[HEADER.FIELDS (SUBJECT)])')
    subject = str(data[-1])
    if "=28=C2=A3" in subject:
        data = subject.split('=28=C2=A3')[-1].split('=')[0]
    elif "=28=E2=82=AC" in subject:
        data = float(subject.split('=28=E2=82=AC')[-1].split('=')[0]) * 0.88
    else:
        data = float(subject.split('(US$')[-1].split(')')[0]) * 0.77
    listy.append(round(float(data), 2))
    typ, dates = M.fetch(num, '(BODY[HEADER.FIELDS (RECEIVED DATE)])')
    received_date = str(dates[-1])
    date_parts = received_date.split(' ')
    formatted_date = date_parts[8] + ' ' + date_parts[9] + ' ' + date_parts[10]
    formatted_date = formatted_date.replace('\\r\\n', '')
    listdates.append(formatted_date)
for i in reversed(range(len(listdates) - 1)):
    if listdates[i] == listdates[i + 1]:
        listy[i] = str(round(float(listy[i]) + float(listy[i + 1]), 2))
        listy[i + 1] = str(0)
listy = [amount for amount in listy if amount != "0" and amount != "0.0"]
listdates = [date for i, date in enumerate(listdates) if listy[i] != "0" and listy[i] != "0.0"]
for i in range(len(listdates)):
    print(f"{listdates[i]}: £{listy[i]}")
M.expunge()
M.close()
M.logout()