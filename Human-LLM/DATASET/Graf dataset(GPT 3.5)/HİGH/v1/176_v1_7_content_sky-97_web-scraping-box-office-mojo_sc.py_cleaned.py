from bs4 import BeautifulSoup
import requests
import sqlite3
b1 = sqlite3.connect('movie.db')
b2 = b1.cursor()
b2.execute()
for year in range(2010, 2020):
    b3 = 'https:
    b4 = requests.get(b3)
    b5 = BeautifulSoup(b4.text, 'html.parser')
    b6 = b5.find_all('table')[6]
    b7 = b6.find_all('tr')[0]
    b8 = b7.find_all('td')
    b9 = [b8[0].text, b8[1].text, b8[4].text, b8[5].text, b8[6].text]
    b10 = [b9]
    for movie in range(2, len(b6.find_all('tr')) - 4):
        b11 = b6.find_all('tr')[movie]
        b12 = b11.find_all('td')
        b13 = [b12[0].text, b12[1].text, b12[4].text, b12[5].text, b12[6].text]
        b10.append(b13)
        b2.execute("INSERT INTO movie VALUES (?, ?, ?, ?, ?)",
                  (b12[0].text, b12[1].text, b12[4].text, b12[5].text, b12[6].text))
b1.commit()
b1.close()
print("Data appended to database successfully.")