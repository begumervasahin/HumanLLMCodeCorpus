import knn
import time
import gc
import numpy as np
if b1 = = '__main__':
    b2 = time.time()
    b3 = './digits/trainingDigits'
    b4 = './digits/testDigits'
    b5 = open('result.txt', 'w')
    train_samples, b6 = knn.load_sample_set(b3)
    test_samples, b7 = knn.load_sample_set(b4)
    b8 = [3, 5, 7, 9]
    b9 = [knn.get_knn_e_dist, knn.get_knn_e_dist_with_kdtree, knn.get_knn_m_dist]
    b10 = ['get_knn_e_dist', 'get_knn_e_dist_with_kdtree', 'get_knn_m_dist']
    b11 = [knn.get_label_by_knn, knn.get_label_by_wknn]
    b12 = ['get_label_by_knn', 'get_label_by_wknn']
    b13 = [0, 4, 8, 16, 32, 64, 128, 256]
    b14 = [['b17', 'b18', 'b19', 'b13', 'b29', 'b30',
                'b31', 'b28', 'b32', 'b25']]
    for b17 in b8:
        for i1, (get_knn_func, knn_func_str) in enumerate(zip(b9, b10)):
            for i2, (get_label_func, label_func_str) in enumerate(zip(b11, b12)):
                for pca_parameter in b13:
                    b15 = []
                    print('\n******** Conditions ******', b16 = b5)
                    print('b17 = ', b17, b16=b5)
                    b15.append(b17)
                    print('b18 = ', knn_func_str, b16=b5)
                    b15.append(knn_func_str)
                    print('b19 = ', label_func_str, b16=b5)
                    b15.append(label_func_str)
                    print('b13 = ', pca_parameter, b16=b5)
                    b15.append(pca_parameter)
                    print('**************************', b16 = b5)
                    b20 = np.copy(train_samples)
                    b21 = np.copy(test_samples)
                    b22 = np.copy(b6)
                    b23 = np.copy(b7)
                    b24 = time.time()
                    result_labels, b25 = knn.get_test_samples_labels(b17, b20, b22,
                                                                            b21, get_knn_func, get_label_func,
                                                                            pca_parameter)
                    b26 = time.time()
                    b27 = b26 - b24
                    b29, precision, recall, F1, b30, b31, b28 = knn.result_evaluate(
                        b23, result_labels)
                    b15.extend([b29, b30, b31, b28, b27, b25])
                    print('b29 = ', b29, b16=b5)
                    print('b30 = ', b30, b16=b5)
                    print('b31 = ', b31, b16=b5)
                    print('b28 = ', b28, b16=b5)
                    print('b32 = ', b27, b16=b5)
                    print('b25 = ', b25, b16=b5)
                    b14.append(b15)
                    gc.collect()
    b33 = time.time()
    print('\n***********************', b16 = b5)
    print('Total b34 = ', b33 - b2, b16=b5)
    print('***********************', b16 = b5)
    b5.close()
    with open('result_table.csv', 'w') as outf:
        for ele in b14:
            b35 = ', '.join(map(str, ele))
            print(b35, b16 = outf)