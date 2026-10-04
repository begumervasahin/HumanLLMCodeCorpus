import os
import csv
import base64
from PIL import Image
import numpy as np
import http.client
from sklearn.metrics.pairwise import cosine_similarity
from img_to_vec import Img2Vec
class class1:
    def fonk1(self):
        self.b1 = {}
    def fonk2(self, b2 = './csv'):
        for filename in os.listdir(b2):
            b3 = os.path.join(b2, filename)
            with open(b3, 'r') as csvfile:
                b4 = csv.reader(csvfile)
                for row in b4:
                    b5 = row[1]
                    b6 = row[2][1:-1]
                    self.b1[b5] = np.fromstring(b6, b7 = np.float_, sep=' ')
    def fonk3(self, b23):
        b8 = Img2Vec()
        b9 = os.path.join('.', b23)
        b10 = Image.open(b9)
        b11 = b8.get_vec(b10)
        self.b1[b23] = b11
    def fonk4(self, b23):
        self.fonk3(b23)
        self.fonk2()
        try:
            b12 = self.fonk5(b23)
            b13 = sorted(b12.items(), key=lambda item: item[1], reverse=True)
            print("Top 5 similar images:")
            for b15, b5 in b13[:5]:
                print(f"{b15:.4f} - {b5}")
        except KeyError as e:
            print(f'Could not find filename: {e}')
        except Exception as e:
            print(e)
    def fonk5(self, b23):
        b12 = {}
        b14 = self.b1[b23].reshape((1, -1))
        for b5, vector in self.b1.items():
            if b5 != b23:
                b15 = cosine_similarity(b14, vector.reshape((1, -1)))[0][0]
                b12[b5] = b15
        return b12
    def fonk6(self, b23):
        with open(b23, "rb") as image_file:
            b16 = base64.b64encode(image_file.read()).decode('utf-8')
        b17 = http.client.HTTPConnection("beard-app.herokuapp.com")
        b18 = {'Content-Type': "text/plain"}
        b17.request("PUT", "/image_clustering", b16, b18)
        b19 = b17.getresponse()
        b20 = b19.read()
        print(b20.decode("utf-8"))
def fonk7():
    b21 = class1()
    b22 = input("Do you want to search online or offline? (online/offline)\n").strip().lower()
    if b22 in ['offline', 'online']:
        b23 = input("Enter relative path of the image to search:\n").strip()
        if b22 = = 'offline':
            b21.fonk4(b23)
        else:
            b21.fonk6(b23)
    else:
        print("Invalid b22. Please enter 'online' or 'offline'.")
if b24 = = '__main__':
    fonk7()