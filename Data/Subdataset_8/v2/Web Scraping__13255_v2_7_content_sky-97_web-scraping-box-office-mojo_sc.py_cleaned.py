from bs4 import BeautifulSoup
import requests
import sqlite3
conn = sqlite3.connect('movie.db')
cursor = conn.cursor()
cursor.execute()
for year in range(2010, 2020):
    year_url = 'https:
    page = requests.get(year_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    tables = soup.find_all('table')
    movie_table = tables[6]
    header_row = movie_table.find_all('tr')[0]
    headers = header_row.find_all('td')
    header_columns = [headers[0].text, headers[1].text, headers[4].text, headers[5].text, headers[6].text]
    movie_data = [header_columns]
    for movie_row in range(2, len(movie_table.find_all('tr')) - 4):
        movie_data_row = movie_table.find_all('tr')[movie_row]
        movie_columns = movie_data_row.find_all('td')
        movie_info = [movie_columns[0].text, movie_columns[1].text, movie_columns[4].text, movie_columns[5].text, movie_columns[6].text]
        movie_data.append(movie_info)
        cursor.execute("INSERT INTO movie VALUES (?, ?, ?, ?, ?)", (movie_columns[0].text, movie_columns[1].text, movie_columns[4].text, movie_columns[5].text, movie_columns[6].text))
conn.commit()
conn.close()
print("Data appended to database successfully.")