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
train_file = os.path.join(args.data_root, dset_opts['train_filename'])
train_loader = LibSVMLoader(train_file, dset_opts['train_opts'])
test_file = os.path.join(args.data_root, dset_opts['test_filename'])
test_loader = LibSVMLoader(test_file, dset_opts['test_opts'])
actual_train_y = train_loader.get_classes().toarray()
actual_test_y = test_loader.get_classes().toarray()
pred_train_y = np.random.randint(2, size=actual_train_y.shape)
pred_test_y = np.random.randint(2, size=actual_test_y.shape)
for K in [1, 3, 5]:
    train_p_at_k = [precision_at_k(actual_train_y[i], pred_train_y[i], K)
                    for i in range(len(pred_train_y))]
    train_ndcg_at_k = [ndcg_score_at_k(actual_train_y[i], pred_train_y[i], K)
                       for i in range(len(pred_train_y))]
    test_p_at_k = [precision_at_k(actual_test_y[i], pred_test_y[i], K)
                   for i in range(len(pred_test_y))]
    test_ndcg_at_k = [ndcg_score_at_k(actual_test_y[i], pred_test_y[i], K)
                      for i in range(len(pred_test_y))]
    print("Train: P@{} = {}, NDCG@{} = {}".format(K, np.mean(train_p_at_k), K,
                                                  np.mean(train_ndcg_at_k)))
    print("Test: P@{} = {}, NDCG@{} = {}".format(K, np.mean(test_p_at_k), K,
                                                 np.mean(test_ndcg_at_k)))