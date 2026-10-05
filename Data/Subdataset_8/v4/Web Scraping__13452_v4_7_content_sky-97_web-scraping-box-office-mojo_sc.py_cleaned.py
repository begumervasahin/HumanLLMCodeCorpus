
from bs4 import BeautifulSoup
import requests
import sqlite3
conn = sqlite3.connect('movie.db')
c = conn.cursor()
c.execute()
for year in range(2010, 2020):
    url = 'https:
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'lxml')
    movie_table = soup.find_all('table')[6]
    headers_row = movie_table.find_all('tr')[0]
    headers = headers_row.find_all('td')
    header_row_list = [headers[0].text, headers[1].text, headers[4].text, headers[5].text, headers[6].text]
    page_data_list = [header_row_list]
    for movie_row in range(2, len(movie_table.find_all('tr')) - 4):
        movie_data_row = movie_table.find_all('tr')[movie_row]
        movie_data_items = movie_data_row.find_all('td')
        movie_details = [movie_data_items[0].text, movie_data_items[1].text,
                         movie_data_items[4].text, movie_data_items[5].text,
                         movie_data_items[6].text]
        page_data_list.append(movie_details)
        c.execute("INSERT INTO movie VALUES (?,?,?,?,?)", (movie_data_items[0].text, movie_data_items[1].text,
                                                            movie_data_items[4].text, movie_data_items[5].text,
                                                            movie_data_items[6].text))
    data.append(page_data_list)
conn.commit()
conn.close()
print("Data appended to database.")