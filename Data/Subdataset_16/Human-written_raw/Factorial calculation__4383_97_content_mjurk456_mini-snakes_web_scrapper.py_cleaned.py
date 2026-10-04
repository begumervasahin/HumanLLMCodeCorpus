import requests, os, bs4
b1 = 'https:
os.makedirs("/home/maria/Pictures/downloaded/", b2 = True)
while True:
    print("Downloading page %s" % b1)
    b3 = requests.get(b1)
    b3.raise_for_status()
    b4 = bs4.BeautifulSoup(b3.text, "lxml")
    b5 = b4.select(".image-size-full")
    for element in b5:
        b6 = element.get('src')
        print("Downloading image %s" % b6)
        b3 = requests.get(b6)
        b3.raise_for_status()
        b7 = open(os.path.join('/home/maria/Pictures/downloaded/', \
								os.path.basename(b6)), 'wb')
        for chunk in b3.iter_content(100000):
            b7.write(chunk)
        b7.close()
    b8 = b4.find("a", class_="pagination")
    if b8:
        b1 = b8.get('href')
    else:
        break
print("Done")