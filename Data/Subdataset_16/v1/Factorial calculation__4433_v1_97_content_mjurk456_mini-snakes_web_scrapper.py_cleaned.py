import requests
import os
from bs4 import BeautifulSoup
def fonk1(b9, b11):
    os.makedirs(b11, b1 = True)
    while True:
        print(f"Downloading page: {b9}")
        b2 = requests.get(b9)
        b2.raise_for_status()
        b3 = BeautifulSoup(b2.text, "lxml")
        b4 = b3.select(".image-size-full")
        for element in b4:
            b5 = element.get('src')
            if b5:
                print(f"Downloading image: {b5}")
                b6 = requests.get(b5)
                b6.raise_for_status()
                b7 = os.path.join(b11, os.path.basename(b5))
                with open(b7, 'wb') as img_file:
                    for chunk in b6.iter_content(100000):
                        img_file.write(chunk)
        b8 = b3.find("a", class_="pagination")
        if b8 and 'href' in b8.attrs:
            b9 = b8.get('href')
        else:
            break
    print("Download complete.")
if b10 = = "__main__":
    b9 = 'https:
    b11 = "/home/maria/Pictures/downloaded/"
    fonk1(b9, b11)