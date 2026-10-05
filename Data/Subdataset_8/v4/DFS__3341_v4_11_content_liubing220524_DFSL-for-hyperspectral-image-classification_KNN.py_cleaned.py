import time
import input_data
import numpy as np
import scipy.io as sio
from sklearn.neighbors import KNeighborsClassifier
import pickle
start_time = time.time()
num_labeled = 5
dataSet = input_data.read_data_sets('I_feature.h5', num_labeled)
train_data = dataSet.train.images
train_label = dataSet.train.labels
test_data = dataSet.test.images
test_label = dataSet.test.labels
print('Training...')
clf = KNeighborsClassifier(n_neighbors=1)
clf.fit(train_data, train_label)
training_score = clf.score(train_data, train_label)
testing_score = clf.score(test_data, test_label)
print('Training score: {:.2f}'.format(training_score))
print('Testing score: {:.2f}'.format(testing_score))
end_time = time.time()
elapsed_time = end_time - start_time
print('Time taken:', elapsed_time)
label_img = clf.predict(test_data)
with open('./gt_I.data', 'rb') as f:
    gt_index = pickle.load(f)
m, n = 145, 145
final_result = np.zeros((m, n), dtype=np.int8)
final_result = final_result.reshape(m * n)
final_result[gt_index] = label_img + 1
final_result = final_result.reshape(m, n)
sio.savemat('I-25.mat', {'final_result': final_result})