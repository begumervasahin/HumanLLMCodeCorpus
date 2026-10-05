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
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        votes = subtext[idx].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)
def main():
    mega_links = []
    mega_subtext = []
    for page_number in range(1, 3):
        links, subtext = get_news(page_number)
        mega_links.extend(links)
        mega_subtext.extend(subtext)
    hn_list = create_custom_hn(mega_links, mega_subtext)
    pprint.pprint(hn_list)
if __name__ == "__main__":
    main()