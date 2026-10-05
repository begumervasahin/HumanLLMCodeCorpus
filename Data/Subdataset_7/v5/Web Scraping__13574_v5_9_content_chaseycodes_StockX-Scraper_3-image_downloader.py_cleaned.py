import os
import json
import urllib.request
import time
import random
b1 = 'path_to_images'
b2 = 'path_to_placeholder_image'
b3 = ['nike', 'jordan', 'adidas', 'other']
def fonk1():
    for brand in b3:
        with open('{}.json'.format(brand)) as file:
            b4 = json.load(file)
            for item_name, item_data in b4.items():
                b5 = item_name.replace('/', '-').replace('?', '').strip()
                b6 = item_data.get('image')
                if f'{b5}.jpg' in os.listdir(b1):
                    print(f'Image already saved: {b5}')
                    continue
                else:
                    if 'Placeholder' in b6.split('-'):
                        with open(b2, 'rb') as placeholder:
                            with open(f'static/{b5}.jpg', 'wb') as f:
                                f.write(placeholder.read())
                        print(f'Placeholder used for: {b5}')
                    else:
                        with open(f'static/{b5}.jpg', 'wb') as f:
                            f.write(urllib.request.urlopen(b6).read())
                        print(f'Downloaded: {b5}')
                    time.sleep(1 / (random.randint(1, 100) * 10000))
if b7 = = "__main__":
    fonk1()