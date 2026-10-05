import re
from bs4 import BeautifulSoup
from downloading import download_webpage
def scrape_with_regex(url, search_regex):
    html_content = download_webpage(url)
    matches = re.findall(search_regex, html_content)
    return matches
def create_soup(html_content):
    soup_object = BeautifulSoup(html_content, 'html5lib')
    return soup_object
def search_games_in_soup(soup, game_info=[]):
    game_elements = soup.find_all("div", {"class": "w-product"})
    with open("soup_object.html", 'w') as soup_file:
        soup_file.write(str(game_elements))
    for element in game_elements:
        game_title = element.find("img")['title']
        game_price = element.find("span", class_="w-currentPrice").text
        game_info.append((game_title, game_price))
    return game_info
def main():
    webpage_url = 'https:
    webpage_content = download_webpage(webpage_url)
    soup_object = create_soup(webpage_content)
    games_info = search_games_in_soup(soup_object)
    print(games_info)
if __name__ == '__main__':
    main()