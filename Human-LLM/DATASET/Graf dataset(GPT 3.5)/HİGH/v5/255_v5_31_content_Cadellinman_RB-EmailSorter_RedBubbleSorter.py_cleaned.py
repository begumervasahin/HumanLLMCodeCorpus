import imaplib
b1 = imaplib.IMAP4_SSL('imap.gmail.com')
try:
    b1.login('youremailinhere', 'yourpasswordinhere')
    print("Logged in successfully")
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
    b6 = b5[-1][0].decode('utf-8')
    if "=b7 = C2=A3" in b6:
        b8 = b6.split('=b7=C2=A3')[-1].split('=')[0]
    elif "=b7 = E2=82=AC" in b6:
        b8 = float(b6.split('=b7=E2=82=AC')[-1].split('=')[0]) * 0.88
    else:
        b8 = float(b6.split('(US$')[-1].split(')')[0]) * 0.77
    b3.append(round(float(b8), 2))
    typ, b9 = b1.fetch(num, '(BODY[HEADER.FIELDS (RECEIVED DATE)])')
    b10 = b9[-1][0].decode('utf-8').split(' ')[8:11]
    b10 = ' '.join(b10).replace('\\r\\n', '')
    b2.append(b10)
for i in range(len(b2) - 1):
    if b2[i] == b2[i + 1]:
        b3[i] = str(round(float(b3[i]) + float(b3[i + 1]), 2))
        b3[i + 1] = str(0)
b2 = [d for d, a in zip(b2, b3) if a != "0" and a != "0.0"]
b3 = [a for a in b3 if a != "0" and a != "0.0"]
for date, b8 in zip(b2, b3):
    print(f"{date}: £{b8}")
b1.expunge()
b1.close()
b1.logout()