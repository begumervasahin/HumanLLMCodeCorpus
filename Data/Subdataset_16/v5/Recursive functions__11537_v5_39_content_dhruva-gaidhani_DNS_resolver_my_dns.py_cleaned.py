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
    for root_server in b3:
        try:
            b4 = dns.message.make_query('www.google.com', dns.rdatatype.TXT, 3)
            b5 = dns.b4.udp(b4, root_server)
            return root_server
        except dns.exception.Timeout:
            print(f'Failed communication with {root_server}')
    return None
def fonk2(b1, b2, b9):
    global a1
    b6 = b9
    while True:
        if b2 = = 'NS':
            b4 = dns.message.make_query(b1, dns.rdatatype.NS)
        elif b2 = = 'MX':
            b4 = dns.message.make_query(b1, dns.rdatatype.MX)
        elif b2 = = 'A':
            b4 = dns.message.make_query(b1, dns.rdatatype.A)
        else:
            print('Invalid b4 type.')
            sys.exit(1)
        b5 = dns.b4.udp(b4, b9)
        a1 += int(b5.time * 1000)
        if b5.authority and not b5.additional:
            for authority in b5.authority:
                b7 = authority.to_text()
                b8 = b7.split(' ')
                if 'SOA' in b8:
                    return b5
                b1 = b8[-1]
                b9 = b6
        if b5.additional:
            for additional in b5.additional:
                b10 = additional.to_text()
                b11 = b10.split(' ')
                b9 = b11[-1]
                break
        if b5.b12 = = 34048:
            for answer in b5.answer:
                b13 = answer.to_text()
                b14 = b13.split(' ')
                if 'CNAME' in b14:
                    print(b13)
                    break
                return b5
b15 = fonk1()
if b15:
    print('\nActive root detected:', b15, '\n')
else:
    print('No active root server found.')
    sys.exit(1)
print('QUESTION SECTION:')
print(f'{b1}\tIN  {b2}')
print('\nANSWER SECTION: ')
b5 = fonk2(b1, b2, b15)
for answer in b5.answer:
    print(answer.to_text())
    break
print('\nQuery time:', a1, 'ms')
print('WHEN:', datetime.datetime.now())
print('\nMSG SIZE rcvd:', b5.__sizeof__())