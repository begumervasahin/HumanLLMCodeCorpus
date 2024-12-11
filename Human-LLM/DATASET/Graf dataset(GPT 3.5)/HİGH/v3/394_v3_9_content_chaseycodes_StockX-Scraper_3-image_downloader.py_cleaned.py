import os
import json
import urllib.request
import time
import random
b1 = 'path_to_images'
b2 = ['nike', 'jordan', 'adidas', 'other']
b3 = 'path_to_placeholder_image'
def fonk1():
    for brand in b2:
        fonk2(brand)
def fonk2(brand):
    with open('{}.json'.format(brand)) as file:
        b4 = json.load(file)
        for item_name, item_details in b4.items():
            b5 = fonk3(item_name)
            b6 = item_details['image']
            if not fonk4(b5):
                fonk5(b6, b5)
                fonk8(item_name)
                fonk9()
def fonk3(b5):
    return b5.replace('/', '-').replace('?', '').strip()
def fonk4(b5):
    return b5 + '.jpg' in os.listdir(b1)
def fonk5(b6, b5):
    if 'Placeholder' in b6.split('-'):
        fonk6(b5)
    else:
        fonk7(b6, b5)
def fonk6(b5):
    with open(b3, 'rb') as placeholder:
        with open('static/{}.jpg'.format(b5), 'wb') as f:
            f.write(placeholder.read())
def fonk7(b6, b5):
    with open('static/{}.jpg'.format(b5), 'wb') as f:
        f.write(urllib.request.urlopen(b6).read())
def fonk8(item_name):
    print('Already Saved: ' + item_name)
def fonk9():
    time.sleep(1 / (random.randint(1, 100) * 10000))
if b7 = = "__main__":
    fonk1()