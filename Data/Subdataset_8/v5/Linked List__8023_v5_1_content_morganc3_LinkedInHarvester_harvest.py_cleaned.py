import json
import sys
import argparse
import re
from urllib.request import build_opener
from unidecode import unidecode
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
credentials = [
    "AAMS", "ACA", "ADPA", "AIF", "AWMA", "CAIA", "CAP", "CDFA", "CEP", "CFA", "CFP", "ChFC", "CIMA", "CLU",
    "CPA", "CMA", "CMM", "CMP", "CDFA", "CPWA", "CRPC", "CRPS", "CTP", "CWS", "Jr.", "MBA", "M.A.", "RICP", "Sr.",
    "WMS"
]
credential_pattern = re.compile(
    r"\s*(?:(?:(?:[\x80-\xff]|\)(?:[Rr]|[Tt][Mm])\()?(?:{})+,?)+|[^,]+,)*\s*([A-Za-z \-\.\'\(\)]+)\s*".format(
        "|".join([re.escape(cred) for cred in credentials[::-1]])
    )
)
def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate email addresses from names of employees of a company on LinkedIn.')
    parser.add_argument('COMPANY', help='Company ID')
    parser.add_argument('DOMAIN', help='Domain to be used in email address')
    parser.add_argument('COOKIE', help='Cookie file', metavar="FILE")
    parser.add_argument("-o", "--output", default='emails.txt', help="Output text file for emails")
    parser.add_argument("-f", action="store_true", dest="abbrevF", default=False, help="Abbreviate first name")
    parser.add_argument("-l", action="store_true", dest="abbrevL", default=False, help="Abbreviate last name")
    parser.add_argument("-s", action="store_true", dest="swap", default=False, help="Switch order of first and last names")
    return parser.parse_args()
def extract_emails(company_id, domain, session_id, csrf_token, abbrevF, abbrevL, swap):
    emails = []
    last_page = False
    curr = 0
    def format_name(fullname):
        normalized_name = unidecode(fullname)
        match = credential_pattern.match(normalized_name[::-1])
        if not match:
            print('Unexpected format for %s' % fullname)
            return ''
        name = match.group(1)[::-1]
        sanitized_name = re.sub(r'(\(.*\)%s|[-\'\.,\\])' % (r'|[A-Z]\.' if (not abbrevF and not abbrevL) else ''), '', name).lower()
        return '.'.join([part for part in sanitized_name.split() if part]) + '@' + domain
    def harvest(curr):
        nonlocal last_page
        url = f"https:
        opener = build_opener()
        opener.addheaders.append(('csrf-token', csrf_token))
        opener.addheaders.append(('Cookie', f"li_at={session_id};JSESSIONID={csrf_token}"))
        opener.addheaders.append(('x-restli-protocol-version', '2.0.0'))
        response = opener.open(url)
        data = json.load(response)
        elements = data["elements"][0]["elements"]
        if len(elements) != 49:
            last_page = True
        for employee in elements:
            mini_profile = employee["image"]["attributes"][0]["miniProfile"]
            fname = mini_profile["firstName"].replace(' ', '')
            lname = mini_profile["lastName"].replace(' ', '')
            if fname:
                if abbrevF:
                    fname = fname[0]
                if abbrevL:
                    lname = lname[0]
                fullname = f"{lname} {fname}" if swap else f"{fname} {lname}"
                email = format_name(fullname)
                if email:
                    emails.append(email)
    while not last_page:
        harvest(curr)
        curr += 49
    return emails
def main():
    args = parse_arguments()
    with open(args.COOKIE, "r") as f:
        session_id = f.readline().strip()
        csrf_token = f.readline().strip()
    emails = extract_emails(args.COMPANY, args.DOMAIN, session_id, csrf_token, args.abbrevF, args.abbrevL, args.swap)
    with open(args.output, "w+") as f:
        for email in emails:
            try:
                f.write(f"{email}\n")
            except Exception as e:
                print(f'Error writing email "{email}" due to strange character')
    print(f"Done! {len(emails)} emails have been written to {args.output}")
if __name__ == "__main__":
    main()