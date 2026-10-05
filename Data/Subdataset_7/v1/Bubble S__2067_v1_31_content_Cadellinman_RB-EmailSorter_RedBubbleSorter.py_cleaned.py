import imaplib
b1 = imaplib.IMAP4_SSL('imap.gmail.com')
try:
    b1.login('youremail@example.com', 'yourpassword')
    print("Logged in")
except imaplib.IMAP4.error:
    print("Login failed")
b1.select("INBOX")
b2 = []
b3 = []
typ, b4 = b1.search(None, '(FROM "congratulations@redbubble.com")')
for num in b4[0].split():
    b1.store(num, '+X-GM-LABELS', 'yourdestinationfolder')
    b1.store(num, '+FLAGS', '\\Deleted')
    typ, b5 = b1.fetch(num, '(BODY.PEEK[HEADER.FIELDS (SUBJECT)])')
    b6 = str(b5[-1])
    if "=b7 = C2=A3" in b6:
        b5 = b6.split('=b7=C2=A3')[-1].split('=')[0]
    elif "=b7 = E2=82=AC" in b6:
        b5 = float(b6.split('=b7=E2=82=AC')[-1].split('=')[0]) * 0.88
    else:
        b5 = float(b6.split('(US$')[-1].split(')')[0]) * 0.77
    b2.append(round(float(b5), 2))
    typ, b8 = b1.fetch(num, '(BODY[HEADER.FIELDS (RECEIVED DATE)])')
    b9 = str(b8[-1])
    b10 = b9.split(' ')
    b11 = b10[8] + ' ' + b10[9] + ' ' + b10[10]
    b11 = b11.replace('\\r\\n', '')
    b3.append(b11)
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