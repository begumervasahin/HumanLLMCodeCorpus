from __future__ import division, print_function
import numpy as np
import bm_classify as sol
import argparse
import sys
import time
from data_loader import (
    toy_data_binary,
    moon_dataset,
    data_loader_mnist,
    smile_dataset_clear,
    smile_dataset_blur
)
def accuracy_score(true, preds):
    return np.sum(true == preds).astype(float) / len(true)
def load_datasets():
    binary_datasets = [
        (toy_data_binary(), 'Synthetic data'),
        (moon_dataset(), 'Two Moon data'),
        (data_loader_mnist(), 'Binarized MNIST data')
    ]
    multiclass_datasets = [
        (smile_dataset_clear(), 'Clear smile data', 3),
        (smile_dataset_blur(), 'Blur smile data', 3),
        (data_loader_mnist(), 'MNIST', 10)
    ]
    return binary_datasets, multiclass_datasets
def preprocess_mnist_labels(y_train, y_test):
    y_train = np.asarray([0 if yi < 5 else 1 for yi in y_train])
    y_test = np.asarray([0 if yi < 5 else 1 for yi in y_test])
    return y_train, y_test
def run_binary():
    binary_datasets, _ = load_datasets()
    for data, name in binary_datasets:
        print(name)
        X_train, X_test, y_train, y_test = data
        if name == 'Binarized MNIST data':
            y_train, y_test = preprocess_mnist_labels(y_train, y_test)
        for loss_type in ["perceptron", "logistic"]:
            w, b = sol.binary_train(X_train, y_train, loss=loss_type)
            train_preds = sol.binary_predict(X_train, w, b, loss=loss_type)
            test_preds = sol.binary_predict(X_test, w, b, loss=loss_type)
            train_acc = accuracy_score(y_train, train_preds)
            test_acc = accuracy_score(y_test, test_preds)
            print(f"{loss_type} train acc: {train_acc:.6f}, test acc: {test_acc:.6f}")
        print()
def run_multiclass():
    _, multiclass_datasets = load_datasets()
    for data, name, num_classes in multiclass_datasets:
        print(f'{name}: {num_classes} class classification')
        X_train, X_test, y_train, y_test = data
        for gd_type in ["sgd", "gd"]:
            start_time = time.time()
            w, b = sol.multiclass_train(X_train, y_train, C=num_classes, gd_type=gd_type)
            training_time = time.time() - start_time
            train_preds = sol.multiclass_predict(X_train, w=w, b=b)
            test_preds = sol.multiclass_predict(X_test, w=w, b=b)
            train_acc = accuracy_score(y_train, train_preds)
            test_acc = accuracy_score(y_test, test_preds)
            print(f"{gd_type} training time: {training_time:.6f} seconds")
            print(f"train acc: {train_acc:.6f}, test acc: {test_acc:.6f}")
        print()
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", choices=['binary', 'multiclass'], help="Type of classification to run")
    parser.add_argument("--output", help="Output file to write results to")
    args = parser.parse_args()
    if args.output:
        sys.stdout = open(args.output, 'w')
    if not args.type or args.type == 'binary':
        run_binary()
    if not args.type or args.type == 'multiclass':
        run_multiclass()
if __name__ == '__main__':
    main()