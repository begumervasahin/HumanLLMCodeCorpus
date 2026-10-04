import requests
b1 = "https:
b2 = requests.session()
def fonk1(b3 = 1):
    b4 = {
        "format": "json",
        "action": "query",
        "generator": "random",
        "grnnamespace": "0",
        "grnlimit": b3
    }
    b5 = b2.get(b1, b4=b4)
    b6 = b5.json()
    b7 = [item["title"] for item in b6["query"]["pages"].values()]
    return b7
def fonk2(title):
    b4 = {
        "action": "query",
        "b7": title,
        "prop": "categories",
        "clcategories": "Category:All disambiguation pages",
        "format": "json",
        "redirects": "true"
    }
    b5 = b2.get(b1, b4=b4)
    b6 = b5.json()
    b8 = list(b6["query"]["pages"].keys())[0]
    b9 = False
    if "redirects" in b6["query"]:
        b9 = b6["query"]["redirects"][0]["to"]
    elif "categories" in b6["query"]["pages"][b8]:
        print(f"'{title}' is a disambiguation page")
    elif b8 = = "-1":
        print(f"'{title}' is not a b9 article")
    else:
        b9 = title
    return b9
def fonk3(title):
    b4 = {
        "action": "query",
        "b7": title,
        "prop": "b10",
        "pllimit": "max",
        "format": "json",
        "plnamespace": 0
    }
    b10 = []
    b11 = False
    while not b11:
        try:
            b5 = b2.get(b1, b4=b4)
            b6 = b5.json()
            b8 = list(b6["query"]["pages"].keys())[0]
            if "b10" in b6["query"]["pages"][b8]:
                b10 += [link["title"] for link in b6["query"]["pages"][b8]["b10"]]
                while "continue" in b6:
                    b4["plcontinue"] = b6["continue"]["plcontinue"]
                    b5 = b2.get(b1, b4=b4)
                    b6 = b5.json()
                    b8 = list(b6["query"]["pages"].keys())[0]
                    b10 += [link["title"] for link in b6["query"]["pages"][b8]["b10"]]
            b11 = True
        except requests.exceptions.ConnectionError:
            input("Connection Error, press <Enter> to try again")
    return b10