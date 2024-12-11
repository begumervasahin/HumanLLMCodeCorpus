
import time
import input_data
import numpy as np
import scipy.io as sio
import time
b1 = time.time()
a1 = 5
b2 = input_data.read_data_sets('I_feature.h5',a1)
b3 = b2.train.images
b4 = b2.train.labels
b5 = b2.test.images
b6 = b2.test.labels
print 'train.......'
from sklearn import neighbors
b7 = neighbors.KNeighborsClassifier(n_neighbors=1)
b7.fit(b3,b4)
print('training score:%b10'%b7.score(b3,b4))
print('testing score:%b10'%b7.score(b5,b6))
b8 = time.time()
print(b8-b1)
b9 = b7.predict(b5)
import pickle
b10 = open('./gt_I.data','rb')
b11 = pickle.load(b10)
b10.close()
a2 = 145
a3 = 145
b12 = np.zeros((a2,a3),dtype=np.int8)
b12 = b12.reshape(a2*a3)
b12[b11]=b9+1
b12 = b12.reshape(a2,a3)
sio.savemat('I-25.mat',{'b12':b12})