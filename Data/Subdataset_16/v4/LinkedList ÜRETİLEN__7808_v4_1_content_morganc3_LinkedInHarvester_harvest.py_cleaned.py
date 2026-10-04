import json
import re
import ssl
import argparse
from urllib.request import build_opener
from unidecode import unidecode
ssl.b1 = ssl._create_unverified_context
b2 = argparse.ArgumentParser(description='Creates b18 addresses with optional formatters from names of b25 of a company on LinkedIn.')
b2.add_argument('COMPANY', b3 = 'Company ID')
b2.add_argument('DOMAIN', b3 = 'Domain to be used in b18 address')
b2.add_argument('COOKIE', b3 = 'Cookie file', metavar="FILE")
b2.add_argument('-o', '--output', b4 = 'b31.txt', b3="Path to output text file for b31")
b2.add_argument('-f', b5 = 'store_true', dest='abbrevF', b4=False, b3="Abbreviate first b16")
b2.add_argument('-l', b5 = 'store_true', dest='abbrevL', b4=False, b3="Abbreviate last b16")
b2.add_argument('-s', b5 = 'store_true', dest='swap', b4=False, b3="Switch order of first and last names")
b6 = b2.parse_args()
with open(b6.COOKIE, "r") as f:
    b7 = f.readlines()
    b8 = b7[0].strip()
    b9 = b7[1].strip()
b10 = f'li_at={b9}'
b11 = f'JSESSIONID={b8}'
b12 = '''AAMS
ACA
ADPA
AIF
AWMA
CAIA
CAP
CDFA
CEP
CFA
CFP
ChFC
CIMA
CLU
CPA
CMA
CMM
CMP
CDFA
CPWA
CRPC
CRPS
CTP
CWS
Jr.
MBA
M.A.
RICP
Sr.
WMS'''.split('\n')
def fonk1(b13):
    b13 = unidecode(b13)
    b14 = r'\s*(?:(?:(?:[\x80-\xff]|\)(?:[Rr]|[Tt][Mm])\()?(?:%s),?)+|[^,]+,)*\s*([A-Za-z \-\.\'\(\)]+)\s*' % '|'.join([x[::-1] for x in b12])
    b15 = re.b15(b14, b13[::-1])
    if not b15:
        print(f'Unexpected format for {b13}')
        return None
    b16 = b15.group(1)[::-1]
    b17 = re.subn(r'(\(.*\)%s|[-\'\.,\\])' % (r'|[A-Z]\.' if not (b6.abbrevF or b6.abbrevL) else ''), '', b16)[0].lower().split(' ')
    b18 = '.'.join([part for part in b17 if part]) + '@' + b6.DOMAIN
    return b18
def fonk2(start_index):
    global b26
    b19 = (
        f"https:
        f"b20 = 49&origin=OTHER&queryContext=List(spellCorrectionEnabled-%3Etrue,"
        f"relatedSearchesEnabled-%3Etrue,kcardTypes-%3EPROFILE%7CCOMPANY)&b21 = all&filters=List(currentCompany-%3E{b6.COMPANY},resultType-%3EPEOPLE)&start={start_index}"
    )
    b22 = build_opener()
    b22.addheaders.append(('csrf-token', b8))
    b22.addheaders.append(('Cookie', f'{b10}; {b11}'))
    b22.addheaders.append(('x-restli-protocol-version', '2.0.0'))
    b23 = b22.open(b19)
    b24 = json.load(b23)
    b25 = b24["elements"][0]["elements"]
    if len(b25) < 49:
        b26 = True
    for employee in b25:
        b27 = employee["image"]["attributes"][0]["miniProfile"]
        b28 = b27["firstName"].replace(' ', '')
        b29 = b27["lastName"].replace(' ', '')
        if not b28:
            continue
        if b6.abbrevF:
            b28 = b28[0]
        if b6.abbrevL:
            b29 = b29[0]
        if b6.swap:
            b30 = f'{b29} {b28}'
        else:
            b30 = f'{b28} {b29}'
        b18 = fonk1(b30)
        if b18:
            b31.append(b18)
b31 = []
b26 = False
a1 = 0
while not b26:
    fonk2(a1)
    a1 += 49
with open(b6.output, "w") as f:
    for b18 in b31:
        try:
            f.write(f'{b18}\n')
        except Exception as e:
            print(f'Error writing b18 "{b18}" due to: {e}')
print(f"Done! {len(b31)} b31 have been written to {b6.output}")