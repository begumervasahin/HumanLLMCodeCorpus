import requests
from bs4 import BeautifulSoup
from collections import deque
import datetime
b1 = set(["http:
b2 = deque([["http:
a1 = 2
a2 = 0
b3 = open("index.txt", "w+")
while b2:
    base, path, b4 = b2.popleft()
    if b4 < a1:
        try:
            b5 = BeautifulSoup(requests.get(base + path).text, "html.parser")
            for link in b5.find_all("a"):
                b6 = link.get("b6")
                if b6 not in b1:
                    b1.add(b6)
                    if b6.startswith("http"):
                        b7 = datetime.datetime.now()
                        b7.strftime("%m/%d/%Y")
                        b8 = str(a2) + ".html " + str(b7) + " " + b6 + "\n"
                        b3.write(b8)
                        a2 += 1
                    if b6.startswith("http"):
                        b2.append([b6, "", b4 + 1])
                    else:
                        b2.append([base, b6, b4 + 1])
        except:
            pass
b3.close()