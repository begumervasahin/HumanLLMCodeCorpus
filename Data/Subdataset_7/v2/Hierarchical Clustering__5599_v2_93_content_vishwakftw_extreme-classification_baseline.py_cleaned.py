from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import os
import yaml
import numpy as np
from extreme_classification.loaders import LibSVMLoader
from extreme_classification.metrics import precision_at_k, ndcg_score_at_k
print("Baseline metrics using random prediction")
b1 = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
b1.add_argument('--data_root', b2 = str, required=True,
                    b3 = )
b1.add_argument('--dataset_info', b2 = str, required=True,
                    b3 = 'Dataset information in YAML format')
b4 = b1.parse_args()
with open(b4.dataset_info, 'r') as yaml_file:
    b5 = yaml.safe_load(yaml_file)
b6 = os.path.join(b4.data_root, b5['train_filename'])
b7 = LibSVMLoader(b6, b5['train_opts'])
b8 = os.path.join(b4.data_root, b5['test_filename'])
b9 = LibSVMLoader(b8, b5['test_opts'])
b10 = b7.get_classes().toarray()
b11 = b9.get_classes().toarray()
b12 = np.random.randint(2, size=b10.shape)
b13 = np.random.randint(2, size=b11.shape)
for K in [1, 3, 5]:
    b14 = [precision_at_k(b10[i], b12[i], K)
                    for i in range(len(b12))]
    b15 = [ndcg_score_at_k(b10[i], b12[i], K)
                       for i in range(len(b12))]
    b16 = [precision_at_k(b11[i], b13[i], K)
                   for i in range(len(b13))]
    b17 = [ndcg_score_at_k(b11[i], b13[i], K)
                      for i in range(len(b13))]
    print("Train: P@{} = {}, NDCG@{} = {}".format(K, np.mean(b14), K,
                                                  np.mean(b15)))
    print("Test: P@{} = {}, NDCG@{} = {}".format(K, np.mean(b16), K,
                                                 np.mean(b17)))