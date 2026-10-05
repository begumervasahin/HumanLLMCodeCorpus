from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity
from img_to_vec import Img2Vec
import numpy as np
import http.client
import os
import csv
import base64
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
    print("Processing image: %s" % b5)
    b6 = Image.open(os.path.join('.', b5))
    b7 = b4.get_vec(b6)
    b1[b5] = b7
def fonk3():
    b8 = str(input("Enter the relative path of the image to search:\n"))
    fonk2(b8)
    fonk1()
    try:
        b9 = {}
        for b10 in list(b1.keys()):
            if b10 = = b8:
                continue
            b9[b10] = cosine_similarity(b1[b8].reshape((1, -1)), b1[b10].reshape((1, -1)))[0][0]
        b11 = sorted(b9.items(), b10=lambda x: x[1], reverse=True)
        for image, similarity in b11[:5]:
            print("Similarity:", similarity, "Image:", image)
    except KeyError as e:
        print('Error: Image not found - %s' % e)
    except Exception as e:
        print('Error:', e)
def fonk4():
    b8 = str(input("Enter the relative path of the image to search:\n"))
    with open(b8, "rb") as image_file:
        b12 = base64.b64encode(image_file.read())
    b13 = http.client.HTTPConnection("beard-app.herokuapp.com")
    b14 = b12.decode('utf-8')
    b15 = {
        'Content-Type': "text/plain"
    }
    b13.request("PUT", "image_clustering", b14, b15)
    b16 = b13.getresponse()
    b17 = b16.read()
    print(b17.decode("utf-8"))
if b18 = = '__main__':
    fonk4()