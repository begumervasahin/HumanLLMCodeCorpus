import requests
from bs4 import BeautifulSoup
import os
import traceback
def download_image(url, filename):
    if os.path.exists(filename):
        print('File already exists:', filename)
        return
    try:
        response = requests.get(url, stream=True, timeout=60)
        response.raise_for_status()
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
                    file.flush()
        print('Downloaded:', filename)
    except KeyboardInterrupt:
        if os.path.exists(filename):
            os.remove(filename)
        raise KeyboardInterrupt
    except Exception as e:
        print('Error downloading:', e)
        traceback.print_exc()
        if os.path.exists(filename):
            os.remove(filename)
if not os.path.exists('data/anime'):
    os.makedirs('data/anime')
start_page = 1
end_page = 8000
for page_number in range(start_page, end_page + 1):
    page_url = 'http:
    try:
        page_html = requests.get(page_url).text
        soup = BeautifulSoup(page_html, 'html.parser')
        for img in soup.find_all('img', class_="preview"):
            image_url = 'http:' + img['src']
            filename = os.path.join('data/anime', image_url.split('/')[-1])
            download_image(image_url, filename)
        print('Page %d / %d' % (page_number, end_page))
    except Exception as e:
        print('Error accessing page:', e)