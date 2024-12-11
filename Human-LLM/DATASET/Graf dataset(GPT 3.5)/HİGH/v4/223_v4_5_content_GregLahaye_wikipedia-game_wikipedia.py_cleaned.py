import requests
b1 = "https:
b2 = requests.b2()
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
    b8 = False
    if "redirects" in b5["query"]:
        b8 = b5["query"]["redirects"][0]["to"]
    elif "categories" in b5["query"]["pages"][b7]:
        print("'{}' is a disambiguation page".format(title))
    elif b7 = = "-1":
        print("'{}' is not a b8 article".format(title))
    else:
        b8 = title
    return b8
def fonk3(title):
    b4 = {
        "action": "query",
        "b6": title,
        "prop": "b10",
        "pllimit": "max",
        "format": "json",
        "plnamespace": 0
    }
    b9 = False
    while not b9:
        b10 = []
        try:
            b5 = b2.get(b1, b4=b4).json()
            b7 = list(b5["query"]["pages"].keys())[0]
            if "b10" in b5["query"]["pages"][b7]:
                b10 += [link["title"] for link in b5["query"]["pages"][b7]["b10"]]
                while "continue" in b5:
                    b4["plcontinue"] = b5["continue"]["plcontinue"]
                    b5 = b2.get(b1, b4=b4).json()
                    b7 = list(b5["query"]["pages"].keys())[0]
                    b10 += [link["title"] for link in b5["query"]["pages"][b7]["b10"]]
            b9 = True
        except requests.exceptions.ConnectionError:
            input("Connect Error, <Enter> to try again")
    return b10