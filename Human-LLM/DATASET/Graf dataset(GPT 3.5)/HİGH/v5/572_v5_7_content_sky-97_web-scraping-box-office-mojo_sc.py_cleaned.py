import requests
from bs4 import BeautifulSoup
import sqlite3
b1 = sqlite3.connect('movie.db')
b2 = b1.cursor()
b2.execute()
def fonk1(year):
    b3 = f'https:
    b4 = requests.get(b3)
    b5 = BeautifulSoup(b4.text, 'lxml')
    b6 = b5.find_all('table')[6]
    b7 = b6.find_all('tr')[0].find_all('td')
    b8 = [header.text for header in b7]
    b9 = [b8]
    for movie_row in b6.find_all('tr')[2:-4]:
        b10 = movie_row.find_all('td')
        b11 = [item.text for item in b10]
        b9.append(b11)
        b2.execute("INSERT INTO movie VALUES (?,?,?,?,?)", b11)
    return b9
for year in range(2010, 2020):
    b12 = fonk1(year)
b1.commit()
b1.close()
print("Data appended to database.")