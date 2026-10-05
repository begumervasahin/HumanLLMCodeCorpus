import requests
from bs4 import BeautifulSoup
import re
import random
import time
import logging
logging.basicConfig(filename='log.log',
                    filemode='w',
                    format='%(asctime)s %(message)s',
                    level=logging.DEBUG)
logging.info('Starting the scraping process')
delays = [0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89,
          0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99,
          1, 1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.08, 1.09,
          1.1, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.17, 1.18, 1.19, 1.2]
def get_urls_from_tag(soup, tag, class_name):
    items = soup.find_all(tag, class_=class_name)
    urls = [item.find('a').get('href') for item in items if item.find('a')]
    return urls
def extract_pagination_urls(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    pagination_form = soup.find('form', class_='pagination')
    if pagination_form:
        pattern = re.compile(r'Seite\s\d+\svon\s(\d+)', re.I)
        pages = soup.find('a', text=pattern).text.strip()
        total_pages = int(pattern.match(pages).group(1))
        page_urls = ['{}-{}.html'.format(url[:-5], p) for p in range(1, total_pages + 1)]
        return page_urls
    return [url]
def scrape_thread_urls(urls):
    thread_urls = []
    for url in urls:
        delay = random.choice(delays)
        time.sleep(delay)
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.text, 'html.parser')
            thread_list = soup.find_all('h3', class_='threadtitle')
            thread_urls.extend([thread.find('a').get('href') for thread in thread_list if thread.find('a')])
        except Exception as e:
            logging.error(f'Error occurred while scraping {url}: {e}')
    return thread_urls
url = 'http:
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
forum_titles = get_urls_from_tag(soup, 'h2', 'forumtitle')
subforum_titles = get_urls_from_tag(soup, 'li', 'subforum')
with open('forumtitles.txt', 'w') as file:
    file.write('\n'.join(forum_titles))
with open('subforumtitles.txt', 'w') as file:
    file.write('\n'.join(subforum_titles))
logging.info(f'Extracted {len(forum_titles)} forum titles and {len(subforum_titles)} subforum titles')
all_titles = forum_titles + subforum_titles
pagination_urls = [extract_pagination_urls(title) for title in all_titles]
thread_urls = [scrape_thread_urls(urls) for urls in pagination_urls]
all_thread_urls = [url for sublist in thread_urls for url in sublist]
with open('threadurls.txt', 'w') as file:
    file.write('\n'.join(all_thread_urls))
logging.info(f'Extracted {len(all_thread_urls)} thread URLs')
logging.info('Scraping process completed')