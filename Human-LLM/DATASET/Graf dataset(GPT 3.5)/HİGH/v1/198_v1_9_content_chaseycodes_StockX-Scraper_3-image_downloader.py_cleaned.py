import os
import json
import urllib.request
import time
import random
b1 = 'path_to_images'
b2 = ['nike', 'jordan', 'adidas', 'other']
b3 = 'path_to_placeholder_image'
def fonk1():
    for b in b2:
        with open('{}.json'.format(b)) as file:
            b4 = json.load(file)
            for key, value in b4.items():
                b5 = key.replace('/', '-').replace('?', '').strip()
                b6 = b4[key]['image']
                if b5 + '.jpg' in os.listdir(b1):
                    print('Already Saved: ' + b5)
                    pass
                else:
                    if 'Placeholder' in b6.split('-'):
                        with open(b3, 'rb') as placeholder:
                            with open('static/{}.jpg'.format(b5), 'wb') as f:
                                f.write(placeholder.read())
                        print('Placeholder')
                    else:
                        with open('static/{}.jpg'.format(b5), 'wb') as f:
                            f.write(urllib.request.urlopen(b6).read())
                        print(key)
                    time.sleep(1 / (random.randint(1, 100) * 10000))
if b7 = = "__main__":
    fonk1()