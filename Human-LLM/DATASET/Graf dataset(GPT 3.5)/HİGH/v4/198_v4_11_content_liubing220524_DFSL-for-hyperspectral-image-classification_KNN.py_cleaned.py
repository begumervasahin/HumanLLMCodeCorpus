import time
import input_data
import numpy as np
import scipy.io as sio
from sklearn.neighbors import KNeighborsClassifier
import pickle
b1 = time.time()
a1 = 5
b2 = input_data.read_data_sets('I_feature.h5', a1)
b3 = b2.train.images
b4 = b2.train.labels
b5 = b2.test.images
b6 = b2.test.labels
print('Training...')
b7 = KNeighborsClassifier(n_neighbors=1)
b7.fit(b3, b4)
b8 = b7.score(b3, b4)
b9 = b7.score(b5, b6)
print('Training score: {:.2f}'.format(b8))
print('Testing score: {:.2f}'.format(b9))
b10 = time.time()
b11 = b10 - b1
print('Time taken:', b11)
b12 = b7.predict(b5)
with open('./gt_I.data', 'rb') as f:
    b13 = pickle.load(f)
m, b14 = 145, 145
b15 = np.zeros((m, b14), dtype=np.int8)
b15 = b15.reshape(m * b14)
b15[b13] = b12 + 1
b15 = b15.reshape(m, b14)
sio.savemat('I-25.mat', {'b15': b15})