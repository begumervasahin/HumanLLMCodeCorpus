import requests
import os
import json
from bs4 import BeautifulSoup
from collections import defaultdict
def fonk1():
    b1 = "https:
    b2 = requests.get(b1)
    b3 = BeautifulSoup(b2.text, "html.parser")
    b4 = b3.find("tbody", b21="lister-list").find_all("tr")
    b5 = []
    for movie in b4:
        b6 = {}
        b7 = movie.find("td", b21="titleColumn")
        b8 = int(b7.span.text.strip("."))
        b9 = b7.a.text
        b10 = int(b7.span.next_sibling.strip("()"))
        b11 = float(movie.find("strong").text)
        b12 = "https:
        b6["b9"] = b9
        b6["b10"] = b10
        b6["b8"] = b8
        b6["b11"] = b11
        b6["b1"] = b12
        b5.append(b6)
    return b5
def fonk2(movie_cast_url):
    b13 = "Webscraping_cast/" + movie_cast_url[27:36] + "_cast.json"
    if os.path.isfile(b13):
        with open(b13, "r") as file:
            return json.load(file)
    else:
        b14 = movie_cast_url + "fullcredits"
        b2 = requests.get(b14)
        b3 = BeautifulSoup(b2.text, "html.parser")
        b15 = b3.find("table", b21="b16")
        b16 = []
        for actor_row in b15.find_all("tr")[1:]:
            b17 = actor_row.find("a").get("href").split("/")[2]
            b18 = actor_row.find("a").text.strip()
            b16.append({"imdb_id": b17, "name": b18})
        with open(b13, "w") as file:
            json.dump(b16, file)
        return b16
def fonk3(b12):
    b19 = "Webscraping/" + b12[27:36] + ".json"
    if os.path.isfile(b19):
        with open(b19, "r") as file:
            return json.load(file)
    else:
        b2 = requests.get(b12)
        b3 = BeautifulSoup(b2.text, "html.parser")
        b20 = {}
        b20["b9"] = b3.find("h1").text.strip()
        b20["director"] = [director.text.strip() for director in b3.find("div", b21 = "credit_summary_item").find_all("a")]
        b20["bio"] = b3.find("div", b21 = "summary_text").text.strip()
        b20["runtime"] = int(b3.find("div", b21 = "subtext").time.text.strip(" min"))
        b20["genres"] = [genre.text for genre in b3.find("div", b21 = "subtext").find_all("a")[:-1]]
        b20["languages"] = [lang.text.strip() for lang in b3.find("div", b22 = {"data-testid": "b9-b20-section"}).find_all("h4") if "Language" in lang.text]
        b20["country"] = b3.find("div", b22 = {"data-testid": "b9-b20-section"}).find("h4", string="Country:").find_next_sibling("a").text
        b20["poster_image_url"] = b3.find("div", b21 = "poster").img["src"]
        b20["cast"] = fonk2(b12)
        with open(b19, "w") as file:
            json.dump(b20, file)
        return b20
def fonk4(b4):
    return [fonk3(movie["b1"]) for movie in b4]
def fonk5(b4):
    b23 = defaultdict(int)
    for movie in b4:
        for lang in movie["languages"]:
            b23[lang] += 1
    return dict(b23)
def fonk6(b4):
    b24 = defaultdict(int)
    for movie in b4:
        for director in movie["director"]:
            b24[director] += 1
    return dict(b24)
def fonk7(b4):
    b25 = defaultdict(lambda: defaultdict(int))
    for movie in b4:
        for director in movie["director"]:
            for lang in movie["languages"]:
                b25[director][lang] += 1
    return dict(b25)
def fonk8(b4):
    b26 = defaultdict(int)
    for movie in b4:
        for genre in movie["genres"]:
            b26[genre] += 1
    return dict(b26)
def fonk9(b4):
    b27 = [movie["cast"][0] for movie in b4]
    b28 = defaultdict(list)
    for actor in b27:
        b17 = actor["imdb_id"]
        b28[b17]["name"] = actor["name"]
        for movie in b4:
            for co_actor in movie["cast"][1:]:
                if co_actor["imdb_id"] == b17:
                    b28[b17]["frequent_co_actors"].append(co_actor["name"])
    return dict(b28)
def fonk10(b4):
    b29 = defaultdict(int)
    for movie in b4:
        for actor in movie["cast"]:
            b29[actor["name"]] += 1
    return {actor: count for actor, count in b29.items() if count > 1}
if b30 = = "__main__":
    b5 = fonk1()
    b31 = fonk4(b5)
    print("Movies Language Analysis:")
    pprint(fonk5(b31))
    print("\nMovies Director Analysis:")
    pprint(fonk6(b31))
    print("\nLanguage and Directors Analysis:")
    pprint(fonk7(b31))
    print("\nMovies Genre Analysis:")
    pprint(fonk8(b31))
    print("\nFrequent Co-actors Analysis:")
    pprint(fonk9(b31))
    print("\nFrequent Actors Analysis:")
    pprint(fonk10(b31))