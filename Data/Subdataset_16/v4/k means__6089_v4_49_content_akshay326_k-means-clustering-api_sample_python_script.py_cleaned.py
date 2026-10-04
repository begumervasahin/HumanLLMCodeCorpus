import os
import csv
import base64
import numpy as np
import http.client
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity
from img_to_vec import Img2Vec
b1 = {}
def fonk1():
    for b5 in os.listdir('./csv'):
        with open(os.path.join('./csv', b5), 'r') as csvfile:
            b2 = csv.reader(csvfile)
            for row in b2:
                b1[row[1]] = np.fromstring(row[2][1:-1], b3 = np.float_, sep=' ')
def fonk2(b8):
    b4 = Img2Vec()
    b5 = os.fsdecode(b8)
    print(f"Filename is: {b5}")
    b6 = Image.open(os.path.join('.', b5))
    b7 = b4.get_vec(b6)
    b1[b5] = b7
def fonk3():
    b8 = input("Enter relative path of the image to search?\n")
    fonk2(b8)
    fonk1()
    try:
        b9 = {}
        for b10 in b1.keys():
            if b10 = = b8:
                continue
            b9[b10] = cosine_similarity(b1[b8].reshape((1, -1)), b1[b10].reshape((1, -1)))[0][0]
        b11 = [(v, k) for k, v in b9.items()]
        b11.sort(b12 = True)
        for v, k in b11[:5]:
            print(v, k)
    except KeyError as e:
        print(f'Could not find b5 {e}')
    except Exception as e:
        print(e)
def fonk4():
    b8 = input("Enter relative path of the image to search?\n")
    with open(b8, "rb") as image_file:
        b13 = base64.b64encode(image_file.read())
    b14 = http.client.HTTPConnection("beard-app.herokuapp.com")
    b15 = b13.decode('utf-8')
    b16 = {
        'Content-Type': "text/plain"
    }
    b14.request("PUT", "/image_clustering", b15, b16)
    b17 = b14.getresponse()
    b18 = b17.read()
    print(b18.decode("utf-8"))
if b19 = = '__main__':
    fonk4()