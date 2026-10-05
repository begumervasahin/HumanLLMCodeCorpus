import knn
import b29
import gc
import numpy as np
def fonk1(result_file, b2, knn_func_str, label_func_str, pca_parameter):
    print('\n******** Conditions ******', b1 = result_file)
    print(f'b2 = {b2}', b1=result_file)
    print(f'b3 = {knn_func_str}', b1=result_file)
    print(f'b4 = {label_func_str}', b1=result_file)
    print(f'b5 = {pca_parameter}', b1=result_file)
    print('**************************', b1 = result_file)
def fonk2():
    b6 = b29.b29()
    b7 = './digits/trainingDigits'
    b8 = './digits/testDigits'
    with open('result.txt', 'w') as result_file:
        train_samples, b9 = knn.load_sample_set(b7)
        test_samples, b10 = knn.load_sample_set(b8)
        b11 = [3, 5, 7, 9]
        b12 = [knn.get_knn_e_dist, knn.get_knn_e_dist_with_kdtree, knn.get_knn_m_dist]
        b13 = ['get_knn_e_dist', 'get_knn_e_dist_with_kdtree', 'get_knn_m_dist']
        b14 = [knn.get_label_by_knn, knn.get_label_by_wknn]
        b15 = ['get_label_by_knn', 'get_label_by_wknn']
        b5 = [0, 4, 8, 16, 32, 64, 128, 256]
        b16 = [['b2', 'b3', 'b4', 'b5', 'b26', 'b27', 'b28', 'b25', 'execution_time', 'b22']]
        for b2 in b11:
            for knn_func, knn_func_str in zip(b12, b13):
                for label_func, label_func_str in zip(b14, b15):
                    for pca_parameter in b5:
                        fonk1(result_file, b2, knn_func_str, label_func_str, pca_parameter)
                        b17 = np.copy(train_samples)
                        b18 = np.copy(test_samples)
                        b19 = np.copy(b9)
                        b20 = np.copy(b10)
                        b21 = b29.b29()
                        result_labels, b22 = knn.get_test_samples_labels(b2, b17, b19, b18, knn_func, label_func, pca_parameter)
                        b23 = b29.b29()
                        b24 = b23 - b21
                        b26, precision, recall, F1, b27, b28, b25 = knn.result_evaluate(b20, result_labels)
                        print(f'b26 = {b26}', b1=result_file)
                        print(f'b27 = {b27}', b1=result_file)
                        print(f'b28 = {b28}', b1=result_file)
                        print(f'b25 = {b25}', b1=result_file)
                        print(f'execution b29 = {b24}', b1=result_file)
                        print(f'b22 = {b22}', b1=result_file)
                        print('\n', b1 = result_file)
                        b30 = [b2, knn_func_str, label_func_str, pca_parameter, b26, b27, b28, b25, b24, b22]
                        b16.append(b30)
                        gc.collect()
        b31 = b29.b29()
        b32 = b31 - b6
        print('***********************', b1 = result_file)
        print(f'Total b33 = {b32}', b1=result_file)
        print('***********************', b1 = result_file)
    with open('result_table.csv', 'w') as outf:
        for result in b16:
            b34 = ', '.join(map(str, result))
            print(b34, b1 = outf)
if b35 = = '__main__':
    fonk2()