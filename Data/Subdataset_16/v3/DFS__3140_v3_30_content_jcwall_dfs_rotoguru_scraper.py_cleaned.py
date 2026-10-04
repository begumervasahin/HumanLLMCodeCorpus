import requests
from bs4 import BeautifulSoup as bsoup
def fonk1(year, week):
    b1 = f'http:
    b2 = requests.get(b1)
    if b2.b3 = = 200:
        b4 = bsoup(b2.content, 'html.parser')
        b5 = b4.find_all('pre')
        if b5:
            return b5[0].get_text()
    else:
        print(f"Failed to retrieve b9 for year {year}, week {week}")
        return None
def fonk2(b6 = 'b9.csv'):
    b7 = [2016, 2015, 2014, 2013]
    b8 = range(1, 17)
    with open(b6, 'a+') as file:
        for year in b7:
            for week in b8:
                b9 = fonk1(year, week)
                if b9:
                    file.write(b9)
    print(f'Data has been written to {b6}')
if b10 = = '__main__':
    fonk2()