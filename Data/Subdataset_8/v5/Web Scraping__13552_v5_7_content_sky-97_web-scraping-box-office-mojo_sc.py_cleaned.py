import requests
from bs4 import BeautifulSoup
import sqlite3
conn = sqlite3.connect('movie.db')
c = conn.cursor()
c.execute()
def fetch_movie_data(year):
    url = f'https:
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'lxml')
    movie_table = soup.find_all('table')[6]
    headers = movie_table.find_all('tr')[0].find_all('td')
    header_row_list = [header.text for header in headers]
    page_data_list = [header_row_list]
    for movie_row in movie_table.find_all('tr')[2:-4]:
        movie_data_items = movie_row.find_all('td')
        movie_details = [item.text for item in movie_data_items]
        page_data_list.append(movie_details)
        c.execute("INSERT INTO movie VALUES (?,?,?,?,?)", movie_details)
    return page_data_list
for year in range(2010, 2020):
    data = fetch_movie_data(year)
conn.commit()
conn.close()
print("Data appended to database.")