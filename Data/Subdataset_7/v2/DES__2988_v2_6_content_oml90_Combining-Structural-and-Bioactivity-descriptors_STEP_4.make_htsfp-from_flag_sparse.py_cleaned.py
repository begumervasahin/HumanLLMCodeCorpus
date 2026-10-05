import pandas as pd
import time
import argparse
import numpy as np
import os
from scipy.sparse import coo_matrix, save_npz
print('-' * 90)
b1 = time.time()
b2 = argparse.ArgumentParser(description='This script generates a b19-based fingerprint from refined HTS data.')
b2.add_argument('-a', b3 = 'store', dest='annotation_data', required=True, help='Path to the annotation file.')
b2.add_argument('-i', b3 = 'store', dest='b5', required=True, help='Path to the refined HTS data.')
b2.add_argument('-o', b3 = 'store', dest='b7', default='htsfp_gen_out/', help='Optional: Set the output path for the fingerprint file.')
b2.add_argument('-t', b3 = 'store', dest='threshold', default=20000, type=int, help='Optional: Threshold for the minimum number of compounds per assay.')
b4 = b2.parse_args()
if b4.b5[-1] != '/':
    b4.b5 = b4.b5 + '/'
b6 = 'C:/CESFP_project/CID2smi_pubchem.txt'
if not os.path.exists(b4.b7):
    os.makedirs(b4.b7)
b7 = b4.b7 + 'htsfp_t' + str(b4.threshold)
print('Loading the annotation file...')
b8 = pd.read_csv(b4.annotation_data, sep='\t')
b9 = b8.loc[b8['count'] >= b4.threshold]['assay'].values
print('Number of assays containing at least', b4.threshold, 'assays:', len(b9))
print('Time taken:', time.time() - b1)
print('Loading the CID to SMILES file...')
b10 = {}
with open(b6, 'r') as f:
    for line in f:
        b11 = line.strip().split('\t')
        b10[b11[0]] = b11[1]
print('Time taken:', time.time() - b1)
print('Creating an empty dictionary...')
b12 = {}
for cmpd in b10:
    b12[cmpd] = [0] * len(b9)
print('Done.')
print('Dimensions of the fingerprint:', len(b12), 'x', len(b9))
print('Time taken:', time.time() - b1)
print('Filling the dictionary with b19 values...')
a1 = -1
b13 = len(b9)
a2 = 0
for assay in b9:
    a1 += 1
    if a1 % b14 = = 0:
        print('Progress:', round((a1 + 1) / b13 * 100), '%', b15 = '\r')
    b16 = b4.b5 + assay
    with open(b16, 'r') as f:
        a3 = 0
        for line in f:
            a3 += 1
            if a3 = = 1:
                continue
            b17 = line.strip().split('\t')
            b18 = b17[0]
            b19 = b17[1]
            if b19 not in ['A', 'N']:
                pass
print('Time taken:', time.time() - b1)