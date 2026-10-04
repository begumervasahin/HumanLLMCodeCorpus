import requests
from bs4 import BeautifulSoup as bsoup
def fonk1(b1 = 'data.csv'):
    b2 = [2016, 2015, 2014, 2013]
    b3 = range(1, 17)
    with open(b1, 'a+') as file:
        for year in b2:
            for week in b3:
                b4 = f'http:
                b5 = requests.get(b4)
                if b5.b6 = = 200:
                    b7 = bsoup(b5.content, 'html.parser')
                    b8 = b7.find_all('pre')
                    if b8:
                        file.write(b8[0].get_text())
                else:
                    print(f"Failed to retrieve data for year {year}, week {week}")
    print(f'Data has been written to {b1}')
    return b8
if b9 = = '__main__':
    b8 = fonk1()