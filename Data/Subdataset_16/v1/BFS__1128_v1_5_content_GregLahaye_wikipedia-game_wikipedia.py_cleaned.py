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
        print("'{}' is a disambiguation b13".format(title))
    elif b8 = = "-1":
        print("'{}' is not a b9 article".format(title))
    else:
        b9 = title
    return b9
def fonk3(title):
    b4 = {
        "action": "query",
        "b7": title,
        "prop": "b11",
        "pllimit": "max",
        "format": "json",
        "plnamespace": 0
    }
    b10 = False
    b11 = []
    while not b10:
        try:
            b5 = b2.get(b1, b4=b4)
            b6 = b5.json()
            b8 = list(b6["query"]["pages"].keys())[0]
            if "b11" in b6["query"]["pages"][b8]:
                b11 += [link["title"] for link in b6["query"]["pages"][b8]["b11"]]
                while "continue" in b6:
                    b4["plcontinue"] = b6["continue"]["plcontinue"]
                    b5 = b2.get(b1, b4=b4)
                    b6 = b5.json()
                    b8 = list(b6["query"]["pages"].keys())[0]
                    b11 += [link["title"] for link in b6["query"]["pages"][b8]["b11"]]
            b10 = True
        except requests.exceptions.ConnectionError:
            input("Connection Error, <Enter> to try again")
    return b11
if b12 = = "__main__":
    print("Random Wikipedia b13:", fonk1())
    b13 = input("Enter a Wikipedia b13 title to check: ")
    print("Checking b13:", fonk2(b13))
    print("Links on the b13:", fonk3(b13))