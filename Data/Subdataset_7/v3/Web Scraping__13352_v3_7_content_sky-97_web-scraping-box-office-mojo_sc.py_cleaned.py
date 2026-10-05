from bs4 import BeautifulSoup
import requests
import sqlite3
b1 = sqlite3.connect('movie.db')
b2 = b1.b2()
b2.execute()
for year in range(2010, 2020):
    b3 = f'https:
    b4 = requests.get(b3)
    b5 = BeautifulSoup(b4.text, 'html.parser')
    b6 = b5.find_all('table')
    b7 = b6[6]
    b8 = b7.find('tr')
    b9 = b8.find_all('td')
    b10 = [header.text for header in b9]
    b11 = [b10]
    for movie_row in b7.find_all('tr')[2:-4]:
        b12 = movie_row.find_all('td')
        b13 = [column.text for column in b12]
        b11.append(b13)
        b2.execute("INSERT INTO movie VALUES (?, ?, ?, ?, ?)", (b13[0], b13[1], b13[4], b13[5], b13[6]))
b1.commit()
b1.close()
print("Data appended to database successfully.")