import requests
from bs4 import BeautifulSoup
from collections import deque
import datetime
visited_urls = set(["http:
queue = deque([
    ["http:
    ["http:
    ["http:
])
max_depth = 2
index = 0
with open("index.txt", "w+") as index_file:
    while queue:
        base_url, path, depth = queue.popleft()
        if depth < max_depth:
            try:
                response = requests.get(base_url + path)
                soup = BeautifulSoup(response.text, "html.parser")
                for link in soup.find_all("a"):
                    href = link.get("href")
                    if href not in visited_urls:
                        visited_urls.add(href)
                        if href.startswith("http"):
                            timestamp = datetime.datetime.now().strftime("%m/%d/%Y")
                            line = f"{index}.html {timestamp} {href}\n"
                            index_file.write(line)
                            index += 1
                        if href.startswith("http"):
                            queue.append([href, "", depth + 1])
                        else:
                            queue.append([base_url, href, depth + 1])
            except Exception as e:
                print(f"Error processing URL: {base_url + path}, {e}")