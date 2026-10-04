import os
import yaml
import numpy as np
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from extreme_classification.loaders import LibSVMLoader
from extreme_classification.b8 import precision_at_k, ndcg_score_at_k
def fonk1(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
def fonk2(data_root, b15):
    b1 = os.path.join(data_root, b15['train_filename'])
    b2 = os.path.join(data_root, b15['test_filename'])
    b3 = LibSVMLoader(b1, b15['train_opts'])
    b4 = LibSVMLoader(b2, b15['test_opts'])
    b5 = b3.get_classes().toarray()
    b6 = b4.get_classes().toarray()
    return b5, b6
def fonk3(shape):
    return np.random.randint(2, b7 = shape)
def fonk4(actual_y, pred_y, b18):
    b8 = {}
    for K in b18:
        b9 = [precision_at_k(actual_y[i], pred_y[i], K) for i in range(len(pred_y))]
        b10 = [ndcg_score_at_k(actual_y[i], pred_y[i], K) for i in range(len(pred_y))]
        b8[K] = {
            'precision': np.mean(b9),
            'ndcg': np.mean(b10)
        }
    return b8
def fonk5(b8, label):
    for K, values in b8.items():
        print(f"{label}: P@{K} = {values['precision']:.4f}, NDCG@{K} = {values['ndcg']:.4f}")
def fonk6():
    print("Baseline b8 using random prediction")
    b11 = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    b11.add_argument('--data_root', b12 = str, required=True,
                        b13 = "Root folder for dataset. The root folder should contain files either ending with test / train.")
    b11.add_argument('--b15', b12 = str, required=True, b13="Dataset information in YAML format")
    b14 = b11.parse_args()
    b15 = fonk1(b14.b15)
    b5, b6 = fonk2(b14.data_root, b15)
    b16 = fonk3(b5.shape)
    b17 = fonk3(b6.shape)
    b18 = [1, 3, 5]
    b19 = fonk4(b5, b16, b18)
    b20 = fonk4(b6, b17, b18)
    fonk5(b19, "Train")
    fonk5(b20, "Test")
if b21 = = "__main__":
    fonk6()