import os
import yaml
import numpy as np
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from extreme_classification.loaders import LibSVMLoader
from extreme_classification.metrics import precision_at_k, ndcg_score_at_k
def load_dataset_info(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
def load_data(data_root, dataset_info):
    train_file = os.path.join(data_root, dataset_info['train_filename'])
    test_file = os.path.join(data_root, dataset_info['test_filename'])
    train_loader = LibSVMLoader(train_file, dataset_info['train_opts'])
    test_loader = LibSVMLoader(test_file, dataset_info['test_opts'])
    actual_train_y = train_loader.get_classes().toarray()
    actual_test_y = test_loader.get_classes().toarray()
    return actual_train_y, actual_test_y
def generate_random_predictions(shape):
    return np.random.randint(2, size=shape)
def evaluate_metrics(actual_y, pred_y, k_values):
    metrics = {}
    for K in k_values:
        p_at_k = [precision_at_k(actual_y[i], pred_y[i], K) for i in range(len(pred_y))]
        ndcg_at_k = [ndcg_score_at_k(actual_y[i], pred_y[i], K) for i in range(len(pred_y))]
        metrics[K] = {
            'precision': np.mean(p_at_k),
            'ndcg': np.mean(ndcg_at_k)
        }
    return metrics
def print_metrics(metrics, label):
    for K, values in metrics.items():
        print(f"{label}: P@{K} = {values['precision']:.4f}, NDCG@{K} = {values['ndcg']:.4f}")
def main():
    print("Baseline metrics using random prediction")
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('--data_root', type=str, required=True, help="Root folder for dataset.")
    parser.add_argument('--dataset_info', type=str, required=True, help="Dataset information in YAML format")
    args = parser.parse_args()
    dataset_info = load_dataset_info(args.dataset_info)
    actual_train_y, actual_test_y = load_data(args.data_root, dataset_info)
    pred_train_y = generate_random_predictions(actual_train_y.shape)
    pred_test_y = generate_random_predictions(actual_test_y.shape)
    k_values = [1, 3, 5]
    train_metrics = evaluate_metrics(actual_train_y, pred_train_y, k_values)
    test_metrics = evaluate_metrics(actual_test_y, pred_test_y, k_values)
    print_metrics(train_metrics, "Train")
    print_metrics(test_metrics, "Test")
if __name__ == "__main__":
    main()