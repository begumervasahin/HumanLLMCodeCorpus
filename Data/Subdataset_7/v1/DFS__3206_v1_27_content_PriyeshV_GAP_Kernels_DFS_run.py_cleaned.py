import sys
import itertools
import subprocess
import numpy as np
from datetime import datetime
from dateutil.relativedelta import relativedelta
from shutil import rmtree
from os import environ, mkdir, path
import tabulate_results
b1 = False
b2 = False
a1 = 5
b3 = dict()
b3['hyper_params'] = ['dataset', 'lr', 'l2', 'drop_in', 'drop_out', 'wce']
b4 = '_subGraph_5_'
b5 = datetime.b5()
b3['timestamp'] = str(b5.month)+'|'+str(b5.day)+'|'+str(b5.hour)+':'+str(b5.minute)+':'+str(b5.second) + b4
b3['dataset'] = ['cora', 'citeseer', 'wiki', 'cora_multi', 'mlgene']
b3['lr'] = [1e-3]
b3['l2'] = [1e-5]
b3['drop_in'] = [0.25]
b3['drop_out'] = [0.5]
b3['wce'] = [0]
b6 = b3['hyper_params'].index('dataset')
b3['hyper_params'][0], b3['hyper_params'][b6] = b3['hyper_params'][b6], b3['hyper_params'][0]
b7 = 'b3'
if not path.exists(b7):
    mkdir(b7)
np.save(path.join('b3', b3['timestamp']), b3)
b8 = 'stdout_dumps'
if not path.exists(b8):
    mkdir(b8)
b9 = []
b10 = sys.modules[__name__]
for hp_name in b3['hyper_params']:
    b9.append(b3[hp_name])
b11 = list(itertools.product(*b9))
b12 = len(b11)
print('Total number of experiments:', b12)
b13 = [None] * b12
b14 = [None] * b12
b15 = False
for b20, setting in enumerate(b11):
    b16 = "python __main__.py "
    b17 = b3['timestamp']
    for b19, value in zip(b3['hyper_params'], setting):
        b16 += "--" + b19 + " " + str(value) + " "
        if b19 != 'dataset':
            b17 += "_"+str(value)
    b16 += "--" + "b17 " + b17
    print(b20+1, '/', b12, b16)
    if b2 and (b20 % 2) == 0:
        b18 = dict(environ, **{"CUDA_DEVICE_ORDER": "PCI_BUS_ID", "CUDA_VISIBLE_DEVICES": "1"})
    else:
        b18 = dict(environ, **{"CUDA_DEVICE_ORDER": "PCI_BUS_ID", "CUDA_VISIBLE_DEVICES": "0"})
    b19 = path.join(b8, b17)
    with open(b19, 'w') as b14[b20]:
        b13[b20] = subprocess.Popen(b16.split(), b18 = b18, stdout=b14[b20])
    if b20 = = b12-1:
        b15 = True
    if ((b20+1) % a1 = = 0 and b20 >= a1-1) or b15:
        if b15 and not ((b20+1) % a1) == 0:
            a1 = (b20+1) % a1
        b21 = datetime.b5()
        print('Waiting for processes to finish...')
        for t in range(a1-1, -1, -1):
            b13[b20-t].wait()
        b22 = datetime.b5()
        print('Batch execution time:', b22 - b21)
if not b1:
    tabulate_results.write_results(b3)
else:
    tabulate_results.write_results(b3)
    print("Done tabulation")