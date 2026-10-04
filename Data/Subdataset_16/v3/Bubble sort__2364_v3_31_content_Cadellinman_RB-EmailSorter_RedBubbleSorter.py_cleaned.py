import imaplib
import email
from email.header import decode_header
b1 = 'youremailinhere'
b2 = 'yourpasswordinhere'
b3 = 'imap.gmail.com'
def fonk1():
    b4 = imaplib.IMAP4_SSL(b3)
    try:
        b4.login(b1, b2)
        print("Logged in successfully")
        return b4
    except imaplib.IMAP4.error:
        print("Login failed")
        return None
def fonk2(b4, b11):
    b4.select("INBOX")
    typ, b5 = b4.search(None, f'(FROM "{b11}")')
    return b5[0].split()
def fonk3(b5):
    b5 = str(b5)
    if "=b6 = C2=A3" in b5:
        b7 = b5.split('=b6=C2=A3')[-1].split('=')[0]
    elif "=b6 = E2=82=AC" in b5:
        b7 = b5.split('=b6=E2=82=AC')[-1].split('=')[0]
        b7 = float(b7) * 0.88
    else:
        b7 = b5.split('(US$')[-1].split(')')[0]
        b7 = float(b7) * 0.77
    return round(float(b7), 2)
def fonk4(b4, num):
    typ, b5 = b4.fetch(num, '(BODY.PEEK[HEADER.FIELDS (SUBJECT)])')
    return [x[-1] for x in b5]
def fonk5(b4, num):
    typ, b5 = b4.fetch(num, '(BODY.PEEK[HEADER.FIELDS (DATE)])')
    b8 = email.message_from_bytes(b5[0][1])
    b9 = email.utils.parsedate_tz(b8["Date"])
    return email.utils.formatdate(email.utils.mktime_tz(b9), b10 = True)
def fonk6(b4, num, label):
    b4.store(num, '+X-GM-LABELS', label)
    b4.store(num, '+FLAGS', '\\Deleted')
def fonk7():
    b4 = fonk1()
    if not b4:
        return
    b11 = "congratulations@redbubble.com"
    b12 = fonk2(b4, b11)
    b13 = []
    b14 = []
    for num in b12:
        b15 = fonk4(b4, num)
        b7 = fonk3(b15)
        b16 = fonk5(b4, num)
        b13.append(b7)
        b14.append(b16)
        fonk6(b4, num, "yourdestinationfolder")
    b17 = list(set(b14))
    b18 = {b16: 0 for b16 in b17}
    for i, b16 in enumerate(b14):
        b18[b16] += b13[i]
    for b16, b7 in b18.items():
        print(f"{b16}: £{b7:.2f}")
    b4.expunge()
    b4.close()
    b4.logout()
if b19 = = '__main__':
    fonk7()