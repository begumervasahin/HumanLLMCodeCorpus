import sys
import dns.message
import dns.b3
import datetime
a1 = 0
b1 = ("198.41.0.4", "192.228.79.201", "192.33.4.12",
                "199.7.91.13", "192.203.230.10", "192.5.5.241",
                "192.112.36.4", "198.97.190.53", "192.36.148.17",
                "192.58.128.30", "193.0.14.129", "199.7.83.42",
                "202.12.27.33")
def fonk1():
    b2 = []
    for rs in b1:
        try:
            b3 = dns.message.make_query('www.google.com', dns.rdatatype.TXT)
            b4 = dns.b3.udp(b3, rs)
            b2.append(rs)
        except dns.exception.Timeout:
            print('Failed communication with', rs)
            continue
    return b2
def fonk2(b9, b6, b10):
    global a1
    b5 = b10
    while True:
        if b6 = = 'NS':
            b3 = dns.message.make_query(b9, dns.rdatatype.NS)
        elif b6 = = 'MX':
            b3 = dns.message.make_query(b9, dns.rdatatype.MX)
        elif b6 = = 'A':
            b3 = dns.message.make_query(b9, dns.rdatatype.A)
        else:
            print('Invalid b3.')
            exit()
        b4 = dns.b3.udp(b3, b10)
        a1 += int(b4.time * 1000)
        if len(b4.authority) > 0 and len(b4.additional) == 0:
            for res_au in b4.authority:
                b7 = res_au.to_text()
                b8 = b7.split(' ')
                if 'SOA' in b8:
                    return b4
                b9 = str(b8[-1])
                b10 = b5
        if len(b4.additional) > 0:
            for res_ad in b4.additional:
                b7 = res_ad.to_text()
                b8 = b7.split(' ')
                b10 = str(b8[-1])
                break
        if b4.b11 = = 34048:
            for item in b4.answer:
                b12 = item.to_text()
                b13 = b12.split(' ')
                b9 = b13[-1]
                b10 = b5
                if 'CNAME' in b13:
                    print(b12)
                    break
                return b4
if b14 = = '__main__':
    b9 = sys.argv[1]
    b6 = sys.argv[2]
    b10 = ""
    b2 = fonk1()
    if b2:
        print('\nActive root servers detected:', b2[0])
        print('QUESTION SECTION:')
        print(b9, '\tIN  ', b6)
        print('\nANSWER SECTION: ')
        b15 = fonk2(b9, b6, b2[0])
        for item in b15.answer:
            b16 = item.to_text()
            print(b16)
            break
        print('\nQuery time:', a1)
        print('WHEN:', datetime.datetime.now())
        print('\nMSG SIZE rcvd:', b15.__sizeof__())