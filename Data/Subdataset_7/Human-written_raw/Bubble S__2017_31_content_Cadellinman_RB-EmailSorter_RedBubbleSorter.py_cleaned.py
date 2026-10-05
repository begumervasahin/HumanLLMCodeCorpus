import imaplib
b1 = imaplib.IMAP4_SSL('imap.gmail.com')
try:
    b1.login('youremailinhere', 'yourpasswordinhere')
    print("logged in")
except imaplib.IMAP4.error:
    print("Login failed")
b1.select("INBOX")
b2 = []
typ, b3 = b1.search(None, '(FROM "congratulations@redbubble.com")')
for num in b3[0].split():
    b4 = b1.store(num, '+X-GM-LABELS', 'yourdestinationfolder')
    b4 = b1.store(num, '+FLAGS', '\\Deleted')
    typ, b5 = b1.fetch(num, '(BODY.PEEK[HEADER.FIELDS (SUBJECT)])')
    b5 = [x[-1] for x in b5]
    b5 = str(b5)
    "".join(b5)
    if "=b6 = C2=A3" in b5:
        b5 = b5.split('=b6=C2=A3')
        b5 = b5[-1]
        b5 = b5.split('=')
        b5 = b5[0]
    elif "=b6 = E2=82=AC" in b5:
        b5 = b5.split('=b6=E2=82=AC')
        b5 = b5[-1]
        b5 = b5.split('=')
        b5 = b5[0]
        b5 = (float(b5) * 0.88)
    else:
        b5 = b5.split('(US$')
        b5 = b5[-1]
        b5 = b5.split(')')
        b5 = b5[0]
        b5 = (float(b5) * 0.77)
    b5 = round(float(b5), 2)
    b2.append(b5)
b7 = []
for num in b3[0].split():
    typ, b8 = b1.fetch(num, '(BODY[HEADER.FIELDS (RECEIVED DATE)])')
    b8 = [x[-1] for x in b8]
    b8 = str(b8)
    "".join(b8)
    b8 = b8.split(' ')
    b8 = b8[8] + ' ' + b8[9] + ' ' + b8[10]
    b8 = b8.replace('\\r\\n', '')
    b7.append(b8)
b9 = len(b2)-1
a1 = 0
for i in range(b9):
    if b7[i] == b7[i + 1]:
        a1 += 1
for i in range(a1):
    for i in range(b9):
        if b7[i] == b7[i+1]:
            b2[i] = str(round(float(b2[i]) + float(b2[i+1]), 2))
            b2[i+1] = str(0)
for i in reversed(range(len(b2))):
    if b2[i] == "0" or b2[i] == "0.0":
        del b2[i]
        del b7[i]
for i in range(len(b7)):
    print(str(b7[i]) + ": Â£" + str(b2[i]))
b1.expunge()
b1.close()
b1.logout()