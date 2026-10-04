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
                    self.b1[row[1]] = np.fromstring(row[2][1:-1], b5 = np.float_, sep=' ')
    def fonk3(self, b20):
        b6 = Img2Vec()
        b7 = os.path.join('.', b20)
        b8 = Image.open(b7)
        b9 = b6.get_vec(b8)
        self.b1[b20] = b9
    def fonk4(self, b20):
        self.fonk3(b20)
        self.fonk2()
        try:
            b10 = {
                key: cosine_similarity(
                    self.b1[b20].reshape((1, -1)),
                    b9.reshape((1, -1))
                )[0][0]
                for key, b9 in self.b1.items() if key != b20
            }
            b11 = sorted([(v, k) for k, v in b10.items()], reverse=True)
            for v, k in b11[:5]:
                print(f"{v:.4f} - {k}")
        except KeyError as e:
            print(f'Could not find filename: {e}')
        except Exception as e:
            print(e)
    def fonk5(self, b20):
        with open(b20, "rb") as image_file:
            b12 = base64.b64encode(image_file.read()).decode('utf-8')
        b13 = http.client.HTTPConnection("beard-app.herokuapp.com")
        b14 = {'Content-Type': "text/plain"}
        b13.request("PUT", "/image_clustering", b12, b14)
        b15 = b13.getresponse()
        b16 = b15.read()
        print(b16.decode("utf-8"))
if b17 = = '__main__':
    b18 = class1()
    b19 = input("Do you want to search online or offline? (online/offline)\n").strip().lower()
    if b19 in ['offline', 'online']:
        b20 = input("Enter relative path of the image to search:\n").strip()
        if b19 = = 'offline':
            b18.fonk4(b20)
        else:
            b18.fonk5(b20)
    else:
        print("Invalid b19. Please enter 'online' or 'offline'.")