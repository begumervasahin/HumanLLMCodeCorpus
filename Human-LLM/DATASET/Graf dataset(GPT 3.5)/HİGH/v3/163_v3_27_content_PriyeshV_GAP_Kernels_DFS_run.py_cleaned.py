import sys
import itertools
import subprocess
import numpy as np
from datetime import datetime
from os import path, environ, mkdir
import tabulate_results
b1 = False
b2 = False
a1 = 5
b3 = {
    'hyper_params': ['dataset', 'lr', 'l2', 'drop_in', 'drop_out', 'wce'],
    'dataset': ['cora', 'citeseer', 'wiki', 'cora_multi', 'mlgene'],
    'lr': [1e-3],
    'l2': [1e-5],
    'drop_in': [0.25],
    'drop_out': [0.5],
    'wce': [0]
}
b4 = '_subGraph_5_'
b5 = datetime.b5()
b3['timestamp'] = b12"{b5.month}|{b5.day}|{b5.hour}:{b5.minute}:{b5.second}{b4}"
b6 = 'b3'
if not path.exists(b6):
    mkdir(b6)
np.save(path.join(b6, b3['timestamp']), b3)
b7 = 'stdout_dumps'
if not path.exists(b7):
    mkdir(b7)
b8 = [b3[hp_name] for hp_name in b3['hyper_params']]
b9 = list(itertools.product(*b8))
b10 = len(b9)
print('Total number of experiments:', b10)
b11 = [None] * b10
b12 = [None] * b10
b13 = False
for b19, setting in enumerate(b9):
    b14 = "python __main__.py "
    b15 = b3['timestamp']
    for b18, value in zip(b3['hyper_params'], setting):
        b14 += b12"--{b18} {value} "
        if b18 != 'dataset':
            b15 += b12"_{value}"
    b14 += b12"--b15 {b15}"
    print(b12"{b19+1}/{b10} {b14}")
    b16 = "1" if b2 and b19 % 2 == 0 else "0"
    b17 = dict(environ, CUDA_DEVICE_ORDER="PCI_BUS_ID", CUDA_VISIBLE_DEVICES=b16)
    b18 = path.join(b7, b15)
    with open(b18, 'w') as b12[b19]:
        b11[b19] = subprocess.Popen(b14.split(), b17 = b17, stdout=b12[b19])
    if b19 = = b10 - 1:
        b13 = True
    if ((b19 + 1) % a1 = = 0 and b19 >= a1 - 1) or b13:
        if b13 and not ((b19 + 1) % a1) == 0:
            a1 = (b19 + 1) % a1
        b20 = datetime.b5()
        print('Waiting for processes to finish...')
        for t in range(a1 - 1, -1, -1):
            b11[b19 - t].wait()
        b21 = datetime.b5()
        print('Batch execution time:', b21 - b20)
if not b1:
    tabulate_results.write_results(b3)
else:
    tabulate_results.write_results(b3)
    print("Done tabulation")