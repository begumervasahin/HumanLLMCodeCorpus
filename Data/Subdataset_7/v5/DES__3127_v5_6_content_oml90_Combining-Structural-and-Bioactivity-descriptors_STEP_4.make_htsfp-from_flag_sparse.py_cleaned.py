import pandas as pd
import time
import argparse
import numpy as np
import os
from scipy.sparse import coo_matrix, save_npz
print('-' * 90)
b1 = time.time()
b2 = argparse.ArgumentParser(description='Generate a flag-based fingerprint from refined HTS data.')
b2.add_argument('-a', b3 = 'store', dest='annotation_data', required=True, help='Path to the annotation file.')
b2.add_argument('-i', b3 = 'store', dest='b5', required=True, help='Path to refined HTS data.')
b2.add_argument('-o', b3 = 'store', dest='b7', default='htsfp_gen_out/', help='Output path for the fingerprint file.')
b2.add_argument('-t', b3 = 'store', dest='threshold', default=20000, type=int, help='Threshold for the minimum number of compounds per assay.')
b4 = b2.parse_args()
b4.b5 = b4.b5.rstrip('/') + '/'
b6 = 'C:/CESFP_project/CID2smi_pubchem.txt'
if not os.path.exists(b4.b7):
    os.makedirs(b4.b7)
b7 = os.path.join(b4.b7, f'htsfp_t{b4.threshold}')
print('Loading the annotation file...')
b8 = pd.read_csv(b4.annotation_data, sep='\t')
b9 = b8.loc[b8['count'] >= b4.threshold]['assay'].values
print(f'Number