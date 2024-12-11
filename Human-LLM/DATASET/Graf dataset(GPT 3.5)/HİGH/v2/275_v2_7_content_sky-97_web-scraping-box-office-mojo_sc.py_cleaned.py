from bs4 import BeautifulSoup
import requests
import sqlite3
b1 = sqlite3.connect('movie.db')
b2 = b1.b2()
b2.execute()
for year in range(2010, 2020):
    b3 = 'https:
    b4 = requests.get(b3)
    b5 = BeautifulSoup(b4.text, 'html.parser')
    b6 = b5.find_all('table')
    b7 = b6[6]
    b8 = b7.find_all('tr')[0]
    b9 = b8.find_all('td')
    b10 = [b9[0].text, b9[1].text, b9[4].text, b9[5].text, b9[6].text]
    b11 = [b10]
    for movie_row in range(2, len(b7.find_all('tr')) - 4):
        b12 = b7.find_all('tr')[movie_row]
        b13 = b12.find_all('td')
        b14 = [b13[0].text, b13[1].text, b13[4].text, b13[5].text, b13[6].text]
        b11.append(b14)
        b2.execute("INSERT INTO movie VALUES (?, ?, ?, ?, ?)", (b13[0].text, b13[1].text, b13[4].text, b13[5].text, b13[6].text))
b1.commit()
b1.close()
print("Data appended to database successfully.")