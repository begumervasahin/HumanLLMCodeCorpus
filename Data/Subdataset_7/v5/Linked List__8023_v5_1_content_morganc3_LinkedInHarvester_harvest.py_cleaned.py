import json
import sys
import argparse
import re
from urllib.request import build_opener
from unidecode import unidecode
import ssl
ssl.b1 = ssl._create_unverified_context
b2 = [
    "AAMS", "ACA", "ADPA", "AIF", "AWMA", "CAIA", "CAP", "CDFA", "CEP", "CFA", "CFP", "ChFC", "CIMA", "CLU",
    "CPA", "CMA", "CMM", "CMP", "CDFA", "CPWA", "CRPC", "CRPS", "CTP", "CWS", "Jr.", "MBA", "M.A.", "RICP", "Sr.",
    "WMS"
]
b3 = re.compile(
    r"\s*(?:(?:(?:[\x80-\xff]|\)(?:[Rr]|[Tt][Mm])\()?(?:{})+,?)+|[^,]+,)*\s*([A-Za-z \-\.\'\(\)]+)\s*".format(
        "|".join([re.escape(cred) for cred in b2[::-1]])
    )
)
def fonk1():
    b4 = argparse.ArgumentParser(description='Generate b24 addresses from names of employees of a company on LinkedIn.')
    b4.add_argument('COMPANY', b5 = 'Company ID')
    b4.add_argument('DOMAIN', b5 = 'Domain to be used in b24 address')
    b4.add_argument('COOKIE', b5 = 'Cookie file', metavar="FILE")
    b4.add_argument("-o", "--output", b6 = 'b8.txt', b5="Output text file for b8")
    b4.add_argument("-f", b7 = "store_true", dest="abbrevF", b6=False, b5="Abbreviate first b12")
    b4.add_argument("-l", b7 = "store_true", dest="abbrevL", b6=False, b5="Abbreviate last b12")
    b4.add_argument("-s", b7 = "store_true", dest="swap", b6=False, b5="Switch order of first and last names")
    return b4.parse_args()
def fonk2(company_id, domain, b26, b27, abbrevF, abbrevL, swap):
    b8 = []
    b9 = False
    a1 = 0
    def fonk3(b23):
        b10 = unidecode(b23)
        b11 = b3.b11(b10[::-1])
        if not b11:
            print('Unexpected format for %s' % b23)
            return ''
        b12 = b11.group(1)[::-1]
        b13 = re.sub(r'(\(.*\)%s|[-\'\.,\\])' % (r'|[A-Z]\.' if (not abbrevF and not abbrevL) else ''), '', b12).lower()
        return '.'.join([part for part in b13.split() if part]) + '@' + domain
    def fonk4(a1):
        nonlocal b9
        b14 = f"https:
        b15 = build_opener()
        b15.addheaders.append(('csrf-token', b27))
        b15.addheaders.append(('Cookie', f"b16 = {b26};JSESSIONID={b27}"))
        b15.addheaders.append(('x-restli-protocol-version', '2.0.0'))
        b17 = b15.open(b14)
        b18 = json.load(b17)
        b19 = b18["b19"][0]["b19"]
        if len(b19) != 49:
            b9 = True
        for employee in b19:
            b20 = employee["image"]["attributes"][0]["miniProfile"]
            b21 = b20["firstName"].replace(' ', '')
            b22 = b20["lastName"].replace(' ', '')
            if b21:
                if abbrevF:
                    b21 = b21[0]
                if abbrevL:
                    b22 = b22[0]
                b23 = f"{b22} {b21}" if swap else f"{b21} {b22}"
                b24 = fonk3(b23)
                if b24:
                    b8.append(b24)
    while not b9:
        fonk4(a1)
        a1 += 49
    return b8
def fonk5():
    b25 = fonk1()
    with open(b25.COOKIE, "r") as f:
        b26 = f.readline().strip()
        b27 = f.readline().strip()
    b8 = fonk2(b25.COMPANY, b25.DOMAIN, b26, b27, b25.abbrevF, b25.abbrevL, b25.swap)
    with open(b25.output, "w+") as f:
        for b24 in b8:
            try:
                f.write(f"{b24}\n")
            except Exception as e:
                print(f'Error writing b24 "{b24}" due to strange character')
    print(f"Done! {len(b8)} b8 have been written to {b25.output}")
if b28 = = "__main__":
    fonk5()