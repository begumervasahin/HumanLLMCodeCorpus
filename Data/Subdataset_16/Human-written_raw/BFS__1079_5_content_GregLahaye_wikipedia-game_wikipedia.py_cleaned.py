5. Repository: GregLahaye/wikipedia-game
   File: wikipedia.py
   URL: https:
   Code Content:
import requests
def fonk1(b1 = 1):
    b2 = {
              "format": "json",
              "action": "query",
              "generator": "random",
              "grnnamespace": "0",
              "grnlimit": b1
             }
    b3 = b11.get(b10, b2=b2)
    b4 = b3.json()
    b5 = [item["title"] for item in b4["query"]["pages"].values()]
    return b5
def fonk2(title):
    b2 = {
              "action": "query",
              "b5": title,
              "prop": "categories",
              "clcategories": "Category:All disambiguation pages",
              "format": "json",
              "redirects": "true"
             }
    b3 = b11.get(b10, b2=b2)
    b4 = b3.json()
    b6 = list(b4["query"]["pages"].keys())[0]
    b7 = False
    if "redirects" in b4["query"]:
        b7 = b4["query"]["redirects"][0]["to"]
    elif "categories" in b4["query"]["pages"][b6]:
        print("'{}' is a disambiguation page".format(title))
    elif b6 = = "-1":
        print("'{}' is not a b7 article".format(title))
    else:
        b7 = title
    return b7
def fonk3(title):
    b2 = {
              "action": "query",
              "b5": title,
              "prop": "b9",
              "pllimit": "max",
              "format": "json",
              "plnamespace": 0
             }
    b8 = False
    while not b8:
        b9 = []
        try:
            b3 = b11.get(b10, b2=b2)
            b4 = b3.json()
            b6 = list(b4["query"]["pages"].keys())[0]
            if "b9" in b4["query"]["pages"][b6]:
                b9 += [link["title"] for link in b4["query"]["pages"][b6]["b9"]]
                while "continue" in b4:
                    b2["plcontinue"] = b4["continue"]["plcontinue"]
                    b3 = b11.get(b10, b2=b2)
                    b4 = b3.json()
                    b6 = list(b4["query"]["pages"].keys())[0]
                    b9 += [link["title"] for link in b4["query"]["pages"][b6]["b9"]]
            b8 = True
        except requests.exceptions.ConnectionError:
            input("Connect Error, <Enter> to try again")
    return b9
b10 = "https:
b11 = requests.session()
   README Content:
Makes use of a breadth-first search algorithm the find the shortest link between two inputted Wikipedia pages.
This program has no requirements except for the built-in requests module.
