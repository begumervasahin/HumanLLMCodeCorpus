import requests
from bs4 import BeautifulSoup
from collections import deque
import datetime
visited_urls = set()
queue = deque([
    ("http:
    ("http:
    ("http:
])
max_depth = 2
file_counter = 0
with open("index.txt", "w+") as index_file:
    while queue:
        base_url, relative_path, depth = queue.popleft()
        if depth < max_depth:
            try:
                response = requests.get(base_url + relative_path)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")
                    for link in soup.find_all("a", href=True):
                        href = link["href"]
                        if href not in visited_urls:
                            visited_urls.add(href)
                            timestamp = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
                            line = f"{file_counter}.html {timestamp} {href}\n"
                            index_file.write(line)
                            file_counter += 1
                            if href.startswith("http"):
                                queue.append((href, "", depth + 1))
                            else:
                                queue.append((base_url, href, depth + 1))
            except Exception as e:
                print(f"Error fetching {base_url + relative_path}: {e}")
print("Crawling completed.")