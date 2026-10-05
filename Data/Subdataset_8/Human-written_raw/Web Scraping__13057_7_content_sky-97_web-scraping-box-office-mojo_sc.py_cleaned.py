from bs4 import BeautifulSoup
import requests
import sqlite3
conn = sqlite3.connect('movie.db')
c = conn.cursor()
c.execute()
data =[]
for year in range(2010,2020):
    url = 'https:
    source = requests.get(url)
    soup =BeautifulSoup(source.text,'lxml')
    my_table =soup.find_all('table')[6]
    my_heading =my_table.find_all('tr')[0]
    my_items = my_heading.find_all('td')
    head_list=[my_items[0].text,my_items[1].text,my_items[4].text,my_items[5].text,my_items[6].text]
    page_list=[head_list]
    for movie in range(2,len(my_table.find_all('tr'))-4):
        my_movie=my_table.find_all('tr')[movie]
        my_movie_item = my_movie.find_all('td')
        movie_list=[my_movie_item[0].text,my_movie_item[1].text,my_movie_item[4].text,my_movie_item[5].text,my_movie_item[6].text]
        page_list.append(movie_list)
        c.execute("INSERT into movie values (?,?,?,?,?)",(my_movie_item[0].text,my_movie_item[1].text,my_movie_item[4].text,my_movie_item[5].text,my_movie_item[6].text))
    data.append(page_list)
print("data appended")
conn.commit()
conn.close()