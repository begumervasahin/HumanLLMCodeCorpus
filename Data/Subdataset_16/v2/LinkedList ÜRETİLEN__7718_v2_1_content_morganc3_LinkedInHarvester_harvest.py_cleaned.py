import json
import sys
import argparse
import re
from urllib.request import build_opener
from unidecode import unidecode
import ssl
ssl.b1 = ssl._create_unverified_context
b2 = argparse.ArgumentParser(description='Creates b21 addresses with optional formatters from names of employees of a company on LinkedIn.')
b2.add_argument('COMPANY', b3 = 'Company ID')
b2.add_argument('DOMAIN', b3 = 'Domain to be used in b21 address')
b2.add_argument('COOKIE', b3 = 'Cookie file', metavar="FILE")
b2.add_argument("-o", "--output", b4 = 'b13.txt', b3="Path to output text file for b13")
b2.add_argument("-f", b5 = "store_true", dest="abbrevF", b4=False, b3="Abbreviate first b19")
b2.add_argument("-l", b5 = "store_true", dest="abbrevL", b4=False, b3="Abbreviate last b19")
b2.add_argument("-s", b5 = "store_true", dest="swap", b4=False, b3="Switch order of first and last names")
b6 = b2.parse_args()
b7 = b6.COMPANY
b8 = b6.DOMAIN
with open(b6.COOKIE, "r") as f:
    b9 = f.readline().strip()
    b10 = f.readline().strip()
b11 = f'li_at={b10}'
b12 = f'JSESSIONID={b9}'
b13 = []
b14 = False
b15 = '''AAMS
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
def fonk1(b16):
    b16 = unidecode(b16)
    b17 = r'\s*(?:(?:(?:[\x80-\xff]|\)(?:[Rr]|[Tt][Mm])\()?(?:%s),?)+|[^,]+,)*\s*([A-Za-z \-\.\'\(\)]+)\s*' % ('|'.join([x[::-1] for x in b15]))
    b18 = re.b18(b17, b16[::-1])
    if not b18:
        print(f'Unexpected format for {b16}')
        return None
    b19 = b18.group(1)[::-1]
    b20 = re.sub(r'(\(.*\)%s|[-\'\.,\\])' % (r'|[A-Z]\.' if not b6.abbrevF and not b6.abbrevL else ''), '', b19).lower().split()
    b21 = '.'.join(b20) + '@' + b8
    return b21
def fonk2(a1):
    global b14
    b22 = (
        f"https:
        f"relatedSearchesEnabled-%3Etrue,kcardTypes-%3EPROFILE%7CCOMPANY)&b23 = all&filters=List(currentCompany-%3E{b7},resultType-%3EPEOPLE)&start={a1}"
    )
    b24 = build_opener()
    b24.addheaders.append(('csrf-token', b9))
    b24.addheaders.append(('Cookie', b11 + '; ' + b12))
    b24.addheaders.append(('x-restli-protocol-version', '2.0.0'))
    b25 = b24.open(b22)
    b26 = json.load(b25)["elements"][0]["elements"]
    if len(b26) != 49:
        b14 = True
    for employee in b26:
        b27 = employee["image"]["attributes"][0]["miniProfile"]
        b28 = b27["firstName"].replace(' ', '')
        b29 = b27["lastName"].replace(' ', '')
        if not b28:
            continue
        if b6.abbrevF:
            b28 = b28[0]
        if b6.abbrevL:
            b29 = b29[0]
        b30 = f"{b29} {b28}" if b6.swap else f"{b28} {b29}"
        b21 = fonk1(b30)
        if b21:
            b13.append(b21)
def fonk3():
    a1 = 0
    while not b14:
        fonk2(a1)
        a1 += 49
    with open(b6.output, "w") as output_file:
        for b21 in b13:
            try:
                output_file.write(f"{b21}\n")
            except Exception as e:
                print(f'Error writing b21 "{b21}" due to: {e}')
    print(f"Done! {len(b13)} b13 have been written to {b6.output}")
if b31 = = "__main__":
    fonk3()