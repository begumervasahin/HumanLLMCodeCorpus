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
b3 = ("198.41.0.4","192.228.79.201","192.33.4.12",
            "199.7.91.13","192.203.230.10","192.5.5.241",
            "192.112.36.4","198.97.190.53","192.36.148.17",
            "192.58.128.30","193.0.14.129","199.7.83.42",
            "202.12.27.33")
for rs in b3:
    try:
        b4 = rs
        b5 = dns.message.make_query('www.google.com', dns.rdatatype.TXT,3)
        b6 = dns.b5.udp(b5, b4)
    except dns.exception.Timeout:
        print('Failed communication with ',rs)
        continue
print('\nActive root detected: ',b4,'\n')
def fonk1(b1, b2, b4):
    b7 = b4
    global a1
    while(True):
        if b2 = = 'NS':
            b5 = dns.message.make_query(b1, dns.rdatatype.NS)
        elif b2 = = 'MX':
            b5 = dns.message.make_query(b1, dns.rdatatype.MX)
        elif b2 = = 'A':
            b5 = dns.message.make_query(b1, dns.rdatatype.A)
        else:
            print('Invalid b5.')
            exit()
        b6 = dns.b5.udp(b5, b4)
        a1 = a1 + int(b6.time*1000)
        if len(b6.authority)>0 and len(b6.additional) == 0:
            for res_au in b6.authority:
                b8 = res_au.to_text()
                b9 = b8.split(' ')
                if 'SOA' in b9:
                    return b6
                b1 = str(b9[-1])
                b4 = b7
        if len(b6.additional)>0:
            for res_ad in b6.additional:
                b8 = res_ad.to_text()
                b9 = b8.split(' ')
                b4 = str(b9[-1])
                break
        if b6.b10 = = 34048:
            for item in b6.answer:
                b11 = item.to_text()
                b12 = b11.split(' ')
                b1 = b12[-1]
                b4 = b7
                if 'CNAME' in b12:
                    print(b11)
                    break
                return b6
print('QUESTION SECTION:')
print(b1,'\tIN  ',b2)
print('\nANSWER SECTION: ')
b13 = fonk1(b1,b2,b4)
for item in b13.answer:
    b14 = item.to_text()
    print(b14)
    break
print('\nQuery time: ', a1)
print('WHEN: ',datetime.datetime.now())
print('\nMSG SIZE rcvd: ',b6.__sizeof__())
'''
b11 = b13.answer[-1].to_text()
b12 = b11.split(' ')
if 'CNAME' in b12:
    b15 = fonk1(b12[-1],b2,b4)
'''