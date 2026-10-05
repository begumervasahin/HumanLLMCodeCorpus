import requests
import os
import bs4
def fonk1(b8, download_path):
    os.makedirs(download_path, b1 = True)
    while True:
        print("Downloading page:", b8)
        b2 = requests.get(b8)
        b2.raise_for_status()
        b3 = bs4.BeautifulSoup(b2.text, "lxml")
        b4 = b3.select(".image-size-full")
        for element in b4:
            b5 = element.get('src')
            print("Downloading image:", b5)
            b6 = requests.get(b5)
            b6.raise_for_status()
            with open(os.path.join(download_path, os.path.basename(b5)), 'wb') as image_file:
                for chunk in b6.iter_content(100000):
                    image_file.write(chunk)
        b7 = b3.find("a", class_="pagination")
        if b7:
            b8 = b7.get('href')
        else:
            break
    print("Download completed.")
if b9 = = "__main__":
    b8 = 'https:
    b10 = "/home/maria/Pictures/downloaded/"
    fonk1(b8, b10)