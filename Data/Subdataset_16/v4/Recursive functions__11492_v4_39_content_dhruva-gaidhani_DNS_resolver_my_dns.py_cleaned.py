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
for root_server in b3:
    try:
        b5 = dns.message.make_query('www.google.com', dns.rdatatype.TXT, 3)
        b6 = dns.b5.udp(b5, root_server)
        b4 = root_server
        break
    except dns.exception.Timeout:
        print('Failed communication with', root_server)
if b4:
    print('\nActive root detected:', b4, '\n')
else:
    print('No active root server found.')
    sys.exit(1)
def fonk1(b1, b2, b10):
    global a1
    b7 = b10
    while True:
        if b2 = = 'NS':
            b5 = dns.message.make_query(b1, dns.rdatatype.NS)
        elif b2 = = 'MX':
            b5 = dns.message.make_query(b1, dns.rdatatype.MX)
        elif b2 = = 'A':
            b5 = dns.message.make_query(b1, dns.rdatatype.A)
        else:
            print('Invalid b5 type.')
            sys.exit(1)
        b6 = dns.b5.udp(b5, b10)
        a1 += int(b6.time * 1000)
        if b6.authority and not b6.additional:
            for authority in b6.authority:
                b8 = authority.to_text()
                b9 = b8.split(' ')
                if 'SOA' in b9:
                    return b6
                b1 = b9[-1]
                b10 = b7
        if b6.additional:
            for additional in b6.additional:
                b11 = additional.to_text()
                b12 = b11.split(' ')
                b10 = b12[-1]
                break
        if b6.b13 = = 34048:
            for answer in b6.answer:
                b14 = answer.to_text()
                b15 = b14.split(' ')
                if 'CNAME' in b15:
                    print(b14)
                    break
                return b6
print('QUESTION SECTION:')
print(f'{b1}\tIN  {b2}')
print('\nANSWER SECTION: ')
b6 = fonk1(b1, b2, b4)
for answer in b6.answer:
    print(answer.to_text())
    break
print('\nQuery time:', a1, 'ms')
print('WHEN:', datetime.datetime.now())
print('\nMSG SIZE rcvd:', b6.__sizeof__())