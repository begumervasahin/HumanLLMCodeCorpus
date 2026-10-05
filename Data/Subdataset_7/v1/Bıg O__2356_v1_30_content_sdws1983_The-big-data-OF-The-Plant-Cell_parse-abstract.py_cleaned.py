from bs4 import BeautifulSoup
import requests
import re
def fonk1(b11):
    b1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Host': 'www.plantcell.org'
    }
    b2 = requests.get(b11, b1=b1)
    b2.raise_for_status()
    return b2.text
def fonk2(b12):
    b3 = BeautifulSoup(b12, 'b12.parser')
    b4 = []
    b5 = []
    b6 = []
    for i in b3.find_all('p', b7 = re.compile(r'p-\d+')):
        b8 = i.get_text(strip=True)
        if len(b8) > 250:
            b4.append(b8)
    a1 = 1
    for each in b3.find_all('li'):
        try:
            if 'last' in each['class'] and 'name' in str(each):
                b9 = each.find('a').string
                b5.append(b9)
            elif 'aff' in each['class']:
                b10 = each.find('b10').get_text(strip=True)
                if b10 and b10[0].isalpha():
                    b10 = b10[1:]
                b6.append(f"{a1}\t{b10}")
                a1 += 1
        except Exception as e:
            pass
    if len(b4) > 2:
        print("Content error")
        b4 = []
        b5 = []
        b6 = []
    return '\n'.join(b4), '\n'.join(b5), '\n'.join(b6)
def fonk3(vol, page):
    b11 = f"http:
    b12 = fonk1(b11)
    b8, b9, b10 = fonk2(b12)
    with open(f"{vol}-b8.csv", 'a') as f1, \
            open(f"{vol}-b9.csv", 'a') as f2, \
            open(f"{vol}-b10.csv", 'a') as f3:
        if b8 and b8[-1] != "\n":
            b8 += "\n"
        if b9 and b9[-1] != "\n":
            b9 += "\n"
        if b10 and b10[-1] != "\n":
            b10 += "\n"
        f1.write(f">{page}\n{b8}")
        f2.write(f">{page}\n{b9}")
        f3.write(f">{page}\n{b10}")
if b13 = = "__main__":
    for iss in range(1, 12):
        b14 = get_issues(iss)
        print(f"vol: {iss}")
        for page in b14:
            print(page)
            try:
                fonk3(iss, page)
            except Exception as e:
                print(e)