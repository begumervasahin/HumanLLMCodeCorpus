from bs4 import BeautifulSoup
import requests
import sqlite3
conn = sqlite3.connect('movie.db')
cursor = conn.cursor()
cursor.execute()
for year in range(2010, 2020):
    year_url = f'https:
    page = requests.get(year_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    tables = soup.find_all('table')
    movie_table = tables[6]
    header_row = movie_table.find('tr')
    headers = header_row.find_all('td')
    header_columns = [header.text for header in headers]
    movie_data = [header_columns]
    for movie_row in movie_table.find_all('tr')[2:-4]:
        movie_columns = movie_row.find_all('td')
        movie_info = [column.text for column in movie_columns]
        movie_data.append(movie_info)
        cursor.execute("INSERT INTO movie VALUES (?, ?, ?, ?, ?)", (movie_info[0], movie_info[1], movie_info[4], movie_info[5], movie_info[6]))
conn.commit()
conn.close()
print("Data appended to database successfully.")