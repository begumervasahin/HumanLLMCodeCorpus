import time
import requests
from bs4 import BeautifulSoup
from collections import deque
seed_url = "https:
result_urls = []
queue = deque([])
visited_titles = set()
def BFS_crawler(seed_url):
    depth = 1
    queue.append(seed_url)
    while queue and len(result_urls) < 1000 and depth < 6:
        size = len(queue)
        for _ in range(size):
            current_url = queue.popleft()
            time.sleep(1)
            if not is_visited_url(current_url):
                extract_urls(current_url)
                if len(result_urls) == 1000:
                    output_urls(result_urls)
                    return
        depth += 1
def extract_urls(url):
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")
    content = soup.find('div', {'id': 'mw-content-text'})
    if content:
        for item in content.find_all('a', {'title': True, 'class': False}):
            href = item.get('href', '')
            if is_valid_url(href):
                url = "https:
                if len(result_urls) < 1000 and url not in result_urls:
                    result_urls.append(url)
                    queue.append(url)
                    print(url)
                    print(len(result_urls))
def output_urls(urls):
    file_loc = 'Task_2_A.txt'
    with open(file_loc, "w") as f:
        for url in urls:
            f.write(url + '\n')
        f.write('\nNum of Urls: ' + str(len(urls)) + '\n')
def is_visited_url(url):
    time.sleep(1)
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")
    title = soup.find('h1', {'id': 'firstHeading'})
    if title in visited_titles:
        return True
    else:
        visited_titles.add(title)
        return False
def is_valid_url(href):
    return href and not href.startswith('/wiki/Category:') \
        and not href.startswith('/wiki/File:') \
        and not href.startswith('/wiki/Template:') \
        and not href.startswith('/wiki/Book:') \
        and not href.startswith('/wiki/Portal:') \
        and not href.startswith('/wiki/Help:') \
        and not href.startswith('/wiki/Template_talk:') \
        and not href.startswith('/wiki/Talk:')
if __name__ == "__main__":
    BFS_crawler(seed_url)