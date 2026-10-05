import requests
class WikipediaGame:
    def __init__(self):
        self.API_URL = "https:
        self.session = requests.session()
    def get_random_page(self, num=1):
        params = {
            "format": "json",
            "action": "query",
            "generator": "random",
            "grnnamespace": "0",
            "grnlimit": num
        }
        response = self.session.get(self.API_URL, params=params).json()
        titles = [item["title"] for item in response["query"]["pages"].values()]
        return titles
    def check_page(self, title):
        params = {
            "action": "query",
            "titles": title,
            "prop": "categories",
            "clcategories": "Category:All disambiguation pages",
            "format": "json",
            "redirects": "true"
        }
        response = self.session.get(self.API_URL, params=params).json()
        pageid = list(response["query"]["pages"].keys())[0]
        valid = False
        if "redirects" in response["query"]:
            valid = response["query"]["redirects"][0]["to"]
        elif "categories" in response["query"]["pages"][pageid]:
            print("'{}' is a disambiguation page".format(title))
        elif pageid == "-1":
            print("'{}' is not a valid article".format(title))
        else:
            valid = title
        return valid
    def get_page_links(self, title):
        params = {
            "action": "query",
            "titles": title,
            "prop": "links",
            "pllimit": "max",
            "format": "json",
            "plnamespace": 0
        }
        done = False
        while not done:
            links = []
            try:
                response = self.session.get(self.API_URL, params=params).json()
                pageid = list(response["query"]["pages"].keys())[0]
                if "links" in response["query"]["pages"][pageid]:
                    links += [link["title"] for link in response["query"]["pages"][pageid]["links"]]
                    while "continue" in response:
                        params["plcontinue"] = response["continue"]["plcontinue"]
                        response = self.session.get(self.API_URL, params=params).json()
                        pageid = list(response["query"]["pages"].keys())[0]
                        links += [link["title"] for link in response["query"]["pages"][pageid]["links"]]
                done = True
            except requests.exceptions.ConnectionError:
                input("Connect Error, <Enter> to try again")
        return links
