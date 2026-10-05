import requests
from bs4 import BeautifulSoup
import pprint
def fetch_news_page(page_num):
    url = f'https:
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')
def extract_links_and_subtext(soup):
    links = soup.select('.storylink')
    subtext = soup.select('.subtext')
    return links, subtext
def merge_data(links_list, subtext_list):
    return links_list + subtext_list
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)
def create_custom_hn(links, subtext):
    hn = []
    for link, info in zip(links, subtext):
        title = link.getText()
        href = link.get('href', None)
        vote = info.select('.score')
        if vote:
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)
soup1 = fetch_news_page(1)
links1, subtext1 = extract_links_and_subtext(soup1)
soup2 = fetch_news_page(2)
links2, subtext2 = extract_links_and_subtext(soup2)
mega_links = merge_data(links1, links2)
mega_subtext = merge_data(subtext1, subtext2)
pprint.pprint(create_custom_hn(mega_links, mega_subtext))