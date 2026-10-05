from bs4 import BeautifulSoup
import requests
import re
def fonk1(b12):
    b1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Host': 'www.plantcell.org'
    }
    b2 = requests.get(b12, b1=b1)
    b2.raise_for_status()
    return b2.text
def fonk2(b10):
    b3 = []
    for paragraph in b10.find_all('p', b4 = re.compile(r'p-\d+')):
        b5 = paragraph.get_text(strip=True)
        if len(b5) > 250:
            b3.append(b5)
    return '\n'.join(b3)
def fonk3(b10):
    b6 = []
    b7 = []
    a1 = 1
    for item in b10.find_all('li'):
        try:
            if 'last' in item['class'] and 'name' in str(item):
                b8 = item.find('a').string
                b6.append(b8)
            elif 'aff' in item['class']:
                b9 = item.find('b9').get_text(strip=True)
                if b9 and b9[0].isalpha():
                    b9 = b9[1:]
                b7.append(f"{a1}\t{b9}")
                a1 += 1
        except Exception as e:
            pass
    return '\n'.join(b6), '\n'.join(b7)
def fonk4(b13):
    b10 = BeautifulSoup(b13, 'b13.parser')
    b3 = fonk2(b10)
    authors, b11 = fonk3(b10)
    if len(b3.split('\n')) > 2:
        print("Content error")
        b3 = authors = b11 = ''
    return b3, authors, b11
def fonk5(vol, page, b3, authors, b11):
    with open(f"{vol}-b5.csv", 'a') as content_file, \
         open(f"{vol}-b8.csv", 'a') as author_file, \
         open(f"{vol}-b9.csv", 'a') as address_file:
        if b3 and b3[-1] != "\n":
            b3 += "\n"
        if authors and authors[-1] != "\n":
            authors += "\n"
        if b11 and b11[-1] != "\n":
            b11 += "\n"
        content_file.write(f">{page}\n{b3}")
        author_file.write(f">{page}\n{authors}")
        address_file.write(f">{page}\n{b11}")
def fonk6(volume):
    for page in get_issues(volume):
        print(f"Volume: {volume}, Page: {page}")
        try:
            b12 = f"http:
            b13 = fonk1(b12)
            b5, authors, b11 = fonk4(b13)
            fonk5(volume, page, b5, authors, b11)
        except Exception as e:
            print(e)
if b14 = = "__main__":
    for vol in range(1, 12):
        fonk6(vol)