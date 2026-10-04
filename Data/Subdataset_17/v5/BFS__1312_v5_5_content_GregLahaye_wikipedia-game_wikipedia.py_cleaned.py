import requests
API_URL = "https:
session = requests.Session()
def random(num=1):
    params = {
        "format": "json",
        "action": "query",
        "generator": "random",
        "grnnamespace": "0",
        "grnlimit": num
    }
    response = session.get(API_URL, params=params).json()
    titles = [item["title"] for item in response["query"]["pages"].values()]
    return titles
def check(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "categories",
        "clcategories": "Category:All disambiguation pages",
        "format": "json",
        "redirects": "true"
    }
    response = session.get(API_URL, params=params).json()
    page_id = list(response["query"]["pages"].keys())[0]
    if "redirects" in response["query"]:
        valid = response["query"]["redirects"][0]["to"]
    elif "categories" in response["query"]["pages"][page_id]:
        print(f"'{title}' is a disambiguation page")
        valid = False
    elif page_id == "-1":
        print(f"'{title}' is not a valid article")
        valid = False
    else:
        valid = title
    return valid
def get_links(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "links",
        "pllimit": "max",
        "format": "json",
        "plnamespace": 0
    }
    links = []
    while True:
        try:
            response = session.get(API_URL, params=params).json()
            page_id = list(response["query"]["pages"].keys())[0]
            if "links" in response["query"]["pages"][page_id]:
                links += [link["title"] for link in response["query"]["pages"][page_id]["links"]]
            if "continue" in response:
                params["plcontinue"] = response["continue"]["plcontinue"]
            else:
                break
        except requests.exceptions.ConnectionError:
            input("Connection Error, press <Enter> to try again")
    return links