import sys
import dns.name
import dns.b5
import dns.resolver
import dns.message
import time
import datetime
b1 = (
    "198.41.0.4", "192.228.79.201", "192.33.4.12",
    "199.7.91.13", "192.203.230.10", "192.5.5.241",
    "192.112.36.4", "198.97.190.53", "192.36.148.17",
    "192.58.128.30", "193.0.14.129", "199.7.83.42",
    "202.12.27.33"
)
b2 = sys.argv[1]
b3 = sys.argv[2]
a1 = 0
b4 = None
for rs in b1:
    try:
        b4 = rs
        b5 = dns.message.make_query('www.google.com', dns.rdatatype.TXT, 3)
        b6 = dns.b5.udp(b5, b4)
    except dns.exception.Timeout:
        print('Failed communication with', rs)
        continue
print('\nActive root detected:', b4, '\n')
def fonk1(b2, b3, b4):
    global a1
    b7 = b4
    while True:
        if b3 not in ['NS', 'MX', 'A']:
            print('Invalid b5.')
            exit()
        if b3 = = 'NS':
            b5 = dns.message.make_query(b2, dns.rdatatype.NS)
        elif b3 = = 'MX':
            b5 = dns.message.make_query(b2, dns.rdatatype.MX)
        else:
            b5 = dns.message.make_query(b2, dns.rdatatype.A)
        b6 = dns.b5.udp(b5, b4)
        a1 += int(b6.time * 1000)
        if len(b6.authority) > 0 and len(b6.additional) == 0:
            for res_au in b6.authority:
                b8 = res_au.to_text()
                b9 = b8.split(' ')
                if 'SOA' in b9:
                    return b6
                b2 = str(b9[-1])
                b4 = b7
        if len(b6.additional) > 0:
            for res_ad in b6.additional:
                b8 = res_ad.to_text()
                b9 = b8.split(' ')
                b4 = str(b9[-1])
                break
        if b6.b10 = = 34048:
            for item in b6.answer:
                b11 = item.to_text()
                b12 = b11.split(' ')
                b2 = b12[-1]
                b4 = b7
                if 'CNAME' in b12:
                    print(b11)
                    break
                return b6
print('QUESTION SECTION:')
print(b2, '\tIN\t', b3)
print('\nANSWER SECTION: ')
b13 = fonk1(b2, b3, b4)
for item in b13.answer:
    b14 = item.to_text()
    print(b14)
    break
print('\nQuery time:', a1)
print('WHEN:', datetime.datetime.now())
print('\nMSG SIZE rcvd:', b6.__sizeof__())