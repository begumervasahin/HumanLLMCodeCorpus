import b36
import gc
import numpy as np
import knn
def fonk1():
    b1 = b36.b36()
    b2 = './digits/trainingDigits'
    b3 = './digits/testDigits'
    b4 = 'result.txt'
    b5 = 'result_table.csv'
    train_samples, b6 = knn.load_sample_set(b2)
    test_samples, b7 = knn.load_sample_set(b3)
    b8 = [3, 5, 7, 9]
    b9 = [
        (knn.get_knn_e_dist, 'get_knn_e_dist'),
        (knn.get_knn_e_dist_with_kdtree, 'get_knn_e_dist_with_kdtree'),
        (knn.get_knn_m_dist, 'get_knn_m_dist')
    ]
    b10 = [
        (knn.get_label_by_knn, 'get_label_by_knn'),
        (knn.get_label_by_wknn, 'get_label_by_wknn')
    ]
    b11 = [0, 4, 8, 16, 32, 64, 128, 256]
    b12 = [
        ['b23', 'b24', 'b25', 'b26', 'b30',
         'b34', 'b35', 'b19', 'execution_time', 'b16']
    ]
    with open(b4, 'w') as result_file:
        for b23 in b8:
            for knn_func, knn_func_str in b9:
                for label_func, label_func_str in b10:
                    for b26 in b11:
                        b13 = [b23, knn_func_str, label_func_str, b26]
                        fonk2(result_file, b23, knn_func_str, label_func_str, b26)
                        b27, b28, b29, b14 = fonk3(
                            train_samples, b6, test_samples, b7
                        )
                        b15 = b36.b36()
                        result_labels, b16 = knn.get_test_samples_labels(
                            b23, b27, b29, b28, knn_func, label_func, b26
                        )
                        b17 = b36.b36() - b15
                        b18 = knn.result_evaluate(b14, result_labels)
                        b30, b34, b35, b19 = b18[:4]
                        fonk4(result_file, b30, b18, b17, b16)
                        b13.extend([b30, b34, b35, b19, b17, b16])
                        b12.append(b13)
                        gc.collect()
    b20 = b36.b36() - b1
    with open(b4, 'a') as result_file:
        print('***********************', b21 = result_file)
        print(f'Total b22 = {b20}', b21=result_file)
        print('***********************', b21 = result_file)
    fonk5(b5, b12)
def fonk2(result_file, b23, knn_func_str, label_func_str, b26):
    print('\n******** Conditions ******', b21 = result_file)
    print(f'b23 = {b23}', b21=result_file)
    print(f'b24 = {knn_func_str}', b21=result_file)
    print(f'b25 = {label_func_str}', b21=result_file)
    print(f'b26 = {b26}', b21=result_file)
    print('**************************', b21 = result_file)
def fonk3(train_samples, b6, test_samples, b7):
    b27 = np.copy(train_samples)
    b28 = np.copy(test_samples)
    b29 = np.copy(b6)
    b14 = np.copy(b7)
    return b27, b28, b29, b14
def fonk4(result_file, b30, b18, b17, b16):
    b31, b32, b33, b34, b35, b19 = b18[1:]
    print(f'b30 = {b30}', b21=result_file)
    print(f'b31 = {b31}', b21=result_file)
    print(f'b32 = {b32}', b21=result_file)
    print(f'b33 = {b33}', b21=result_file)
    print(f'b34 = {b34}', b21=result_file)
    print(f'b35 = {b35}', b21=result_file)
    print(f'b19 = {b19}', b21=result_file)
    print(f'execution b36 = {b17}', b21=result_file)
    print(f'b16 = {b16}', b21=result_file)
    print(b21 = result_file)
def fonk5(b5, b12):
    with open(b5, 'w') as csv_file:
        for result in b12:
            csv_file.write(', '.join(map(str, result)) + '\n')
if b37 = = '__main__':
    fonk1()