import os
import json
import urllib.request
import time
import random
IMAGE_DIRECTORY = 'path_to_images'
PLACEHOLDER_IMAGE_PATH = 'path_to_placeholder_image'
BRANDS = ['nike', 'jordan', 'adidas', 'other']
def download_images():
    for brand in BRANDS:
        with open('{}.json'.format(brand)) as file:
            data = json.load(file)
            for item_name, item_data in data.items():
                item_name_cleaned = item_name.replace('/', '-').replace('?', '').strip()
                img_link = item_data.get('image')
                if f'{item_name_cleaned}.jpg' in os.listdir(IMAGE_DIRECTORY):
                    print(f'Image already saved: {item_name_cleaned}')
                    continue
                else:
                    if 'Placeholder' in img_link.split('-'):
                        with open(PLACEHOLDER_IMAGE_PATH, 'rb') as placeholder:
                            with open(f'static/{item_name_cleaned}.jpg', 'wb') as f:
                                f.write(placeholder.read())
                        print(f'Placeholder used for: {item_name_cleaned}')
                    else:
                        with open(f'static/{item_name_cleaned}.jpg', 'wb') as f:
                            f.write(urllib.request.urlopen(img_link).read())
                        print(f'Downloaded: {item_name_cleaned}')
                    time.sleep(1 / (random.randint(1, 100) * 10000))
if __name__ == "__main__":
    download_images()