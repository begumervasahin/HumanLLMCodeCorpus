import requests
import os
from bs4 import BeautifulSoup
def fonk1(b7, b11):
    os.makedirs(b11, b1 = True)
    while True:
        print(f"Fetching page: {b7}")
        b2 = requests.get(b7)
        b2.raise_for_status()
        b3 = BeautifulSoup(b2.text, "lxml")
        b4 = b3.select(".image-size-full")
        for element in b4:
            b5 = element.get('src')
            if b5:
                fonk2(b5, b11)
        b6 = b3.find("a", class_="pagination")
        if b6 and 'href' in b6.attrs:
            b7 = b6.get('href')
        else:
            print("No more pages to download.")
            break
    print("All images have been downloaded.")
def fonk2(b5, b11):
    print(f"Downloading image: {b5}")
    b2 = requests.get(b5)
    b2.raise_for_status()
    b8 = os.path.join(b11, os.path.basename(b5))
    with open(b8, 'wb') as img_file:
        for chunk in b2.iter_content(1024):
            img_file.write(chunk)
if b9 = = "__main__":
    b10 = 'https:
    b11 = "/home/maria/Pictures/downloaded/"
    fonk1(b10, b11)