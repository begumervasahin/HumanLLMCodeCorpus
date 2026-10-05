import pandas as pd
import time
import argparse
import numpy as np
import os
from scipy.sparse import coo_matrix, save_npz
print('-' * 90)
start = time.time()
ap = argparse.ArgumentParser(description='This script generates a flag-based fingerprint from refined HTS data.')
ap.add_argument('-a', action='store', dest='annotation_data', required=True, help='Path to the annotation file.')
ap.add_argument('-i', action='store', dest='hts_data', required=True, help='Path to the refined HTS data.')
ap.add_argument('-o', action='store', dest='outpath', default='htsfp_gen_out/', help='Optional: Set the output path for the fingerprint file.')
ap.add_argument('-t', action='store', dest='threshold', default=20000, type=int, help='Optional: Threshold for the minimum number of compounds per assay.')
args = ap.parse_args()
if args.hts_data[-1] != '/':
    args.hts_data = args.hts_data + '/'
cid2smi_file = 'C:/CESFP_project/CID2smi_pubchem.txt'
if not os.path.exists(args.outpath):
    os.makedirs(args.outpath)
outpath = args.outpath + 'htsfp_t' + str(args.threshold)
print('Loading the annotation file...')
statsdf = pd.read_csv(args.annotation_data, sep='\t')
assay_selection = statsdf.loc[statsdf['count'] >= args.threshold]['assay'].values
print('Number of assays containing at least', args.threshold, 'assays:', len(assay_selection))
print('Time taken:', time.time() - start)
print('Loading the CID to SMILES file...')
cid2smi = {}
with open(cid2smi_file, 'r') as f:
    for line in f:
        linels = line.strip().split('\t')
        cid2smi[linels[0]] = linels[1]
print('Time taken:', time.time() - start)
print('Creating an empty dictionary...')
main_cmpd_dict = {}
for cmpd in cid2smi:
    main_cmpd_dict[cmpd] = [0] * len(assay_selection)
print('Done.')
print('Dimensions of the fingerprint:', len(main_cmpd_dict), 'x', len(assay_selection))
print('Time taken:', time.time() - start)
print('Filling the dictionary with flag values...')
idx = -1
Alength = len(assay_selection)
miss_cid = 0
for assay in assay_selection:
    idx += 1
    if idx % 10 == 0:
        print('Progress:', round((idx + 1) / Alength * 100), '%', end='\r')
    assay_file = args.hts_data + assay
    with open(assay_file, 'r') as f:
        j = 0
        for line in f:
            j += 1
            if j == 1:
                continue
            line_list = line.strip().split('\t')
            Cid = line_list[0]
            flag = line_list[1]
            if flag not in ['A', 'N']:
                pass
print('Time taken:', time.time() - start)