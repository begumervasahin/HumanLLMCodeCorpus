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
    b2 = './csv'
    for b6 in os.listdir(b2):
        with open(os.path.join(b2, b6), 'r') as csvfile:
            b3 = csv.reader(csvfile)
            for row in b3:
                b1[row[1]] = np.fromstring(row[2][1:-1], b4 = np.float_, sep=' ')
def fonk2(b9):
    b5 = Img2Vec()
    b6 = os.fsdecode(b9)
    print("Processing image:", b6)
    b7 = Image.open(os.path.join('.', b6))
    b8 = b5.get_vec(b7)
    b1[b6] = b8
def fonk3():
    b9 = input("Enter the relative path of the image to search:\n")
    fonk2(b9)
    fonk1()
    try:
        b10 = b1[b9]
        b11 = {}
        for b12, vector in b1.items():
            if b12 = = b9:
                continue
            b13 = cosine_similarity(b10.reshape(1, -1), vector.reshape(1, -1))[0][0]
            b11[b12] = b13
        b14 = sorted(b11.items(), b12=lambda x: x[1], reverse=True)
        print("Top 5 similar images:")
        for image, b13 in b14[:5]:
            print("Similarity:", b13, "- Image:", image)
    except KeyError as e:
        print('Error: Image not found -', e)
    except Exception as e:
        print('Error:', e)
def fonk4():
    b9 = input("Enter the relative path of the image to search:\n")
    with open(b9, "rb") as image_file:
        b15 = base64.b64encode(image_file.read())
    b16 = http.client.HTTPConnection("beard-app.herokuapp.com")
    b17 = b15.decode('utf-8')
    b18 = {'Content-Type': "text/plain"}
    b16.request("PUT", "image_clustering", b17, b18)
    b19 = b16.getresponse()
    b20 = b19.read()
    print(b20.decode("utf-8"))
if b21 = = '__main__':
    fonk4()