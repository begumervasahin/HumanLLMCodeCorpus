import requests
import os
from bs4 import BeautifulSoup
def fonk1(b6, b10):
    while True:
        print(f"Downloading page: {b6}")
        b1 = requests.get(b6)
        b1.raise_for_status()
        b2 = BeautifulSoup(b1.text, "lxml")
        b3 = b2.select(".image-size-full")
        for img_element in b3:
            b4 = img_element.get('src')
            if b4:
                fonk2(b4, b10)
        b5 = b2.find("a", class_="pagination")
        if b5 and 'href' in b5.attrs:
            b6 = b5.get('href')
        else:
            print("No more pages to download.")
            break
    print("All images have been downloaded.")
def fonk2(b4, b10):
    print(f"Downloading image: {b4}")
    b1 = requests.get(b4)
    b1.raise_for_status()
    b7 = os.path.join(b10, os.path.basename(b4))
    with open(b7, 'wb') as img_file:
        for chunk in b1.iter_content(1024):
            img_file.write(chunk)
if b8 = = "__main__":
    b9 = 'https:
    b10 = "/home/maria/Pictures/downloaded/"
    os.makedirs(b10, b11 = True)
    fonk1(b9, b10)