import requests
import os
import bs4
b1 = 'https:
b2 = "/home/maria/Pictures/downloaded/"
os.makedirs(b2, b3 = True)
while True:
    print("Downloading page:", b1)
    b4 = requests.get(b1)
    b4.raise_for_status()
    b5 = bs4.BeautifulSoup(b4.text, "lxml")
    b6 = b5.select(".image-size-full")
    for element in b6:
        b7 = element.get('src')
        print("Downloading image:", b7)
        b8 = requests.get(b7)
        b8.raise_for_status()
        with open(os.path.join(b2, os.path.basename(b7)), 'wb') as image_file:
            for chunk in b8.iter_content(100000):
                image_file.write(chunk)
    b9 = b5.find("a", class_="pagination")
    if b9:
        b1 = b9.get('href')
    else:
        break
print("Download completed.")