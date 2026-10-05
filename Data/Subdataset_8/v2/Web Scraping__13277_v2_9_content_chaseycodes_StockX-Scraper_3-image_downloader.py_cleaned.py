import os
import json
import urllib.request
import time
import random
PATH = 'path_to_images'
BRANDS = ['nike', 'jordan', 'adidas', 'other']
PLACEHOLDER_PATH = 'path_to_placeholder_image'
def download_images():
    for brand in BRANDS:
        with open('{}.json'.format(brand)) as file:
            data = json.load(file)
            for key, value in data.items():
                name = key.replace('/', '-').replace('?', '').strip()
                img_link = data[key]['image']
                if name + '.jpg' in os.listdir(PATH):
                    print('Already Saved: ' + name)
                    continue
                else:
                    if 'Placeholder' in img_link.split('-'):
                        with open(PLACEHOLDER_PATH, 'rb') as placeholder:
                            with open('static/{}.jpg'.format(name), 'wb') as f:
                                f.write(placeholder.read())
                        print('Placeholder')
                    else:
                        with open('static/{}.jpg'.format(name), 'wb') as f:
                            f.write(urllib.request.urlopen(img_link).read())
                        print(key)
                    time.sleep(1 / (random.randint(1, 100) * 10000))
if __name__ == "__main__":
    download_images()