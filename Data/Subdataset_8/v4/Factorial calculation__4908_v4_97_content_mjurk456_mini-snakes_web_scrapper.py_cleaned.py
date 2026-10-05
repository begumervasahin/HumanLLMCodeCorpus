import requests
import os
import bs4
url = 'https:
download_directory = "/home/maria/Pictures/downloaded/"
os.makedirs(download_directory, exist_ok=True)
while True:
    print("Downloading page:", url)
    response = requests.get(url)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, "lxml")
    image_elements = soup.select(".image-size-full")
    for element in image_elements:
        img_url = element.get('src')
        print("Downloading image:", img_url)
        image_response = requests.get(img_url)
        image_response.raise_for_status()
        with open(os.path.join(download_directory, os.path.basename(img_url)), 'wb') as image_file:
            for chunk in image_response.iter_content(100000):
                image_file.write(chunk)
    next_link = soup.find("a", class_="pagination")
    if next_link:
        url = next_link.get('href')
    else:
        break
print("Download completed.")