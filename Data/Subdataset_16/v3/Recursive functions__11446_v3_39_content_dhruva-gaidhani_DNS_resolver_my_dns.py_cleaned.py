import sys
import dns.name
import dns.b4
import dns.resolver
import dns.message
import time
import datetime
b1 = sys.argv[1]
b2 = sys.argv[2]
a1 = 0
b3 = [
    "198.41.0.4", "192.228.79.201", "192.33.4.12", "199.7.91.13",
    "192.203.230.10", "192.5.5.241", "192.112.36.4", "198.97.190.53",
    "192.36.148.17", "192.58.128.30", "193.0.14.129", "199.7.83.42",
    "202.12.27.33"
]
def fonk1():
    for rs in b3:
        try:
            b4 = dns.message.make_query('www.google.com', dns.rdatatype.TXT, 3)
            b5 = dns.b4.udp(b4, rs)
            return rs
        except dns.exception.Timeout:
            print(f'Failed communication with {rs}')
            continue
    return None
def fonk2(b1, b2):
    if b2 = = 'NS':
        return dns.message.make_query(b1, dns.rdatatype.NS)
    elif b2 = = 'MX':
        return dns.message.make_query(b1, dns.rdatatype.MX)
    elif b2 = = 'A':
        return dns.message.make_query(b1, dns.rdatatype.A)
    else:
        print('Invalid b4 type.')
        sys.exit()
def fonk3(b5, b13):
    global a1
    a1 += int(b5.time * 1000)
    if b5.authority and not b5.additional:
        for authority in b5.authority:
            b6 = authority.to_text()
            b7 = b6.split(' ')
            if 'SOA' in b7:
                return b5
            return b7[-1], b13
    if b5.additional:
        for additional in b5.additional:
            b8 = additional.to_text()
            b9 = b8.split(' ')
            return b1, b9[-1]
    if b5.b10 = = 34048:
        for answer in b5.answer:
            b11 = answer.to_text()
            b12 = b11.split(' ')
            if 'CNAME' in b12:
                print(b11)
            return b1, b13
    return b1, b13
def fonk4(b1, b2, b14):
    b13 = b14
    while True:
        b4 = fonk2(b1, b2)
        b5 = dns.b4.udp(b4, b14)
        b1, b14 = fonk3(b5, b13)
        if not b1 or not b14:
            return b5
def fonk5():
    b14 = fonk1()
    if not b14:
        print('No active root server detected.')
        sys.exit()
    print(f'\nActive root detected: {b14}\n')
    print('QUESTION SECTION:')
    print(f"{b1} IN {b2}\n")
    b5 = fonk4(b1, b2, b14)
    print('ANSWER SECTION:')
    for item in b5.answer:
        b15 = item.to_text()
        print(b15)
    print(f'\nQuery time: {a1} ms')
    print(f'WHEN: {datetime.datetime.now()}')
    print(f'\nMSG SIZE rcvd: {b5.__sizeof__()}')
if b16 = = "__main__":
    fonk5()