import knn
import b31
import gc
import numpy as np
if b1 = = '__main__':
    b2 = b31.b31()
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
    b14 = [['b16', 'b17', 'b18', 'b13', 'b28', 'b29', 'b30', 'b27', 'execution_time', 'b24']]
    for b16 in b8:
        for knn_func, knn_func_str in zip(b9, b10):
            for label_func, label_func_str in zip(b11, b12):
                for pca_parameter in b13:
                    print('\n******** Conditions ******', b15 = b5)
                    print(f'b16 = {b16}', b15=b5)
                    print(f'b17 = {knn_func_str}', b15=b5)
                    print(f'b18 = {label_func_str}', b15=b5)
                    print(f'b13 = {pca_parameter}', b15=b5)
                    print('**************************', b15 = b5)
                    b19 = np.copy(train_samples)
                    b20 = np.copy(test_samples)
                    b21 = np.copy(b6)
                    b22 = np.copy(b7)
                    b23 = b31.b31()
                    result_labels, b24 = knn.get_test_samples_labels(b16, b19, b21, b20, knn_func, label_func, pca_parameter)
                    b25 = b31.b31()
                    b26 = b25 - b23
                    b28, precision, recall, F1, b29, b30, b27 = knn.result_evaluate(b22, result_labels)
                    print(f'b28 = {b28}', b15=b5)
                    print(f'b29 = {b29}', b15=b5)
                    print(f'b30 = {b30}', b15=b5)
                    print(f'b27 = {b27}', b15=b5)
                    print(f'execution b31 = {b26}', b15=b5)
                    print(f'b24 = {b24}', b15=b5)
                    print('\n', b15 = b5)
                    b32 = [b16, knn_func_str, label_func_str, pca_parameter, b28, b29, b30, b27, b26, b24]
                    b14.append(b32)
                    gc.collect()
    b33 = b31.b31()
    b34 = b33 - b2
    print('***********************', b15 = b5)
    print(f'Total b35 = {b34}', b15=b5)
    print('***********************', b15 = b5)
    b5.close()
    with open('result_table.csv', 'w') as outf:
        for result in b14:
            b36 = ', '.join(map(str, result))
            print(b36, b15 = outf)