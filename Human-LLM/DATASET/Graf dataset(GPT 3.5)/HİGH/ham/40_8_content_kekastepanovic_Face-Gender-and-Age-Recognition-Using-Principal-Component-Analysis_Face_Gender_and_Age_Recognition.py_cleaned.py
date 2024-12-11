import numpy as np
import cv2
import os
import random2 as random
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
b1 = list()
b2 = list()
b3 = list()
b4 = list()
b5 = list()
b6 = list()
a1 = 0
a2 = 0
a3 = 0
b7 = r"C:\Users\Computer\Desktop\KV\Viola and Jones"
b8 = r"C:\Users\Computer\Desktop\KV\treniranje a6 testiranje"
b9 = r"C:\Users\Computer\Desktop\KV\jedinicna lica"
a4 = 50
a5 = 0
while a5<=110:
   b10 = random.choice([x for x in os.listdir(r"C:\Users\Computer\Desktop\KV\part1") if os.path.isfile(os.path.join(r"C:\Users\Computer\Desktop\KV\part1", x))])
   a5 = a5+1
   b11 = cv2.imread(os.path.join(r"C:\Users\Computer\Desktop\KV\part1",b10))
   b12 = cv2.cvtColor(b11,cv2.COLOR_BGR2GRAY)
   b13 = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
   b14 = b13.detectMultiScale(b12)
   a6 = 0
   for(column,row,width,height) in b14:
       cv2.rectangle(b12,(column,row),(column+width,row+height),(0,255,0),2)
       b15 = b12[row:row+height,column:column+width]
       b16 = b10
       b15 = cv2.resize(b15,(360,480))
       if a6 = =0:
          b6.append(b16)
          b1.append(b15)
          cv2.imwrite(os.path.join(b7,b16),b15)
          b17 = b16.find("_")
          b18 = b16[0:b17]
          b18 = int(b18)
          if(b18<45):
              b3.append(0)
          else:
              b3.append(1)
          b2.append(b16[b17 + 1])
          cv2.waitKey(40)
       a6 = a6+1
a7 = 0
a8 = 0
for img in b1:
    a8 = a8+1
b19 = np.zeros(shape=(a8,172800))
for img in b1:
    b19[a7,:]=np.reshape(img,(1,172800),'F')
    a7 = a7+1
b20 = np.random.rand(len(b19))<0.8
b2 = np.array(b2)
b3 = np.array(b3)
b6 = np.array(b6)
b21 = b19[b20,:]
b22 = b6[b20]
b23 = b2[b20]
b24 = b3[b20]
b25 = b19[~b20,:]
b26 = b6[~b20]
b27 = b2[~b20]
b28 = b3[~b20]
b29 = np.sum(b21,b40=0)/len(b21)
b30 = np.sum(b25,b40=0)/len(b25)
b31 = b21
b32 = b25
for xx in range(len(b21)):
    b21[xx,:]=b21[xx,:]-b29
for xx in range(len(b25)):
   b25[xx,:]=b25[xx,:]-b30
U, Sigma, b33 = np.linalg.svd(b21, full_matrices=False)
b34 = np.matmul(b21,b33[:a4,:].T)
b35 = np.matmul(b25,b33[:a4,:].T)
b36 = len(b35)
for r_idx in range(len(b35)):
    if(a3<=3):
          b37 = np.reshape(b32[r_idx,:],(360,480),'C')
          b38 = str(a3)+"test"+b26[r_idx]
          cv2.imwrite(os.path.join(b8,b38),b37)
    b39 = list()
    for training in range(len(b34)):
       b39.append(np.sum((b34[training,:]-b35[r_idx,:])**2,b40 = 0))
    b41 = b39.index(min(b39))
    if (a3 <= 3):
        b42 = np.reshape(b31[b41, :], (360, 480),'C')
        b38 = str(a3)+"train"+b22[b41]
        cv2.imwrite(os.path.join(b8, b38), b42)
    b43 = b23[b41]
    b4.append(b43)
    b18 = b24[b41]
    b5.append(b18)
    if(b27[r_idx]==b43):
        a1 = a1+1
    if(b28[r_idx]==b18):
        a2 = a2+1
    del b39[:]
    a3 = a3+1
b4 = np.array(b4)
b5 = np.array(b5)
b44 = (a1/b36)*100
b45 = (a2/b36)*100
print(b44)
print(confusion_matrix(b27,b4))
print(b45)
print(confusion_matrix(b28,b5))
b46 = MLPClassifier(hidden_layer_sizes=(15,10),max_iter=1000,solver='adam',batch_size='auto',early_stopping=True)
b46.fit(b34,b23)
b47 = b46.predict(b35)
print(confusion_matrix(b27,b47))
b48 = MLPClassifier(hidden_layer_sizes=(15,10),max_iter=1000,solver='adam',batch_size='auto',early_stopping=True)
b48.fit(b34,b24)
b49 = b48.predict(b35)
print(confusion_matrix(b28,b49))
b50 = np.sum(b19,b40=0)/len(b19)
b51 = np.reshape(b50,(360,480),'C')
b52 = "average_photo.jpg"
cv2.imwrite(os.path.join(b7,b52),b51)
b53 = "face1.jpg"
b54 = "face2.jpg"
b55 = "face3.jpg"
b56 = "face4.jpg"
b57 = np.reshape(b33[0,:].T,(360,480))
b58 = np.reshape(b33[1,:].T,(360,480))
b59 = np.reshape(b33[2,:].T,(360,480))
b60 = np.reshape(b33[3,:].T,(360,480))
ret,b61 = cv2.threshold(b57,0,175,cv2.THRESH_BINARY)
ret,b62 = cv2.threshold(b58,0,175,cv2.THRESH_BINARY)
ret,b63 = cv2.threshold(b59,0,175,cv2.THRESH_BINARY)
ret,b64 = cv2.threshold(b60,0,175,cv2.THRESH_BINARY)
cv2.imwrite(os.path.join(b9,b53),b61)
cv2.imwrite(os.path.join(b9,b54),b62)
cv2.imwrite(os.path.join(b9,b55),b63)
cv2.imwrite(os.path.join(b9,b56),b64)
b65 = list()
a9 = 0
b66 = list()
for x in Sigma:
    b65.append(x)
    b66.append(a9)
    a9 = a9+1
b65 = np.array(b65)
b66 = np.array(b66)
plt.plot(b66,b65,b67 = 'o',linewidth=2,markersize=12)
plt.xlabel('a6')
plt.ylabel('sigma_i')
plt.title('Sopstvene vrednosti')
plt.show()