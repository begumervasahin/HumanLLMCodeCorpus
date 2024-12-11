import time
import numpy as np
import scipy.io as sio
from sklearn.neighbors import KNeighborsClassifier
import input_data
import pickle
def fonk1(file_path, a1):
    return input_data.read_data_sets(file_path, a1)
def fonk2(data, labels):
    b1 = KNeighborsClassifier(n_neighbors=1)
    b1.fit(data, labels)
    return b1
def fonk3(b8, b9):
    print('Training score: {:.2f}'.format(b8))
    print('Testing score: {:.2f}'.format(b9))
def fonk4(classifier, test_data):
    return classifier.predict(test_data)
def fonk5(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)
def fonk6(predictions, b12, m, b13):
    b2 = np.zeros((m, b13), dtype=np.int8).reshape(m * b13)
    b2[b12] = predictions + 1
    return b2.reshape(m, b13)
def fonk7(file_path, result):
    sio.savemat(file_path, {'b2': result})
if b3 = = "__main__":
    b4 = time.time()
    a1 = 5
    b5 = fonk1('I_feature.h5', a1)
    train_data, b6 = b5.train.images, b5.train.labels
    test_data, b7 = b5.test.images, b5.test.labels
    print('Training the KNN classifier...')
    b1 = fonk2(train_data, b6)
    b8 = b1.score(train_data, b6)
    b9 = b1.score(test_data, b7)
    fonk3(b8, b9)
    b10 = time.time() - b4
    print('Time taken:', b10)
    print('Predicting labels for test data...')
    b11 = fonk4(b1, test_data)
    print('Loading ground truth indices...')
    b12 = fonk5('./gt_I.data')
    m, b13 = 145, 145
    b2 = fonk6(b11, b12, m, b13)
    print('Saving the final result...')
    fonk7('I-25.mat', b2)