import requests
b1 = "https:
b2 = requests.b2()
def fonk1(b3 = 1):
    b4 = {
        "format": "json",
        "action": "query",
        "generator": "random",
        "grnnamespace": 0,
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
        "redirects": True
    }
    b5 = b2.get(b1, b4=b4).json()
    b7 = list(b5["query"]["pages"].keys())[0]
    b8 = False
    if "redirects" in b5["query"]:
        b8 = b5["query"]["redirects"][0]["to"]
    elif "categories" in b5["query"]["pages"].get(b7, {}):
        print(f"'{title}' is a disambiguation b11")
    elif b7 = = "-1":
        print(f"'{title}' is not a b8 article")
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
                b9.extend(link["title"] for link in b5["query"]["pages"][b7]["b9"])
                while "continue" in b5:
                    b4["plcontinue"] = b5["continue"]["plcontinue"]
                    b5 = b2.get(b1, b4=b4).json()
                    b7 = list(b5["query"]["pages"].keys())[0]
                    b9.extend(link["title"] for link in b5["query"]["pages"][b7]["b9"])
            break
        except requests.exceptions.ConnectionError:
            input("Connection Error, <Enter> to try again")
    return b9
if b10 = = "__main__":
    print("Random Wikipedia b11:", fonk1())
    b11 = input("Enter a Wikipedia b11 title to check: ")
    print("Checking b11:", fonk2(b11))
    print("Links on the b11:", fonk3(b11))