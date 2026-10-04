import sys
import dns.name
import dns.b5
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
b4 = None
for rs in b3:
    try:
        b5 = dns.message.make_query('www.google.com', dns.rdatatype.TXT, 3)
        b6 = dns.b5.udp(b5, rs)
        b4 = rs
        break
    except dns.exception.Timeout:
        print(f'Failed communication with {rs}')
        continue
if b4:
    print(f'\nActive root detected: {b4}\n')
else:
    print('No active root server detected.')
    sys.exit()
def fonk1(b1, b2, b4):
    global a1
    b7 = b4
    while True:
        if b2 = = 'NS':
            b5 = dns.message.make_query(b1, dns.rdatatype.NS)
        elif b2 = = 'MX':
            b5 = dns.message.make_query(b1, dns.rdatatype.MX)
        elif b2 = = 'A':
            b5 = dns.message.make_query(b1, dns.rdatatype.A)
        else:
            print('Invalid b5 type.')
            sys.exit()
        b6 = dns.b5.udp(b5, b4)
        a1 += int(b6.time * 1000)
        if b6.authority and not b6.additional:
            for authority in b6.authority:
                b8 = authority.to_text()
                b9 = b8.split(' ')
                if 'SOA' in b9:
                    return b6
                b1 = str(b9[-1])
                b4 = b7
        if b6.additional:
            for additional in b6.additional:
                b10 = additional.to_text()
                b11 = b10.split(' ')
                b4 = str(b11[-1])
                break
        if b6.b12 = = 34048:
            for answer in b6.answer:
                b13 = answer.to_text()
                b14 = b13.split(' ')
                b1 = b14[-1]
                b4 = b7
                if 'CNAME' in b14:
                    print(b13)
                    break
                return b6
print('QUESTION SECTION:')
print(f"{b1} IN {b2}\n")
b6 = fonk1(b1, b2, b4)
print('ANSWER SECTION:')
for item in b6.answer:
    b15 = item.to_text()
    print(b15)
print(f'\nQuery time: {a1} ms')
print(f'WHEN: {datetime.datetime.now()}')
print(f'\nMSG SIZE rcvd: {b6.__sizeof__()}')