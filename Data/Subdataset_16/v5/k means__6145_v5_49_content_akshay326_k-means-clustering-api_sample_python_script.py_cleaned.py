import os
import csv
import base64
import numpy as np
import http.client
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity
from img_to_vec import Img2Vec
b1 = {}
def fonk1(b2 = './csv'):
    for b8 in os.listdir(b2):
        b3 = os.path.join(b2, b8)
        with open(b3, 'r') as csvfile:
            b4 = csv.reader(csvfile)
            for row in b4:
                image_name, b5 = row[1], row[2]
                b6 = np.fromstring(b5[1:-1], dtype=np.float_, sep=' ')
                b1[image_name] = b6
def fonk2(b11):
    b7 = Img2Vec()
    b8 = os.fsdecode(b11)
    print(f"Processing file: {b8}")
    b9 = Image.open(b8)
    b10 = b7.get_vec(b9)
    b1[b8] = b10
def fonk3():
    b11 = input("Enter the relative path of the image to search:\n")
    fonk2(b11)
    fonk1()
    try:
        b12 = b1[b11]
        b13 = {}
        for b14, b10 in b1.items():
            if b14 = = b11:
                continue
            b15 = cosine_similarity(b12.reshape((1, -1)), b10.reshape((1, -1)))[0][0]
            b13[b14] = b15
        b16 = sorted(b13.items(), b14=lambda item: item[1], reverse=True)
        for b15, b8 in b16[:5]:
            print(f"Similarity: {b15:.4f}, Filename: {b8}")
    except KeyError:
        print(f'Filename {b11} not found in the dictionary.')
    except Exception as e:
        print(f"An error occurred: {e}")
def fonk4():
    b11 = input("Enter the relative path of the image to search:\n")
    with open(b11, "rb") as image_file:
        b17 = base64.b64encode(image_file.read()).decode('utf-8')
    b18 = http.client.HTTPConnection("beard-app.herokuapp.com")
    b19 = {'Content-Type': "text/plain"}
    b18.request("PUT", "/image_clustering", b17, b19)
    b20 = b18.getresponse()
    b21 = b20.read()
    print(b21.decode("utf-8"))
if b22 = = '__main__':
    fonk4()