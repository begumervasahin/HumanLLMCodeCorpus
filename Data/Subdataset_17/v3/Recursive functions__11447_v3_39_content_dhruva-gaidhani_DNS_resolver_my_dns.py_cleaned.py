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
def find_active_root_server():
    for rs in ROOT_SERVERS:
        try:
            query = dns.message.make_query('www.google.com', dns.rdatatype.TXT, 3)
            response = dns.query.udp(query, rs)
            return rs
        except dns.exception.Timeout:
            print(f'Failed communication with {rs}')
            continue
    return None
def prepare_query(domain, qtype):
    if qtype == 'NS':
        return dns.message.make_query(domain, dns.rdatatype.NS)
    elif qtype == 'MX':
        return dns.message.make_query(domain, dns.rdatatype.MX)
    elif qtype == 'A':
        return dns.message.make_query(domain, dns.rdatatype.A)
    else:
        print('Invalid query type.')
        sys.exit()
def process_response(response, initial_ns):
    global total_query_time
    total_query_time += int(response.time * 1000)
    if response.authority and not response.additional:
        for authority in response.authority:
            authority_text = authority.to_text()
            authority_parts = authority_text.split(' ')
            if 'SOA' in authority_parts:
                return response
            return authority_parts[-1], initial_ns
    if response.additional:
        for additional in response.additional:
            additional_text = additional.to_text()
            additional_parts = additional_text.split(' ')
            return domain, additional_parts[-1]
    if response.flags == 34048:
        for answer in response.answer:
            answer_text = answer.to_text()
            answer_parts = answer_text.split(' ')
            if 'CNAME' in answer_parts:
                print(answer_text)
            return domain, initial_ns
    return domain, initial_ns
def dns_resolve(domain, qtype, nameserver):
    initial_ns = nameserver
    while True:
        query = prepare_query(domain, qtype)
        response = dns.query.udp(query, nameserver)
        domain, nameserver = process_response(response, initial_ns)
        if not domain or not nameserver:
            return response
def main():
    nameserver = find_active_root_server()
    if not nameserver:
        print('No active root server detected.')
        sys.exit()
    print(f'\nActive root detected: {nameserver}\n')
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
if __name__ == "__main__":
    main()