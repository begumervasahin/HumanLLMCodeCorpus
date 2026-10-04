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
        print(f"Failed to retrieve b10 for year {year}, week {week}")
        return None
def fonk2(b10, b6 = 'test.csv'):
    with open(b6, 'a+') as file:
        file.write(b10)
def fonk3():
    b7 = [2016, 2015, 2014, 2013]
    b8 = range(1, 17)
    b9 = None
    for year in b7:
        for week in b8:
            b10 = fonk1(year, week)
            if b10:
                fonk2(b10)
                b9 = b10
    return b9
if b11 = = '__main__':
    b9 = fonk3()
    print('Data fetching complete.')