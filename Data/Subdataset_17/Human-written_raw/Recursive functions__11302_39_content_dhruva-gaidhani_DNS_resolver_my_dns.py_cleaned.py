import sys
import dns.name
import dns.query
import dns.resolver
import dns.message
import time
import datetime
domain = sys.argv[1]
qtype = sys.argv[2]
tm = 0
ROOT_SERVERS = ("198.41.0.4","192.228.79.201","192.33.4.12",
            "199.7.91.13","192.203.230.10","192.5.5.241",
            "192.112.36.4","198.97.190.53","192.36.148.17",
            "192.58.128.30","193.0.14.129","199.7.83.42",
            "202.12.27.33")
for rs in ROOT_SERVERS:
    try:
        nameserver = rs
        query = dns.message.make_query('www.google.com', dns.rdatatype.TXT,3)
        response = dns.query.udp(query, nameserver)
    except dns.exception.Timeout:
        print('Failed communication with ',rs)
        continue
print('\nActive root detected: ',nameserver,'\n')
def dns_resolve(domain, qtype, nameserver):
    init_ns = nameserver
    global tm
    while(True):
        if qtype == 'NS':
            query = dns.message.make_query(domain, dns.rdatatype.NS)
        elif qtype == 'MX':
            query = dns.message.make_query(domain, dns.rdatatype.MX)
        elif qtype == 'A':
            query = dns.message.make_query(domain, dns.rdatatype.A)
        else:
            print('Invalid query.')
            exit()
        response = dns.query.udp(query, nameserver)
        tm = tm + int(response.time*1000)
        if len(response.authority)>0 and len(response.additional) == 0:
            for res_au in response.authority:
                li = res_au.to_text()
                lu = li.split(' ')
                if 'SOA' in lu:
                    return response
                domain = str(lu[-1])
                nameserver = init_ns
        if len(response.additional)>0:
            for res_ad in response.additional:
                li = res_ad.to_text()
                lu = li.split(' ')
                nameserver = str(lu[-1])
                break
        if response.flags == 34048:
            for item in response.answer:
                check1 = item.to_text()
                check2 = check1.split(' ')
                domain = check2[-1]
                nameserver = init_ns
                if 'CNAME' in check2:
                    print(check1)
                    break
                return response
print('QUESTION SECTION:')
print(domain,'\tIN  ',qtype)
print('\nANSWER SECTION: ')
iter1 = dns_resolve(domain,qtype,nameserver)
for item in iter1.answer:
    result = item.to_text()
    print(result)
    break
print('\nQuery time: ', tm)
print('WHEN: ',datetime.datetime.now())
print('\nMSG SIZE rcvd: ',response.__sizeof__())
'''
check1 = iter1.answer[-1].to_text()
check2 = check1.split(' ')
if 'CNAME' in check2:
    iter2 = dns_resolve(check2[-1],qtype,nameserver)
'''