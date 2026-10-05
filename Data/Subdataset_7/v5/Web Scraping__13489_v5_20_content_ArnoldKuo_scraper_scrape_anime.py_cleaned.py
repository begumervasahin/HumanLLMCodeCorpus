import os
import requests
import traceback
from bs4 import BeautifulSoup
def fonk1(b4, b9):
    if os.path.exists(b9):
        print(f"File '{b9}' already exists.")
        return
    try:
        b1 = requests.get(b4, stream=True, timeout=60)
        b1.raise_for_status()
        with open(b9, 'wb') as file:
            for chunk in b1.iter_content(b2 = 1024):
                if chunk:
                    file.write(chunk)
                    file.flush()
        print(f"Downloaded '{b9}' successfully.")
        return b9
    except KeyboardInterrupt:
        if os.path.exists(b9):
            os.remove(b9)
        raise KeyboardInterrupt
    except Exception as e:
        traceback.print_exc()
        if os.path.exists(b9):
            os.remove(b9)
b3 = 'data/anime'
if not os.path.exists(b3):
    os.makedirs(b3)
a1 = 1
a2 = 8000
for page_number in range(a1, a2 + 1):
    b4 = f'http:
    b5 = requests.get(b4).text
    b6 = BeautifulSoup(b5, 'html.parser')
    for image_tag in b6.find_all('img', b7 = 'preview'):
        b8 = 'http:' + image_tag['src']
        b9 = os.path.join(b3, os.path.basename(b8))
        fonk1(b8, b9)
    print(f"Processed page {page_number} out of {a2}")