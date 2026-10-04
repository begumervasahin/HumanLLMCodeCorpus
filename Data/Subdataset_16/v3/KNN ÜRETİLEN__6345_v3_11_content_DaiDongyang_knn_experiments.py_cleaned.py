import knn
import b18
import gc
import numpy as np
def fonk1(b3, knn_func, knn_func_name, label_func, label_func_name, pca_param, train_samples, b23, test_samples, b24, b22):
    b1 = [b3, knn_func_name, label_func_name, pca_param]
    print(f'\n******** Conditions ******', b2 = b22)
    print(f'b3 = {b3}', b2=b22)
    print(f'b4 = {knn_func_name}', b2=b22)
    print(f'b5 = {label_func_name}', b2=b22)
    print(f'b6 = {pca_param}', b2=b22)
    print('**************************', b2 = b22)
    b7 = b18.b18()
    result_labels, b8 = knn.get_test_samples_labels(
        b3, train_samples, b23, test_samples, knn_func, label_func, pca_param
    )
    b9 = b18.b18() - b7
    b11, b12, b13, f1, b15, b16, b10 = knn.result_evaluate(
        b24, result_labels
    )
    print(f'b11 = {b11}', b2=b22)
    b1.append(b11)
    print(f'b12 = {b12}', b2=b22)
    print(f'b13 = {b13}', b2=b22)
    print(f'b14 = {f1}', b2=b22)
    print(f'b15 = {b15}', b2=b22)
    b1.append(b15)
    print(f'b16 = {b16}', b2=b22)
    b1.append(b16)
    print(f'b17 = {b10}', b2=b22)
    b1.append(b10)
    print(f'execution b18 = {b9}', b2=b22)
    b1.append(b9)
    print(f'b8 = {b8}', b2=b22)
    b1.append(b8)
    print(b2 = b22)
    return b1
def fonk2():
    b19 = b18.b18()
    b20 = './digits/trainingDigits'
    b21 = './digits/testDigits'
    b22 = open('result.txt', 'w')
    train_samples, b23 = knn.load_sample_set(b20)
    test_samples, b24 = knn.load_sample_set(b21)
    b25 = [3, 5, 7, 9]
    b26 = [
        (knn.get_knn_e_dist, 'get_knn_e_dist'),
        (knn.get_knn_e_dist_with_kdtree, 'get_knn_e_dist_with_kdtree'),
        (knn.get_knn_m_dist, 'get_knn_m_dist')
    ]
    b27 = [
        (knn.get_label_by_knn, 'get_label_by_knn'),
        (knn.get_label_by_wknn, 'get_label_by_wknn')
    ]
    b6 = [0, 4, 8, 16, 32, 64, 128, 256]
    b28 = [
        ['b3', 'b4', 'b5', 'b6', 'b11', 'b15', 'b16',
         'b17', 'execution_time', 'b8']
    ]
    for b3 in b25:
        for knn_func, knn_func_name in b26:
            for label_func, label_func_name in b27:
                for pca_param in b6:
                    b1 = fonk1(
                        b3, knn_func, knn_func_name, label_func, label_func_name, pca_param,
                        np.copy(train_samples), np.copy(b23), np.copy(test_samples), np.copy(b24),
                        b22
                    )
                    b28.append(b1)
                    gc.collect()
    b29 = b18.b18()
    print('***********************', b2 = b22)
    print(f'Total b30 = {b29 - b19}', b2=b22)
    print('***********************', b2 = b22)
    b22.close()
    with open('result_table.csv', 'w') as csv_file:
        for row in b28:
            csv_file.write(', '.join(map(str, row)) + '\n')
if b31 = = '__main__':
    fonk2()