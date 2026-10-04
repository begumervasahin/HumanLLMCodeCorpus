import sys
import dns.name
import dns.query
import dns.resolver
import dns.message
import time
import datetime
domain = sys.argv[1]
qtype = sys.argv[2]
total_query_time = 0
ROOT_SERVERS = [
    "198.41.0.4", "192.228.79.201", "192.33.4.12", "199.7.91.13",
    "192.203.230.10", "192.5.5.241", "192.112.36.4", "198.97.190.53",
    "192.36.148.17", "192.58.128.30", "193.0.14.129", "199.7.83.42",
    "202.12.27.33"
]
nameserver = None
for rs in ROOT_SERVERS:
    try:
        query = dns.message.make_query('www.google.com', dns.rdatatype.TXT, 3)
        response = dns.query.udp(query, rs)
        nameserver = rs
        break
    except dns.exception.Timeout:
        print(f'Failed communication with {rs}')
        continue
if nameserver:
    print(f'\nActive root detected: {nameserver}\n')
else:
    print('No active root server detected.')
    sys.exit()
def dns_resolve(domain, qtype, nameserver):
    global total_query_time
    initial_ns = nameserver
    while True:
        if qtype == 'NS':
            query = dns.message.make_query(domain, dns.rdatatype.NS)
        elif qtype == 'MX':
            query = dns.message.make_query(domain, dns.rdatatype.MX)
        elif qtype == 'A':
            query = dns.message.make_query(domain, dns.rdatatype.A)
        else:
            print('Invalid query type.')
            sys.exit()
        response = dns.query.udp(query, nameserver)
        total_query_time += int(response.time * 1000)
        if response.authority and not response.additional:
            for authority in response.authority:
                authority_text = authority.to_text()
                authority_parts = authority_text.split(' ')
                if 'SOA' in authority_parts:
                    return response
                domain = str(authority_parts[-1])
                nameserver = initial_ns
        if response.additional:
            for additional in response.additional:
                additional_text = additional.to_text()
                additional_parts = additional_text.split(' ')
                nameserver = str(additional_parts[-1])
                break
        if response.flags == 34048:
            for answer in response.answer:
                answer_text = answer.to_text()
                answer_parts = answer_text.split(' ')
                domain = answer_parts[-1]
                nameserver = initial_ns
                if 'CNAME' in answer_parts:
                    print(answer_text)
                    break
                return response
print('QUESTION SECTION:')
print(f"{domain} IN {qtype}\n")
response = dns_resolve(domain, qtype, nameserver)
print('ANSWER SECTION:')
for item in response.answer:
    result = item.to_text()
    print(result)
print(f'\nQuery time: {total_query_time} ms')
print(f'WHEN: {datetime.datetime.now()}')
print(f'\nMSG SIZE rcvd: {response.__sizeof__()}')