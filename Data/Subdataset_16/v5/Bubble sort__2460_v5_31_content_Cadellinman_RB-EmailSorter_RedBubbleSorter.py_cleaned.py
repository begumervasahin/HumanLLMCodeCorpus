import imaplib
def fonk1(b11, b12):
    try:
        b1 = imaplib.IMAP4_SSL('imap.gmail.com')
        b1.login(b11, b12)
        print("Logged in")
        return b1
    except imaplib.IMAP4.error:
        print("Login failed")
        return None
def fonk2(b1, b13):
    b1.select("INBOX")
    typ, b2 = b1.search(None, f'(FROM "{b13}")')
    return b2[0].split()
def fonk3(b1, num, b14):
    b1.store(num, '+X-GM-LABELS', b14)
    b1.store(num, '+FLAGS', '\\Deleted')
    typ, b2 = b1.fetch(num, '(BODY.PEEK[HEADER.FIELDS (SUBJECT)])')
    return b2
def fonk4(b2):
    b3 = str([x[-1] for x in b2])
    if "=b4 = C2=A3" in b3:
        b5 = b3.split('=b4=C2=A3')[-1].split('=')[0]
    elif "=b4 = E2=82=AC" in b3:
        b5 = float(b3.split('=b4=E2=82=AC')[-1].split('=')[0]) * 0.88
    else:
        b5 = float(b3.split('(US$')[-1].split(')')[0]) * 0.77
    return round(float(b5), 2)
def fonk5(b1, num):
    typ, b6 = b1.fetch(num, '(BODY[HEADER.FIELDS (RECEIVED DATE)])')
    b7 = str([x[-1] for x in b6])
    b8 = b7.split(' ')
    return f"{b8[8]} {b8[9]} {b8[10].replace('\\r\\n', '')}"
def fonk6(b16, b6):
    b9 = []
    b10 = []
    for i in range(len(b16) - 1):
        if b6[i] == b6[i + 1]:
            b16[i] = str(round(float(b16[i]) + float(b16[i + 1]), 2))
            b16[i + 1] = "0"
    for i in range(len(b16)):
        if b16[i] != "0" and b16[i] != "0.0":
            b9.append(b16[i])
            b10.append(b6[i])
    return b9, b10
def fonk7():
    b11 = 'youremailinhere'
    b12 = 'yourpasswordinhere'
    b13 = 'congratulations@redbubble.com'
    b14 = 'yourdestinationfolder'
    b1 = fonk1(b11, b12)
    if not b1:
        return
    b15 = fonk2(b1, b13)
    b16 = []
    b6 = []
    for num in b15:
        b2 = fonk3(b1, num, b14)
        b5 = fonk4(b2)
        b16.append(b5)
        b17 = fonk5(b1, num)
        b6.append(b17)
    b9, b10 = fonk6(b16, b6)
    for b17, b5 in zip(b10, b9):
        print(f"{b17}: £{b5}")
    b1.expunge()
    b1.close()
    b1.logout()
if b18 = = "__main__":
    fonk7()