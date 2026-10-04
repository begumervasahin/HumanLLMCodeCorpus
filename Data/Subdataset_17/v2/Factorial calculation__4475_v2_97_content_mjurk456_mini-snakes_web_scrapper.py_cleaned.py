import requests
import os
from bs4 import BeautifulSoup
def download_images_from_url(url, save_directory):
    os.makedirs(save_directory, exist_ok=True)
    while True:
        print(f"Fetching page: {url}")
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "lxml")
        img_elements = soup.select(".image-size-full")
        for element in img_elements:
            img_url = element.get('src')
            if img_url:
                print(f"Downloading image: {img_url}")
                img_response = requests.get(img_url)
                img_response.raise_for_status()
                img_filename = os.path.join(save_directory, os.path.basename(img_url))
                with open(img_filename, 'wb') as img_file:
                    for chunk in img_response.iter_content(1024):
                        img_file.write(chunk)
        next_link = soup.find("a", class_="pagination")
        if next_link and 'href' in next_link.attrs:
            url = next_link.get('href')
        else:
            print("No more pages to download.")
            break
    print("All images have been downloaded.")
if __name__ == "__main__":
    url = 'https:
    save_directory = "/home/maria/Pictures/downloaded/"
    download_images_from_url(url, save_directory)