import knn
import time
import gc
import numpy as np
if __name__ == '__main__':
    experiment_start_time = time.time()
    train_dir = './digits/trainingDigits'
    test_dir = './digits/testDigits'
    with open('result.txt', 'w') as result_file:
        train_samples, train_labels = knn.load_sample_set(train_dir)
        test_samples, ground_labels = knn.load_sample_set(test_dir)
        ks = [3, 5, 7, 9]
        knn_functions = [knn.get_knn_e_dist, knn.get_knn_e_dist_with_kdtree, knn.get_knn_m_dist]
        knn_functions_names = ['get_knn_e_dist', 'get_knn_e_dist_with_kdtree', 'get_knn_m_dist']
        label_functions = [knn.get_label_by_knn, knn.get_label_by_wknn]
        label_functions_names = ['get_label_by_knn', 'get_label_by_wknn']
        pca_parameters = [0, 4, 8, 16, 32, 64, 128, 256]
        results = [['k', 'get_knn_function', 'get_label_function', 'pca_parameters', 'accuracy', 'macro_precision',
                    'macro_recall', 'macro_F1', 'execution_time', 'dimension']]
        for k in ks:
            for knn_func, knn_func_name in zip(knn_functions, knn_functions_names):
                for label_func, label_func_name in zip(label_functions, label_functions_names):
                    for pca_parameter in pca_parameters:
                        single_result = []
                        print('\n******** Conditions ******', file=result_file)
                        print(f'k = {k}', file=result_file)
                        single_result.append(k)
                        print(f'get_knn_function = {knn_func_name}', file=result_file)
                        single_result.append(knn_func_name)
                        print(f'get_label_function = {label_func_name}', file=result_file)
                        single_result.append(label_func_name)
                        print(f'pca_parameters = {pca_parameter}', file=result_file)
                        single_result.append(pca_parameter)
                        print('**************************', file=result_file)
                        train_set = np.copy(train_samples)
                        test_set = np.copy(test_samples)
                        train_labels_copy = np.copy(train_labels)
                        ground_labels_copy = np.copy(ground_labels)
                        start_time = time.time()
                        result_labels, dimension = knn.get_test_samples_labels(k, train_set, train_labels_copy,
                                                                                test_set, knn_func, label_func,
                                                                                pca_parameter)
                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        accuracy, macro_precision, macro_recall, macro_F1 = knn.result_evaluate(ground_labels_copy, result_labels)
                        single_result.extend([accuracy, macro_precision, macro_recall, macro_F1, elapsed_time, dimension])
                        print(f'accuracy = {accuracy}', file=result_file)
                        print(f'macro_precision = {macro_precision}', file=result_file)
                        print(f'macro_recall = {macro_recall}', file=result_file)
                        print(f'macro_F1 = {macro_F1}', file=result_file)
                        print(f'execution_time = {elapsed_time}', file=result_file)
                        print(f'dimension = {dimension}', file=result_file)
                        results.append(single_result)
                        gc.collect()
        experiment_end_time = time.time()
        print('\n***********************', file=result_file)
        print(f'Total Time = {experiment_end_time - experiment_start_time}', file=result_file)
        print('***********************', file=result_file)
    result_file.close()
    with open('result_table.csv', 'w') as outf:
        for record in results:
            record_str = ', '.join(map(str, record))
            print(record_str, file=outf)