import pandas as pd
import time
import argparse
import numpy as np
import os
from scipy.sparse import coo_matrix, save_npz
print('-' * 90)
start_time = time.time()
parser = argparse.ArgumentParser(description='Generate a flag-based fingerprint from refined HTS data.')
parser.add_argument('-a', action='store', dest='annotation_data', required=True, help='Path to the annotation file.')
parser.add_argument('-i', action='store', dest='hts_data', required=True, help='Path to refined HTS data.')
parser.add_argument('-o', action='store', dest='outpath', default='htsfp_gen_out/', help='Output path for the fingerprint file.')
parser.add_argument('-t', action='store', dest='threshold', default=20000, type=int, help='Threshold for the minimum number of compounds per assay.')
args = parser.parse_args()
args.hts_data = args.hts_data.rstrip('/') + '/'
cid2smi_file = 'C:/CESFP_project/CID2smi_pubchem.txt'
if not os.path.exists(args.outpath):
    os.makedirs(args.outpath)
outpath = args.outpath + 'htsfp_t' + str(args.threshold)
print('Loading the annotation file...')
stats_df = pd.read_csv(args.annotation_data, sep='\t')
assay_selection = stats_df.loc[stats_df['count'] >= args.threshold]['assay'].values
print('Number of assays containing at least', args.threshold, 'assays:', len(assay_selection))
print('Time taken:', time.time() - start_time)
print('Loading the CID to SMILES file...')
cid2smi = {}
with open(cid2smi_file, 'r') as file:
    for line in file:
        cid, smi = line.strip().split('\t')
        cid2smi[cid] = smi
print('Time taken:', time.time() - start_time)
print('Creating an empty dictionary...')
main_cmpd_dict = {cid: [0] * len(assay_selection) for cid in cid2smi}
print('Done.')
print('Dimensions of the fingerprint:', len(main_cmpd_dict), 'x', len(assay_selection))
print('Time taken:', time.time() - start_time)
print('Filling the dictionary with flag values...')
idx = -1
Alength = len(assay_selection)
miss_cid = 0
for assay in assay_selection:
    idx += 1
    if idx % 10 == 0:
        print('Progress:', round((idx + 1) / Alength * 100), '%', end='\r')
    assay_file = args.hts_data + assay
    with open(assay_file, 'r') as file:
        for line in file.readlines()[1:]:
            cid, flag = line.strip().split('\t')
            if flag not in ['A', 'N']:
                print(f'{assay} unknown flag: {flag}')
                continue
            if cid == '':
                miss_cid += 1
                continue
            elif cid in main_cmpd_dict:
                if flag == 'A':
                    main_cmpd_dict[cid][idx] = 1
            else:
                print(f'{assay}, CID not in main cmpd dict: {cid}')
                continue
print('Number of entries without CID:', miss_cid)
print('\nDone')
print('Time taken:', time.time() - start_time)
print('Converting results to sparse matrix (COO)...')
row = []
col = []
data = []
cmpd_list = []
for i, (key, value) in enumerate(sorted(main_cmpd_dict.items())):
    cmpd_list.append(key)
    for j, bit in enumerate(value):
        if int(bit) == 1:
            row.append(i)
            col.append(j)
            data.append(np.int8(int(bit)))
coo_matrix = coo_matrix((data, (row, col)), shape=(len(main_cmpd_dict), len(assay_selection)))
save_npz('htsfp_sparse.npz', coo_matrix)
with open('htsfp_sparse_cmpdlist.txt', 'w') as outfile:
    for cmpd in cmpd_list:
        outfile.write(f'{cmpd}\n')
with open('htsfp_sparse_assaylist.txt', 'w') as outfile:
    for assay in assay_selection:
        assay_id = assay.split('.')[0]
        outfile.write(f'{assay_id}\n')