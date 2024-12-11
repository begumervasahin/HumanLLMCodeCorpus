import time
import numpy as np
import scipy.io as sio
from sklearn.neighbors import KNeighborsClassifier
import input_data
import pickle
b1 = time.time()
a1 = 5
b2 = input_data.read_data_sets('I_feature.h5', a1)
b3 = b2.train.images
b4 = b2.train.labels
b5 = b2.test.images
b6 = b2.test.labels
print('Train...')
b7 = KNeighborsClassifier(n_neighbors=1)
b7.fit(b3, b4)
print('Training score: %f' % b7.score(b3, b4))
print('Testing score: %f' % b7.score(b5, b6))
b8 = time.time()
print('Time taken:', b8 - b1)
b9 = b7.predict(b5)
with open('./gt_I.data', 'rb') as f:
    b10 = pickle.load(f)
a2 = 145
a3 = 145
b11 = np.zeros((a2, a3), dtype=np.int8)
b11 = b11.reshape(a2 * a3)
b11[b10] = b9 + 1
b11 = b11.reshape(a2, a3)
sio.savemat('I-25.mat', {'b11': b11})