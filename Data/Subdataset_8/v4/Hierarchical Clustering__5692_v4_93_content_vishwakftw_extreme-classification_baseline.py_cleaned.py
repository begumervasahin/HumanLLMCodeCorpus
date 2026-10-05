from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import os
import yaml
import numpy as np
from extreme_classification.loaders import LibSVMLoader
from extreme_classification.metrics import precision_at_k, ndcg_score_at_k
print("Baseline metrics using random prediction")
parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument('--data_root', type=str, required=True,
                    help=)
parser.add_argument('--dataset_info', type=str, required=True,
                    help='Dataset information in YAML format')
args = parser.parse_args()
with open(args.dataset_info, 'r') as yaml_file:
    dset_opts = yaml.safe_load(yaml_file)
train_file_path = os.path.join(args.data_root, dset_opts['train_filename'])
train_loader = LibSVMLoader(train_file_path, dset_opts['train_opts'])
test_file_path = os.path.join(args.data_root, dset_opts['test_filename'])
test_loader = LibSVMLoader(test_file_path, dset_opts['test_opts'])
actual_train_labels = train_loader.get_classes().toarray()
actual_test_labels = test_loader.get_classes().toarray()
predicted_train_labels = np.random.randint(2, size=actual_train_labels.shape)
predicted_test_labels = np.random.randint(2, size=actual_test_labels.shape)
for k in [1, 3, 5]:
    train_precision_at_k = [precision_at_k(actual_train_labels[i], predicted_train_labels[i], k)
                            for i in range(len(predicted_train_labels))]
    train_ndcg_at_k = [ndcg_score_at_k(actual_train_labels[i], predicted_train_labels[i], k)
                       for i in range(len(predicted_train_labels))]
    test_precision_at_k = [precision_at_k(actual_test_labels[i], predicted_test_labels[i], k)
                           for i in range(len(predicted_test_labels))]
    test_ndcg_at_k = [ndcg_score_at_k(actual_test_labels[i], predicted_test_labels[i], k)
                      for i in range(len(predicted_test_labels))]
    print("Train: P@{} = {}, NDCG@{} = {}".format(k, np.mean(train_precision_at_k), k,
                                                  np.mean(train_ndcg_at_k)))
    print("Test: P@{} = {}, NDCG@{} = {}".format(k, np.mean(test_precision_at_k), k,
                                                 np.mean(test_ndcg_at_k)))