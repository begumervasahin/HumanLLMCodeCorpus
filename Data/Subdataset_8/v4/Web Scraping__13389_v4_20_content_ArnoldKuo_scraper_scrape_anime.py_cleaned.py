import requests
from bs4 import BeautifulSoup
import os
import traceback
def download(url, filename):
    if os.path.exists(filename):
        print('File already exists!')
        return
    try:
        response = requests.get(url, stream=True, timeout=60)
        response.raise_for_status()
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
                    file.flush()
        return filename
    except KeyboardInterrupt:
        if os.path.exists(filename):
            os.remove(filename)
        raise KeyboardInterrupt
    except Exception as e:
        traceback.print_exc()
        if os.path.exists(filename):
            os.remove(filename)
if not os.path.exists('data/anime'):
    os.makedirs('data/anime')
start_page = 1
end_page = 8000
for page_number in range(start_page, end_page + 1):
    url = 'http:
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, 'html.parser')
    for image_tag in soup.find_all('img', class_="preview"):
        image_source_url = 'http:' + image_tag['src']
        filename = os.path.join('data/anime', image_source_url.split('/')[-1])
        download(image_source_url, filename)
    print('Processed page %d out of %d' % (page_number, end_page))