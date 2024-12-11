import imaplib
b1 = imaplib.IMAP4_SSL('imap.gmail.com')
try:
    b1.login('youremail@example.com', 'yourpassword')
    print("Logged in successfully")
except imaplib.IMAP4.error:
    print("Failed to log in")
b1.select("INBOX")
b2 = []
b3 = []
status, b4 = b1.search(None, '(FROM "congratulations@redbubble.com")')
for email_id in b4[0].split():
    b1.store(email_id, '+X-GM-LABELS', 'yourdestinationfolder')
    b1.store(email_id, '+FLAGS', '\\Deleted')
    status, b5 = b1.fetch(email_id, '(BODY.PEEK[HEADER.FIELDS (SUBJECT)])')
    b6 = str(b5[-1])
    if "=b7 = C2=A3" in b6:
        b8 = b6.split('=b7=C2=A3')[-1].split('=')[0]
    elif "=b7 = E2=82=AC" in b6:
        b8 = float(b6.split('=b7=E2=82=AC')[-1].split('=')[0]) * 0.88
    else:
        b8 = float(b6.split('(US$')[-1].split(')')[0]) * 0.77
    b2.append(round(float(b8), 2))
    status, b9 = b1.fetch(email_id, '(BODY[HEADER.FIELDS (RECEIVED DATE)])')
    b10 = str(b9[-1])
    b11 = b10.split(' ')
    b12 = f"{b11[8]} {b11[9]} {b11[10]}".replace('\\r\\n', '')
    b3.append(b12)
for i in reversed(range(len(b3) - 1)):
    if b3[i] == b3[i + 1]:
        b2[i] = str(round(float(b2[i]) + float(b2[i + 1]), 2))
        b2[i + 1] = str(0)
b2 = [amount for amount in b2 if amount != "0" and amount != "0.0"]
b3 = [date for i, date in enumerate(b3) if b2[i] != "0" and b2[i] != "0.0"]
for i in range(len(b3)):
    print(f"{b3[i]}: £{b2[i]}")
b1.expunge()
b1.close()
b1.logout()