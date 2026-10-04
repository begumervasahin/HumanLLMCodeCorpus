import requests
import os
from bs4 import BeautifulSoup
def download_images_from_page(url, save_directory):
    while True:
        print(f"Downloading page: {url}")
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "lxml")
        img_elements = soup.select(".image-size-full")
        for img_element in img_elements:
            img_url = img_element.get('src')
            if img_url:
                download_image(img_url, save_directory)
        next_page_link = soup.find("a", class_="pagination")
        if next_page_link and 'href' in next_page_link.attrs:
            url = next_page_link.get('href')
        else:
            print("No more pages to download.")
            break
    print("All images have been downloaded.")
def download_image(img_url, save_directory):
    print(f"Downloading image: {img_url}")
    response = requests.get(img_url)
    response.raise_for_status()
    img_filename = os.path.join(save_directory, os.path.basename(img_url))
    with open(img_filename, 'wb') as img_file:
        for chunk in response.iter_content(1024):
            img_file.write(chunk)
if __name__ == "__main__":
    start_url = 'https:
    save_directory = "/home/maria/Pictures/downloaded/"
    os.makedirs(save_directory, exist_ok=True)
    download_images_from_page(start_url, save_directory)