import requests
import os
import json
import random
import time
from bs4 import BeautifulSoup
def scrape_top_list():
    url = requests.get("https:
    soup = BeautifulSoup(url.text, "html.parser")
    list1 = soup.find("tbody", class_="lister-list")
    list2 = list1.find_all("tr")
    all_movies_details = []
    for i in list2:
        trs = i.find("td", class_="titleColumn").getText().strip()
        a = trs.strip()
        list3 = a.split("\n")
        b = list3[1].strip()
        c = float(list3[0])
        d = int(list3[2][1:5])
        rate = i.find("strong").getText().strip()
        url1 = i.find("a")
        half_url = url1.get("href")
        half_url = half_url[:17]
        movie_details = {
            "name": b,
            "year": d,
            "position": c,
            "Ratings": rate,
            "url": "https:
        }
        all_movies_details.append(movie_details)
    return all_movies_details
def group_by_year(movies):
    group_by_year = {}
    for movie in movies:
        year = movie["year"]
        if year not in group_by_year:
            group_by_year[year] = []
        group_by_year[year].append(movie)
    return group_by_year
def decade_by_year(movies):
    decade_by_year = {}
    for movie in movies:
        decade = movie["year"] - (movie["year"] % 10)
        if decade not in decade_by_year:
            decade_by_year[decade] = []
        decade_by_year[decade].append(movie)
    return decade_by_year
def scrape_movie_cast(movie_cast_url):
def scrape_movie_details(movie_url):
def get_movie_list_details(movies_list):
def analyse_movies_language(movies_list):
def analyse_movies_Director(movies_list):
def analyse_language_and_directors(movies_list):
def analyse_movies_genre(movies_list):
def analyse_co_actors(movies_list):
def analyse_actors(movies_list):
top_movies = scrape_top_list()
movies_list = top_movies[:]
pprint(analyse_language_and_directors(movies_list))