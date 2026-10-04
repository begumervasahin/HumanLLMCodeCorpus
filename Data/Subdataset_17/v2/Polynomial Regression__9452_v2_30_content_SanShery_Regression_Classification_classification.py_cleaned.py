from __future__ import division, print_function
import numpy as np
import bm_classify as sol
import argparse
import sys
import time
def accuracy_score(true, preds):
    return np.sum(true == preds).astype(float) / len(true)
def run_binary():
    from data_loader import toy_data_binary, moon_dataset, data_loader_mnist
    datasets = [
        (toy_data_binary(), 'Synthetic data'),
        (moon_dataset(), 'Two Moon data'),
        (data_loader_mnist(), 'Binarized MNIST data')
    ]
    for data, name in datasets:
        print(name)
        X_train, X_test, y_train, y_test = data
        if name == 'Binarized MNIST data':
            y_train = np.asarray([0 if yi < 5 else 1 for yi in y_train])
            y_test = np.asarray([0 if yi < 5 else 1 for yi in y_test])
        for loss_type in ["perceptron", "logistic"]:
            w, b = sol.binary_train(X_train, y_train, loss=loss_type)
            train_preds = sol.binary_predict(X_train, w, b, loss=loss_type)
            test_preds = sol.binary_predict(X_test, w, b, loss=loss_type)
            print(f'{loss_type} train acc: {accuracy_score(y_train, train_preds):.6f}, test acc: {accuracy_score(y_test, test_preds):.6f}')
        print()
def run_multiclass():
    from data_loader import smile_dataset_clear, smile_dataset_blur, data_loader_mnist
    datasets = [
        (smile_dataset_clear(), 'Clear smile data', 3),
        (smile_dataset_blur(), 'Blur smile data', 3),
        (data_loader_mnist(), 'MNIST', 10)
    ]
    for data, name, num_classes in datasets:
        print(f'{name}: {num_classes} class classification')
        X_train, X_test, y_train, y_test = data
        for gd_type in ["sgd", "gd"]:
            start_time = time.time()
            w, b = sol.multiclass_train(X_train, y_train, C=num_classes, gd_type=gd_type)
            elapsed_time = time.time() - start_time
            train_preds = sol.multiclass_predict(X_train, w=w, b=b)
            test_preds = sol.multiclass_predict(X_test, w=w, b=b)
            print(f'{gd_type} training time: {elapsed_time:.6f} seconds')
            print(f'train acc: {accuracy_score(y_train, train_preds):.6f}, test acc: {accuracy_score(y_test, test_preds):.6f}')
        print()
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", choices=['binary', 'multiclass'], help="Specify the type of classification to run")
    parser.add_argument("--output", help="Specify the output file to write the results")
    args = parser.parse_args()
    if args.output:
        sys.stdout = open(args.output, 'w')
    if not args.type or args.type == 'binary':
        run_binary()
    if not args.type or args.type == 'multiclass':
        run_multiclass()
if __name__ == '__main__':
    main()