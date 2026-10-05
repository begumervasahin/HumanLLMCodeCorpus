import requests
from bs4 import BeautifulSoup
import pprint
def get_news(page_number):
    url = f'https:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.select('.storylink')
    subtext = soup.select('.subtext')
    return links, subtext
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)
def create_custom_hn(links, subtext):
    hn = []
    for link, sub in zip(links, subtext):
        title = link.getText()
        href = link.get('href', None)
        votes = sub.select_one('.score')
        if votes:
            points = int(votes.getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)
def main():
    all_links = []
    all_subtext = []
    for page_number in range(1, 3):
        links, subtext = get_news(page_number)
        all_links.extend(links)
        all_subtext.extend(subtext)
    hn_list = create_custom_hn(all_links, all_subtext)
    pprint.pprint(hn_list)
if __name__ == "__main__":
    main()