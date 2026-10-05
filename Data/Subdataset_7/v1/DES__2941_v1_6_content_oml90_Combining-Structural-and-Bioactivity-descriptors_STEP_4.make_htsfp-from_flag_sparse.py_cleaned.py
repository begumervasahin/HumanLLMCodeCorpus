import pandas as pd
import time
import argparse
import numpy as np
import os
from scipy.sparse import coo_matrix, save_npz
print('---'*30)
b1 = time.time()
b2 = argparse.ArgumentParser(description='Takes refined hts data and generates a b19 based fingerprint')
b2.add_argument('-a', b3 = "store", dest='annotation_data', required=True, help='Path to annotation file')
b2.add_argument('-i', b3 = "store", dest='b5', required=True, help='Path to refined hts data')
b2.add_argument('-o', b3 = "store", dest='b7', default='htsfp_gen_out/', help='Optional: set output path for fingerprint file')
b2.add_argument('-t', b3 = "store", dest='threshold', default=20000, type=int, help='Optional: threshold for minimum number of compounds per assay')
b4 = b2.parse_args()
if b4.b5[-1] != '/':
    b4.b5 = b4.b5 + '/'
b6 = 'C:/CESFP_project/CID2smi_pubchem.txt'
if not os.path.exists(b4.b7):
    os.makedirs(b4.b7)
b7 = b4.b7 + 'htsfp_t' + str(b4.threshold)
print('loading annotation file...')
b8 = pd.read_csv(b4.annotation_data, sep='\t')
b9 = b8.loc[b8['count'] >= b4.threshold]['assay'].values
print('Number of assays containing at least', b4.threshold, 'Assays:', len(b9))
print(time.time() - b1)
print('loading CID 2 smiles file...')
b10 = {}
with open(b6, 'r') as f:
    for line in f:
        b11 = line.strip().split('\t')
        b10[b11[0]] = b11[1]
print(time.time() - b1)
print('Creating empty dict...')
b12 = {}
for cmpd in b10:
    b12[cmpd] = [0] * len(b9)
print('done.')
print('dimensions of htsfp:\t{} x {}'.format(len(b12), len(b9)))
print(time.time() - b1)
print('Filling dict with b19 values...')
a1 = -1
b13 = len(b9)
a2 = 0
for assay in b9:
    a1 += 1
    if a1 % b14 = = 0:
        print('... {}%'.format(round((a1 + 1) / b13 * 100), 0), b15 = '\r')
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
            if b19 not in ['A', 'N