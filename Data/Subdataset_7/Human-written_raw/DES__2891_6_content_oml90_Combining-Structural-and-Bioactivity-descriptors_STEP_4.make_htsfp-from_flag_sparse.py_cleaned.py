
import pandas as pd
import time
import argparse
import numpy as np
import os
from scipy.sparse import coo_matrix, save_npz
print('---'*30)
b1 = time.time()
b2 = argparse.ArgumentParser(description='Takes refined hts b22 and generates a b18 based fingerprint')
b2.add_argument('-a', b3 = "store", dest='annotation_data', required=True, help='Path to annotation file')
b2.add_argument('-i', b3 = "store", dest='b5', required=True, help='Path to refined hts b22')
b2.add_argument('-o', b3 = "store", dest='b7', default='htsfp_gen_out/' , help='Optional: set output path for fingerprint file')
b2.add_argument('-t', b3 = "store", dest='threshold', default=20000, type=int, help='Optional: threshold for minimum number of compounds per assay')
b4 = b2.parse_args()
if b4.b5[-1] != '/':
    b4.b5 = b4.b5+'/'
b6 = 'C:/CESFP_project/CID2smi_pubchem.txt'
if not os.path.exists(b4.b7):
    os.makedirs(b4.b7)
b7 = b4.b7+'htsfp_t'+str(b4.threshold)
print('loading annotation file...')
b8 = pd.read_csv(b4.annotation_data, sep='\t')
b9 = b8.loc[b8['count']>=b4.threshold]['assay'].values
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
    b12[cmpd] = [0]*len(b9)
print('done.')
print('dimensions of htsfp:\t{} x {}'.format(len(b12),len(b9)))
print(time.time() - b1)
print('Filling dict with b18 values...')
a1 = -1
b13 = len(b9)
a2 = 0
for assay in b9:
    a1 += 1
    if a1 % b14 = = 0: print('... {}%'.format(round((a1+1)/b13*100),0), b19='\r')
    b15 = b4.b5+assay
    with open(b15, 'r') as f:
        a3 = 0
        for line in f:
            a3 += 1
            if a3 = = 1: continue
            b16 = line.strip().split('\t')
            b17 = b16[0]
            b18 = b16[1]
            if b18 not in ['A','N']: print('{} unknown b18: {}'.format(assay, b18), b19 = '\n'); continue
            if b17 = = '': a2 += 1; continue
            elif b17 in b12:
                if b18 = = 'A': b12[b17][a1] = 1
            else:
                print('{}, CID not in main cmpd dict: {}'.format(assay, b17))
                continue
print('number of entries without CID: {}'.format(a2))
print('\ndone')
print(time.time() - b1)
print('converting results to sparse matrix (coo)...')
b20 = []
b21 = []
b22 = []
b23 = []
for i,(key,value) in enumerate(sorted(b12.items())):
    b23.append(key)
    for a3, bit in enumerate(value):
        if int(bit)==1:
            b20.append(i)
            b21.append(a3)
            b22.append(np.int8(int(bit)))
b24 = coo_matrix((b22, (b20, b21)), shape=(len(b12), len(b9)))
save_npz('htsfp_sparse.npz',b24)
with open('htsfp_sparse_cmpdlist.txt','w') as outf:
    for cmpd in b23:
        outf.write('{}\n'.format(cmpd))
with open('htsfp_sparse_assaylist.txt','w') as outf:
    for assay in b9:
        b25 = assay.split('.')[0]
        outf.write("{}\n".format(b25))