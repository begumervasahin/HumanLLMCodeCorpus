import json
import re
import ssl
import argparse
from urllib.request import build_opener
from unidecode import unidecode
ssl.b1 = ssl._create_unverified_context
b2 = argparse.ArgumentParser(description='Creates b18 addresses with optional formatters from names of employees of a company on LinkedIn.')
b2.add_argument('COMPANY', b3 = 'Company ID')
b2.add_argument('DOMAIN', b3 = 'Domain to be used in b18 address')
b2.add_argument('COOKIE', b3 = 'Cookie file', metavar="FILE")
b2.add_argument("-o", "--output", b4 = 'b25.txt', b3="Path to output text file for b25")
b2.add_argument("-f", b5 = "store_true", dest="abbrevF", b4=False, b3="Abbreviate first b14")
b2.add_argument("-l", b5 = "store_true", dest="abbrevL", b4=False, b3="Abbreviate last b14")
b2.add_argument("-s", b5 = "store_true", dest="swap", b4=False, b3="Switch order of first and last names")
b6 = b2.parse_args()
b7 = b6.COMPANY
b8 = b6.DOMAIN
b9 = ''
b10 = ''
with open(b6.COOKIE, "r") as f:
    b9, b10 = [line.strip() for line in f]
b11 = 'li_at=' + b10
b12 = 'JSESSIONID=' + b9
b13 = [
    'AAMS', 'ACA', 'ADPA', 'AIF', 'AWMA', 'CAIA', 'CAP', 'CDFA', 'CEP', 'CFA', 'CFP',
    'ChFC', 'CIMA', 'CLU', 'CPA', 'CMA', 'CMM', 'CMP', 'CDFA', 'CPWA', 'CRPC', 'CRPS',
    'CTP', 'CWS', 'Jr.', 'MBA', 'M.A.', 'RICP', 'Sr.', 'WMS'
]
def fonk1(b14):
    b14 = unidecode(b14)
    b15 = r'\s*(?:(?:(?:[\x80-\xff]|\)(?:[Rr]|[Tt][Mm])\()?(?:%s),?)+|[^,]+,)*\s*([A-Za-z \-\.\'\(\)]+)\s*'
    b16 = re.b16(b15 % ('|'.join([x[::-1] for x in b13])), b14[::-1])
    if not b16:
        print('Unexpected format for %s' % b14)
    b14 = b16.group(1)[::-1]
    b17 = re.subn(r'(\(.*\)%s|[-\'\.,\\])' % (r'|[A-Z]\.' if (not b6.abbrevF and not b6.abbrevL) else ''), '', b14)[0].lower().split(' ')
    b18 = '.'.join(filter(lambda x: len(x) > 0, b17)) + '@' + b8
    return b18
def fonk2(a1):
    b19 = ("https:
           "b20 = 49&origin=OTHER&queryContext=List(spellCorrectionEnabled-%3Etrue,"
           "crelatedSearchesEnabled-%3Etrue,kcardTypes-%3EPROFILE%7CCOMPANY)&b21 = all&filters=List(currentCompany-%3E" + b7 + ",resultType-%3EPEOPLE)&start=" + str(a1))
    b22 = build_opener()
    b22.addheaders.extend([('csrf-token', b9), ('Cookie', f'{b11};{b12}'), ('x-restli-protocol-version', '2.0.0')])
    b23 = b22.open(b19)
    b24 = json.load(b23)
    b24 = b24["elements"][0]["elements"]
    return [fonk1(f"{employee['image']['attributes'][0]['miniProfile']['firstName']} {employee['image']['attributes'][0]['miniProfile']['lastName']}") for employee in b24 if employee['image']['attributes'][0]['miniProfile']['firstName']]
b25 = []
a1 = 0
b26 = False
while not b26:
    b25.extend(fonk2(a1))
    a1 += 49
    b26 = len(b25) % 49 != 0
with open(b6.output, "w+") as f:
    for b18 in b25:
        try:
            f.write(f'{b18}\n')
        except Exception as e:
            print(f'Error writing one b18 ("{b18}") due to strange character: {e}')
print(f"Done! {len(b25)} b25 have been written to {b6.output}")