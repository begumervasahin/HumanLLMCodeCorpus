import knn
import time
import gc
import numpy as np
if __name__ == '__main__':
    experiment_start_time = time.time()
    train_directory = './digits/trainingDigits'
    test_directory = './digits/testDigits'
    result_file = open('result.txt', 'w')
    train_samples, train_labels = knn.load_sample_set(train_directory)
    test_samples, ground_truth_labels = knn.load_sample_set(test_directory)
    ks = [3, 5, 7, 9]
    knn_functions = [knn.get_knn_e_dist, knn.get_knn_e_dist_with_kdtree, knn.get_knn_m_dist]
    knn_functions_str = ['get_knn_e_dist', 'get_knn_e_dist_with_kdtree', 'get_knn_m_dist']
    label_functions = [knn.get_label_by_knn, knn.get_label_by_wknn]
    label_functions_str = ['get_label_by_knn', 'get_label_by_wknn']
    pca_parameters = [0, 4, 8, 16, 32, 64, 128, 256]
    results = [['k', 'get_knn_function', 'get_label_function', 'pca_parameters', 'accuracy', 'macro_precision', 'macro_recall', 'macro_F1', 'execution_time', 'dimension']]
    for k in ks:
        for knn_func, knn_func_str in zip(knn_functions, knn_functions_str):
            for label_func, label_func_str in zip(label_functions, label_functions_str):
                for pca_parameter in pca_parameters:
                    print('\n******** Conditions ******', file=result_file)
                    print(f'k = {k}', file=result_file)
                    print(f'get_knn_function = {knn_func_str}', file=result_file)
                    print(f'get_label_function = {label_func_str}', file=result_file)
                    print(f'pca_parameters = {pca_parameter}', file=result_file)
                    print('**************************', file=result_file)
                    train_set = np.copy(train_samples)
                    test_set = np.copy(test_samples)
                    train_labels_copy = np.copy(train_labels)
                    ground_truth_labels_copy = np.copy(ground_truth_labels)
                    start_time = time.time()
                    result_labels, dimension = knn.get_test_samples_labels(k, train_set, train_labels_copy, test_set, knn_func, label_func, pca_parameter)
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    accuracy, precision, recall, F1, macro_precision, macro_recall, macro_F1 = knn.result_evaluate(ground_truth_labels_copy, result_labels)
                    print(f'accuracy = {accuracy}', file=result_file)
                    print(f'macro_precision = {macro_precision}', file=result_file)
                    print(f'macro_recall = {macro_recall}', file=result_file)
                    print(f'macro_F1 = {macro_F1}', file=result_file)
                    print(f'execution time = {elapsed_time}', file=result_file)
                    print(f'dimension = {dimension}', file=result_file)
                    print('\n', file=result_file)
                    single_result = [k, knn_func_str, label_func_str, pca_parameter, accuracy, macro_precision, macro_recall, macro_F1, elapsed_time, dimension]
                    results.append(single_result)
                    gc.collect()
    experiment_end_time = time.time()
    total_time = experiment_end_time - experiment_start_time
    print('***********************', file=result_file)
    print(f'Total Time = {total_time}', file=result_file)
    print('***********************', file=result_file)
    result_file.close()
    with open('result_table.csv', 'w') as outf:
        for result in results:
            str_result = ', '.join(map(str, result))
            print(str_result, file=outf)