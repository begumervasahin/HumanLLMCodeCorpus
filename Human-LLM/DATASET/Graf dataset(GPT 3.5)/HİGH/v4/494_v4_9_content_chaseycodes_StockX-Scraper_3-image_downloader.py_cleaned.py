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
            for key, value in b4.items():
                b5 = key.replace('/', '-').replace('?', '').strip()
                b6 = b4[key]['image']
                if b5 + '.jpg' in os.listdir(b1):
                    print('Already Saved: ' + b5)
                    continue
                else:
                    if 'Placeholder' in b6.split('-'):
                        with open(b2, 'rb') as placeholder:
                            with open('static/{}.jpg'.format(b5), 'wb') as f:
                                f.write(placeholder.read())
                        print('Placeholder: ' + b5)
                    else:
                        with open('static/{}.jpg'.format(b5), 'wb') as f:
                            f.write(urllib.request.urlopen(b6).read())
                        print('Downloaded: ' + b5)
                    time.sleep(1 / (random.randint(1, 100) * 10000))
if b7 = = "__main__":
    fonk1()