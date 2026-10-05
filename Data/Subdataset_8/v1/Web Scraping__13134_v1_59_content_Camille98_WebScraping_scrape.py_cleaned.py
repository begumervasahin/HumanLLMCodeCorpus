import requests
from bs4 import BeautifulSoup
from collections import deque
import datetime
visited = set()
queue = deque([("http:
               ("http:
               ("http:
max_depth = 2
i = 0
with open("index.txt", "w+") as urlfile:
    while queue:
        base, path, depth = queue.popleft()
        if depth < max_depth:
            try:
                response = requests.get(base + path)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")
                    for link in soup.find_all("a", href=True):
                        href = link["href"]
                        if href not in visited:
                            visited.add(href)
                            timestamp = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
                            line = f"{i}.html {timestamp} {href}\n"
                            urlfile.write(line)
                            i += 1
                            if href.startswith("http"):
                                queue.append((href, "", depth + 1))
                            else:
                                queue.append((base, href, depth + 1))
            except Exception as e:
                print(f"Error fetching {base + path}: {e}")
print("Crawling completed.")