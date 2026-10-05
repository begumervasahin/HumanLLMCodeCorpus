import requests
from bs4 import BeautifulSoup
import os
import traceback
def fonk1(url, b8):
    if os.path.exists(b8):
        print('File already exists:', b8)
        return
    try:
        b1 = requests.get(url, stream=True, timeout=60)
        b1.raise_for_status()
        with open(b8, 'wb') as file:
            for chunk in b1.iter_content(b2 = 1024):
                if chunk:
                    file.write(chunk)
                    file.flush()
        print('Downloaded:', b8)
    except KeyboardInterrupt:
        if os.path.exists(b8):
            os.remove(b8)
        raise KeyboardInterrupt
    except Exception as e:
        print('Error downloading:', e)
        traceback.print_exc()
        if os.path.exists(b8):
            os.remove(b8)
if not os.path.exists('data/anime'):
    os.makedirs('data/anime')
a1 = 1
a2 = 8000
for page_number in range(a1, a2 + 1):
    b3 = 'http:
    try:
        b4 = requests.get(b3).text
        b5 = BeautifulSoup(b4, 'html.parser')
        for img in b5.find_all('img', b6 = "preview"):
            b7 = 'http:' + img['src']
            b8 = os.path.join('data/anime', os.path.basename(b7))
            fonk1(b7, b8)
        print('Page %d / %d' % (page_number, a2))
    except Exception as e:
        print('Error accessing page:', e)