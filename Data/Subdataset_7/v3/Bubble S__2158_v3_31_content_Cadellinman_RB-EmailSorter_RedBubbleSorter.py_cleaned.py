import imaplib
b1 = imaplib.IMAP4_SSL('imap.gmail.com')
b2 = 'youremail@example.com'
b3 = 'yourpassword'
b4 = 'yourdestinationfolder'
try:
    b1.login(b2, b3)
    print("Logged in successfully")
except imaplib.IMAP4.error:
    print("Failed to log in")
b1.select("INBOX")
b5 = []
b6 = []
status, b7 = b1.search(None, '(FROM "congratulations@redbubble.com")')
for email_id in b7[0].split():
    b1.store(email_id, '+X-GM-LABELS', b4)
    b1.store(email_id, '+FLAGS', '\\Deleted')
    status, b8 = b1.fetch(email_id, '(BODY.PEEK[HEADER.FIELDS (SUBJECT)])')
    b9 = str(b8[-1])
    if "=b10 = C2=A3" in b9:
        b11 = b9.split('=b10=C2=A3')[-1].split('=')[0]
    elif "=b10 = E2=82=AC" in b9:
        b11 = float(b9.split('=b10=E2=82=AC')[-1].split('=')[0]) * 0.88
    else:
        b11 = float(b9.split('(US$')[-1].split(')')[0]) * 0.77
    b5.append(round(float(b11), 2))
    status, b12 = b1.fetch(email_id, '(BODY[HEADER.FIELDS (RECEIVED DATE)])')
    b13 = str(b12[-1])
    b14 = b13.split(' ')
    b15 = f"{b14[8]} {b14[9]} {b14[10]}".replace('\\r\\n', '')
    b6.append(b15)
for i in reversed(range(len(b6) - 1)):
    if b6[i] == b6[i + 1]:
        b5[i] = str(round(float(b5[i]) + float(b5[i + 1]), 2))
        b5[i + 1] = str(0)
b5 = [amount for amount in b5 if amount != "0" and amount != "0.0"]
b6 = [date for i, date in enumerate(b6) if b5[i] != "0" and b5[i] != "0.0"]
for i in range(len(b6)):
    print(f"{b6[i]}: £{b5[i]}")
b1.expunge()
b1.close()
b1.logout()