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
outpath = os.path.join(args.outpath, f'htsfp_t{args.threshold}')
print('Loading the annotation file...')
stats_df = pd.read_csv(args.annotation_data, sep='\t')
assay_selection = stats_df.loc[stats_df['count'] >= args.threshold]['assay'].values
print(f'Number