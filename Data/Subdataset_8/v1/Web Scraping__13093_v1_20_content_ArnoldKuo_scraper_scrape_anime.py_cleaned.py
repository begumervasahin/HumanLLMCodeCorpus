import requests
from bs4 import BeautifulSoup
import os
import traceback
def download(url, filename):
    if os.path.exists(filename):
        print('File exists:', filename)
        return
    try:
        r = requests.get(url, stream=True, timeout=60)
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
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
start = 1
end = 8000
for i in range(start, end + 1):
    url = 'http:
    try:
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        for img in soup.find_all('img', class_="preview"):
            target_url = 'http:' + img['src']
            filename = os.path.join('data/anime', target_url.split('/')[-1])
            download(target_url, filename)
        print('%d / %d' % (i, end))
    except Exception as e:
        print('Error accessing page:', e)