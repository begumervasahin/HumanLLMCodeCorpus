import knn
import b36
import gc
import numpy as np
if b1 = = '__main__':
    b2 = b36.b36()
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
    b14 = [
        ['b17', 'b18', 'b19', 'b13', 'b29', 'b33', 'b34',
         'b35', 'execution_time', 'b37']
    ]
    for b17 in b8:
        for get_knn_func, i1 in zip(b9, range(len(b9))):
            for get_label_func, i2 in zip(b11, range(len(b11))):
                for pca_parameter in b13:
                    b15 = []
                    print(b16 = b5)
                    print('******** Conditions ******', b16 = b5)
                    print('b17 = ', b17, b16=b5)
                    b15.append(b17)
                    print('b18 = ', b10[i1], b16=b5)
                    b15.append(b10[i1])
                    print('b19 = ', b12[i2], b16=b5)
                    b15.append(b12[i2])
                    print('b13 = ', pca_parameter, b16=b5)
                    b15.append(pca_parameter)
                    print('**************************', b16 = b5)
                    b20 = np.copy(train_samples)
                    b21 = np.copy(test_samples)
                    b22 = np.copy(b6)
                    b23 = np.copy(b7)
                    b24 = b36.b36()
                    result_labels, b25 = knn.get_test_samples_labels(
                        b17, b20, b22, b21, get_knn_func, get_label_func, pca_parameter
                    )
                    b26 = b36.b36()
                    b27 = b26 - b24
                    b29, b30, b31, F_1, b33, b34, b28 = knn.result_evaluate(
                        b23, result_labels
                    )
                    print('b29 = ', b29, b16=b5)
                    b15.append(b29)
                    print('b30 = ', b30, b16=b5)
                    print('b31 = ', b31, b16=b5)
                    print('b32 = ', F_1, b16=b5)
                    print('b33 = ', b33, b16=b5)
                    b15.append(b33)
                    print('b34 = ', b34, b16=b5)
                    b15.append(b34)
                    print('b35 = ', b28, b16=b5)
                    b15.append(b28)
                    print('execution b36 = ', b27, b16=b5)
                    b15.append(b27)
                    print('b37 = ', b25, b16=b5)
                    b15.append(b25)
                    print(b16 = b5)
                    b14.append(b15)
                    gc.collect()
    b38 = b36.b36()
    print('***********************', b16 = b5)
    print('Total b39 = ', b38 - b2, b16=b5)
    print('***********************', b16 = b5)
    b5.close()
    with open('result_table.csv', 'w') as outf:
        for ele in b14:
            b40 = [str(i) for i in ele]
            b41 = ', '.join(b40)
            print(b41, b16 = outf)