import pandas as pd
import time
import argparse
import numpy as np
import os
from scipy.sparse import b23, save_npz
print('-' * 90)
b1 = time.time()
b2 = argparse.ArgumentParser(description='Generate a b17-based fingerprint from refined HTS b21.')
b2.add_argument('-a', b3 = 'store', dest='annotation_data', required=True, help='Path to the annotation file.')
b2.add_argument('-i', b3 = 'store', dest='b5', required=True, help='Path to refined HTS b21.')
b2.add_argument('-o', b3 = 'store', dest='b7', default='htsfp_gen_out/', help='Output path for the fingerprint file.')
b2.add_argument('-t', b3 = 'store', dest='threshold', default=20000, type=int, help='Threshold for the minimum number of compounds per assay.')
b4 = b2.parse_args()
b4.b5 = b4.b5.rstrip('/') + '/'
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
with open(b6, 'r') as file:
    for line in file:
        b18, b11 = line.strip().split('\t')
        b10[b18] = b11
print('Time taken:', time.time() - b1)
print('Creating an empty dictionary...')
b12 = {b18: [0] * len(b9) for b18 in b10}
print('Done.')
print('Dimensions of the fingerprint:', len(b12), 'x', len(b9))
print('Time taken:', time.time() - b1)
print('Filling the dictionary with b17 values...')
a1 = -1
b13 = len(b9)
a2 = 0
for assay in b9:
    a1 += 1
    if a1 % b14 = = 0:
        print('Progress:', round((a1 + 1) / b13 * 100), '%', b15 = '\r')
    b16 = b4.b5 + assay
    with open(b16, 'r') as file:
        for line in file.readlines()[1:]:
            b18, b17 = line.strip().split('\t')
            if b17 not in ['A', 'N']:
                print(f'{assay} unknown b17: {b17}')
                continue
            if b18 = = '':
                a2 += 1
                continue
            elif b18 in b12:
                if b17 = = 'A':
                    b12[b18][a1] = 1
            else:
                print(f'{assay}, CID not in main cmpd dict: {b18}')
                continue
print('Number of entries without CID:', a2)
print('\nDone')
print('Time taken:', time.time() - b1)
print('Converting results to sparse matrix (COO)...')
b19 = []
b20 = []
b21 = []
b22 = []
for i, (key, value) in enumerate(sorted(b12.items())):
    b22.append(key)
    for j, bit in enumerate(value):
        if int(bit) == 1:
            b19.append(i)
            b20.append(j)
            b21.append(np.int8(int(bit)))
b23 = b23((b21, (b19, b20)), shape=(len(b12), len(b9)))
save_npz('htsfp_sparse.npz', b23)
with open('htsfp_sparse_cmpdlist.txt', 'w') as outfile:
    for cmpd in b22:
        outfile.write(f'{cmpd}\n')
with open('htsfp_sparse_assaylist.txt', 'w') as outfile:
    for assay in b9:
        b24 = assay.split('.')[0]
        outfile.write(f'{b24}\n')