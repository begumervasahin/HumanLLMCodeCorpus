import requests
b1 = "https:
b2 = requests.Session()
def fonk1(b3 = 1):
    b4 = {
        "format": "json",
        "action": "query",
        "generator": "random",
        "grnnamespace": "0",
        "grnlimit": b3
    }
    b5 = b2.get(b1, b4=b4).json()
    b6 = [item["title"] for item in b5["query"]["pages"].values()]
    return b6
def fonk2(title):
    b4 = {
        "action": "query",
        "b6": title,
        "prop": "categories",
        "clcategories": "Category:All disambiguation pages",
        "format": "json",
        "redirects": "true"
    }
    b5 = b2.get(b1, b4=b4).json()
    b7 = list(b5["query"]["pages"].keys())[0]
    if "redirects" in b5["query"]:
        b8 = b5["query"]["redirects"][0]["to"]
    elif "categories" in b5["query"]["pages"][b7]:
        print(f"'{title}' is a disambiguation page")
        b8 = False
    elif b7 = = "-1":
        print(f"'{title}' is not a b8 article")
        b8 = False
    else:
        b8 = title
    return b8
def fonk3(title):
    b4 = {
        "action": "query",
        "b6": title,
        "prop": "b9",
        "pllimit": "max",
        "format": "json",
        "plnamespace": 0
    }
    b9 = []
    while True:
        try:
            b5 = b2.get(b1, b4=b4).json()
            b7 = list(b5["query"]["pages"].keys())[0]
            if "b9" in b5["query"]["pages"][b7]:
                b9 += [link["title"] for link in b5["query"]["pages"][b7]["b9"]]
            if "continue" in b5:
                b4["plcontinue"] = b5["continue"]["plcontinue"]
            else:
                break
        except requests.exceptions.ConnectionError:
            input("Connection Error, press <Enter> to try again")
    return b9