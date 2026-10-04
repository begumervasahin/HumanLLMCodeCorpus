import requests
from bs4 import BeautifulSoup as bsoup
def fonk1(year, week):
    b1 = f'http:
    b2 = requests.get(b1)
    if b2.b3 = = 200:
        b4 = bsoup(b2.content, 'html.parser')
        b5 = b4.find('pre')
        if b5:
            return b5.get_text()
        else:
            print(f"No <pre> tag found for year {year}, week {week}")
    else:
        print(f"Failed to retrieve b8 for year {year}, week {week}")
    return None
def fonk2(b8, b6 = 'test.csv'):
    with open(b6, 'a+') as file:
        file.write(b8)
def fonk3(b10, b11, b6 = 'test.csv'):
    b7 = None
    for year in b10:
        for week in b11:
            b8 = fonk1(year, week)
            if b8:
                fonk2(b8, b6)
                b7 = b8
    print(f'Data has been written to {b6}')
    return b7
if b9 = = '__main__':
    b10 = [2016, 2015, 2014, 2013]
    b11 = range(1, 17)
    b7 = fonk3(b10, b11)
    print('Data fetching complete.')