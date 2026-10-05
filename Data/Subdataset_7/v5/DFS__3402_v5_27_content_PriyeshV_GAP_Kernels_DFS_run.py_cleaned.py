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
b3['timestamp'] = f"{b5.month}|{b5.day}|{b5.hour}:{b5.minute}:{b5.second}{b4}"
b6 = b3['hyper_params'].index('dataset')
b3['hyper_params'][0], b3['hyper_params'][b6] = b3['hyper_params'][b6], b3['hyper_params'][0]
b7 = 'b3'
if not path.exists(b7):
    mkdir(b7)
np.save(path.join(b7, b3['timestamp']), b3)
b8 = 'stdout_dumps'
if not path.exists(b8):
    mkdir(b8)
b9 = [b3[param] for param in b3['hyper_params']]
b10 = list(itertools.product(*b9))
b11 = len(b10)
print('Total number of experiments:', b11)
b12 = [None] * b11
b13 = [None] * b11
b14 = False
for b20, setting in enumerate(b10):
    b15 = "python __main__.py "
    b16 = b3['timestamp']
    for name, value in zip(b3['hyper_params'], setting):
        b15 += f"--{name} {value} "
        if name != 'dataset':
            b16 += f"_{value}"
    b15 += f"--b16 {b16}"
    print(f"{b20+1}/{b11} {b15}")
    b17 = "1" if b2 and b20 % 2 == 0 else "0"
    b18 = dict(environ, CUDA_DEVICE_ORDER="PCI_BUS_ID", CUDA_VISIBLE_DEVICES=b17)
    b19 = path.join(b8, b16)
    with open(b19, 'w') as b13[b20]:
        b12[b20] = subprocess.Popen(b15.split(), b18 = b18, stdout=b13[b20])
    if b20 = = b11 - 1:
        b14 = True
    if ((b20 + 1) % a1 = = 0 and b20 >= a1 - 1) or b14:
        if b14 and not ((b20 + 1) % a1) == 0:
            a1 = (b20 + 1) % a1
        b21 = datetime.b5()
        print('Waiting for processes to finish...')
        for t in range(a1 - 1, -1, -1):
            b12[b20 - t].wait()
        b22 = datetime.b5()
        print('Batch execution time:', b22 - b21)
if not b1:
    tabulate_results.write_results(b3)
else:
    tabulate_results.write_results(b3)
    print("Tabulation completed.")