import knn
import time
import gc
import numpy as np
if b1 = = '__main__':
    b2 = time.time()
    b3 = './digits/trainingDigits'
    b4 = './digits/testDigits'
    with open('result.txt', 'w') as result_file:
        train_samples, b5 = knn.load_sample_set(b3)
        test_samples, b6 = knn.load_sample_set(b4)
        b7 = [3, 5, 7, 9]
        b8 = [knn.get_knn_e_dist, knn.get_knn_e_dist_with_kdtree, knn.get_knn_m_dist]
        b9 = ['get_knn_e_dist', 'get_knn_e_dist_with_kdtree', 'get_knn_m_dist']
        b10 = [knn.get_label_by_knn, knn.get_label_by_wknn]
        b11 = ['get_label_by_knn', 'get_label_by_wknn']
        b12 = [0, 4, 8, 16, 32, 64, 128, 256]
        b13 = [['b16', 'b17', 'b18', 'b12', 'b28', 'b29',
                    'b30', 'b27', 'b31', 'b24']]
        for b16 in b7:
            for knn_func, knn_func_name in zip(b8, b9):
                for label_func, label_func_name in zip(b10, b11):
                    for pca_parameter in b12:
                        b14 = []
                        print('\n******** Conditions ******', b15 = result_file)
                        print(f'b16 = {b16}', b15=result_file)
                        b14.append(b16)
                        print(f'b17 = {knn_func_name}', b15=result_file)
                        b14.append(knn_func_name)
                        print(f'b18 = {label_func_name}', b15=result_file)
                        b14.append(label_func_name)
                        print(f'b12 = {pca_parameter}', b15=result_file)
                        b14.append(pca_parameter)
                        print('**************************', b15 = result_file)
                        b19 = np.copy(train_samples)
                        b20 = np.copy(test_samples)
                        b21 = np.copy(b5)
                        b22 = np.copy(b6)
                        b23 = time.time()
                        result_labels, b24 = knn.get_test_samples_labels(b16, b19, b21,
                                                                                b20, knn_func, label_func,
                                                                                pca_parameter)
                        b25 = time.time()
                        b26 = b25 - b23
                        b28, b29, b30, b27 = knn.result_evaluate(b22, result_labels)
                        b14.extend([b28, b29, b30, b27, b26, b24])
                        print(f'b28 = {b28}', b15=result_file)
                        print(f'b29 = {b29}', b15=result_file)
                        print(f'b30 = {b30}', b15=result_file)
                        print(f'b27 = {b27}', b15=result_file)
                        print(f'b31 = {b26}', b15=result_file)
                        print(f'b24 = {b24}', b15=result_file)
                        b13.append(b14)
                        gc.collect()
        b32 = time.time()
        print('\n***********************', b15 = result_file)
        print(f'Total b33 = {b32 - b2}', b15=result_file)
        print('***********************', b15 = result_file)
    result_file.close()
    with open('result_table.csv', 'w') as outf:
        for record in b13:
            b34 = ', '.join(map(str, record))
            print(b34, b15 = outf)