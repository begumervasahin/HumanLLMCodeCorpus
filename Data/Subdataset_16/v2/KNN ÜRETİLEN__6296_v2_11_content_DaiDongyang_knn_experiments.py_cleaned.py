import knn
import b32
import gc
import numpy as np
def fonk1():
    b1 = b32.b32()
    b2 = './digits/trainingDigits'
    b3 = './digits/testDigits'
    b4 = open('result.txt', 'w')
    train_samples, b5 = knn.load_sample_set(b2)
    test_samples, b6 = knn.load_sample_set(b3)
    b7 = [3, 5, 7, 9]
    b8 = [
        (knn.get_knn_e_dist, 'get_knn_e_dist'),
        (knn.get_knn_e_dist_with_kdtree, 'get_knn_e_dist_with_kdtree'),
        (knn.get_knn_m_dist, 'get_knn_m_dist')
    ]
    b9 = [
        (knn.get_label_by_knn, 'get_label_by_knn'),
        (knn.get_label_by_wknn, 'get_label_by_wknn')
    ]
    b10 = [0, 4, 8, 16, 32, 64, 128, 256]
    b11 = [
        ['b14', 'b15', 'b16', 'b10', 'b25', 'b29', 'b30',
         'b31', 'execution_time', 'b22']
    ]
    for b14 in b7:
        for get_knn_func, knn_func_name in b8:
            for get_label_func, label_func_name in b9:
                for pca_param in b10:
                    b12 = []
                    print(b13 = b4)
                    print('******** Conditions ******', b13 = b4)
                    print(f'b14 = {b14}', b13=b4)
                    b12.append(b14)
                    print(f'b15 = {knn_func_name}', b13=b4)
                    b12.append(knn_func_name)
                    print(f'b16 = {label_func_name}', b13=b4)
                    b12.append(label_func_name)
                    print(f'b10 = {pca_param}', b13=b4)
                    b12.append(pca_param)
                    print('**************************', b13 = b4)
                    b17 = np.copy(train_samples)
                    b18 = np.copy(test_samples)
                    b19 = np.copy(b5)
                    b20 = np.copy(b6)
                    b21 = b32.b32()
                    result_labels, b22 = knn.get_test_samples_labels(
                        b14, b17, b19, b18, get_knn_func, get_label_func, pca_param
                    )
                    b23 = b32.b32() - b21
                    b25, b26, b27, f1, b29, b30, b24 = knn.result_evaluate(
                        b20, result_labels
                    )
                    print(f'b25 = {b25}', b13=b4)
                    b12.append(b25)
                    print(f'b26 = {b26}', b13=b4)
                    print(f'b27 = {b27}', b13=b4)
                    print(f'b28 = {f1}', b13=b4)
                    print(f'b29 = {b29}', b13=b4)
                    b12.append(b29)
                    print(f'b30 = {b30}', b13=b4)
                    b12.append(b30)
                    print(f'b31 = {b24}', b13=b4)
                    b12.append(b24)
                    print(f'execution b32 = {b23}', b13=b4)
                    b12.append(b23)
                    print(f'b22 = {b22}', b13=b4)
                    b12.append(b22)
                    print(b13 = b4)
                    b11.append(b12)
                    gc.collect()
    b33 = b32.b32()
    print('***********************', b13 = b4)
    print(f'Total b34 = {b33 - b1}', b13=b4)
    print('***********************', b13 = b4)
    b4.close()
    with open('result_table.csv', 'w') as csv_file:
        for row in b11:
            csv_file.write(', '.join(map(str, row)) + '\n')
if b35 = = '__main__':
    fonk1()