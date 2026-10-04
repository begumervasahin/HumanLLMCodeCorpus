import requests
API_URL = "https:
session = requests.session()
def get_random_titles(num=1):
    params = {
        "format": "json",
        "action": "query",
        "generator": "random",
        "grnnamespace": 0,
        "grnlimit": num
    }
    response = session.get(API_URL, params=params).json()
    titles = [item["title"] for item in response["query"]["pages"].values()]
    return titles
def check_title(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "categories",
        "clcategories": "Category:All disambiguation pages",
        "format": "json",
        "redirects": True
    }
    response = session.get(API_URL, params=params).json()
    page_id = list(response["query"]["pages"].keys())[0]
    valid = False
    if "redirects" in response["query"]:
        valid = response["query"]["redirects"][0]["to"]
    elif "categories" in response["query"]["pages"].get(page_id, {}):
        print(f"'{title}' is a disambiguation page")
    elif page_id == "-1":
        print(f"'{title}' is not a valid article")
    else:
        valid = title
    return valid
def get_page_links(title):
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
                links.extend(link["title"] for link in response["query"]["pages"][page_id]["links"])
                while "continue" in response:
                    params["plcontinue"] = response["continue"]["plcontinue"]
                    response = session.get(API_URL, params=params).json()
                    page_id = list(response["query"]["pages"].keys())[0]
                    links.extend(link["title"] for link in response["query"]["pages"][page_id]["links"])
            break
        except requests.exceptions.ConnectionError:
            input("Connection Error, <Enter> to try again")
    return links
if __name__ == "__main__":
    print("Random Wikipedia page:", get_random_titles())
    page = input("Enter a Wikipedia page title to check: ")
    print("Checking page:", check_title(page))
    print("Links on the page:", get_page_links(page))