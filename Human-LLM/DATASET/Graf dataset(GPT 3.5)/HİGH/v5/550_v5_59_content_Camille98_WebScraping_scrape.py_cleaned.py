import requests
from bs4 import BeautifulSoup
from collections import deque
import datetime
b1 = set(["http:
b2 = deque([
    ["http:
    ["http:
    ["http:
])
a1 = 2
a2 = 0
with open("a2.txt", "w+") as index_file:
    while b2:
        base_url, path, b3 = b2.popleft()
        if b3 < a1:
            try:
                b4 = requests.get(base_url + path)
                b5 = BeautifulSoup(b4.text, "html.parser")
                for link in b5.find_all("a"):
                    b6 = link.get("b6")
                    if b6 not in b1:
                        b1.add(b6)
                        if b6.startswith("http"):
                            b7 = datetime.datetime.now().strftime("%m/%d/%Y")
                            b8 = f"{a2}.html {b7} {b6}\n"
                            index_file.write(b8)
                            a2 += 1
                        if b6.startswith("http"):
                            b2.append([b6, "", b3 + 1])
                        else:
                            b2.append([base_url, b6, b3 + 1])
            except Exception as e:
                print(f"Error processing URL: {base_url + path}, {e}")