import os
import requests
import traceback
from bs4 import BeautifulSoup
def download_image(url, filename):
    if os.path.exists(filename):
        print(f"File '{filename}' already exists.")
        return
    try:
        response = requests.get(url, stream=True, timeout=60)
        response.raise_for_status()
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
                    file.flush()
        print(f"Downloaded '{filename}' successfully.")
        return filename
    except KeyboardInterrupt:
        if os.path.exists(filename):
            os.remove(filename)
        raise KeyboardInterrupt
    except Exception as e:
        traceback.print_exc()
        if os.path.exists(filename):
            os.remove(filename)
download_directory = 'data/anime'
if not os.path.exists(download_directory):
    os.makedirs(download_directory)
start_page = 1
end_page = 8000
for page_number in range(start_page, end_page + 1):
    url = f'http:
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, 'html.parser')
    for image_tag in soup.find_all('img', class_='preview'):
        image_source_url = 'http:' + image_tag['src']
        filename = os.path.join(download_directory, os.path.basename(image_source_url))
        download_image(image_source_url, filename)
    print(f"Processed page {page_number} out of {end_page}")