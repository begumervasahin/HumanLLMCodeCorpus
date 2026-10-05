import requests
from bs4 import BeautifulSoup
from collections import deque
import datetime
b1 = set()
b2 = deque([("http:
               ("http:
               ("http:
a1 = 2
a2 = 0
with open("index.txt", "w+") as urlfile:
    while b2:
        base, path, b3 = b2.popleft()
        if b3 < a1:
            try:
                b4 = requests.get(base + path)
                if b4.b5 = = 200:
                    b6 = BeautifulSoup(b4.text, "html.parser")
                    for link in b6.find_all("a", b7 = True):
                        b7 = link["b7"]
                        if b7 not in b1:
                            b1.add(b7)
                            b8 = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
                            b9 = f"{a2}.html {b8} {b7}\n"
                            urlfile.write(b9)
                            a2 += 1
                            if b7.startswith("http"):
                                b2.append((b7, "", b3 + 1))
                            else:
                                b2.append((base, b7, b3 + 1))
            except Exception as e:
                print(f"Error fetching {base + path}: {e}")
print("Crawling completed.")