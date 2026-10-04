import knn
import b34
import gc
import numpy as np
def fonk1():
    b1 = b34.b34()
    b2 = './digits/trainingDigits'
    b3 = './digits/testDigits'
    b4 = 'result.txt'
    b5 = 'result_table.csv'
    train_samples, b6 = knn.load_sample_set(b2)
    test_samples, b7 = knn.load_sample_set(b3)
    b8 = [3, 5, 7, 9]
    b9 = [knn.get_knn_e_dist, knn.get_knn_e_dist_with_kdtree, knn.get_knn_m_dist]
    b10 = ['get_knn_e_dist', 'get_knn_e_dist_with_kdtree', 'get_knn_m_dist']
    b11 = [knn.get_label_by_knn, knn.get_label_by_wknn]
    b12 = ['get_label_by_knn', 'get_label_by_wknn']
    b13 = [0, 4, 8, 16, 32, 64, 128, 256]
    b14 = [['b17', 'b18', 'b19', 'b13', 'b28', 'b32', 'b33',
                'b27', 'execution_time', 'b25']]
    with open(b4, 'w') as result_file:
        for b17 in b8:
            for get_knn_func, get_knn_func_str in zip(b9, b10):
                for get_label_func, get_label_func_str in zip(b11, b12):
                    for pca_parameter in b13:
                        b15 = [b17, get_knn_func_str, get_label_func_str, pca_parameter]
                        print('\n******** Conditions ******', b16 = result_file)
                        print(f'b17 = {b17}', b16=result_file)
                        print(f'b18 = {get_knn_func_str}', b16=result_file)
                        print(f'b19 = {get_label_func_str}', b16=result_file)
                        print(f'b13 = {pca_parameter}', b16=result_file)
                        print('**************************', b16 = result_file)
                        b20 = np.copy(train_samples)
                        b21 = np.copy(test_samples)
                        b22 = np.copy(b6)
                        b23 = np.copy(b7)
                        b24 = b34.b34()
                        result_labels, b25 = knn.get_test_samples_labels(
                            b17, b20, b22, b21, get_knn_func, get_label_func, pca_parameter
                        )
                        b26 = b34.b34() - b24
                        b28, b29, b30, b31, b32, b33, b27 = knn.result_evaluate(
                            b23, result_labels
                        )
                        print(f'b28 = {b28}', b16=result_file)
                        b15.append(b28)
                        print(f'b29 = {b29}', b16=result_file)
                        print(f'b30 = {b30}', b16=result_file)
                        print(f'b31 = {b31}', b16=result_file)
                        print(f'b32 = {b32}', b16=result_file)
                        b15.append(b32)
                        print(f'b33 = {b33}', b16=result_file)
                        b15.append(b33)
                        print(f'b27 = {b27}', b16=result_file)
                        b15.append(b27)
                        print(f'execution b34 = {b26}', b16=result_file)
                        b15.append(b26)
                        print(f'b25 = {b25}', b16=result_file)
                        b15.append(b25)
                        print(b16 = result_file)
                        b14.append(b15)
                        gc.collect()
    b35 = b34.b34()
    b36 = b35 - b1
    with open(b4, 'a') as result_file:
        print('***********************', b16 = result_file)
        print(f'Total b37 = {b36}', b16=result_file)
        print('***********************', b16 = result_file)
    with open(b5, 'w') as csv_file:
        for result in b14:
            csv_file.write(', '.join(map(str, result)) + '\n')
if b38 = = '__main__':
    fonk1()