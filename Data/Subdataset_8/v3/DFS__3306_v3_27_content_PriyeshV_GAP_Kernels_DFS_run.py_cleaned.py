import sys
import itertools
import subprocess
import numpy as np
from datetime import datetime
from os import path, environ, mkdir
import tabulate_results
get_results_only = False
switch_gpus = False
n_parallel_threads = 5
args = {
    'hyper_params': ['dataset', 'lr', 'l2', 'drop_in', 'drop_out', 'wce'],
    'dataset': ['cora', 'citeseer', 'wiki', 'cora_multi', 'mlgene'],
    'lr': [1e-3],
    'l2': [1e-5],
    'drop_in': [0.25],
    'drop_out': [0.5],
    'wce': [0]
}
custom = '_subGraph_5_'
now = datetime.now()
args['timestamp'] = f"{now.month}|{now.day}|{now.hour}:{now.minute}:{now.second}{custom}"
args_path = 'args'
if not path.exists(args_path):
    mkdir(args_path)
np.save(path.join(args_path, args['timestamp']), args)
stdout_dump_path = 'stdout_dumps'
if not path.exists(stdout_dump_path):
    mkdir(stdout_dump_path)
param_values = [args[hp_name] for hp_name in args['hyper_params']]
combinations = list(itertools.product(*param_values))
n_combinations = len(combinations)
print('Total number of experiments:', n_combinations)
pids = [None] * n_combinations
f = [None] * n_combinations
last_process = False
for i, setting in enumerate(combinations):
    command = "python __main__.py "
    folder_suffix = args['timestamp']
    for name, value in zip(args['hyper_params'], setting):
        command += f"--{name} {value} "
        if name != 'dataset':
            folder_suffix += f"_{value}"
    command += f"--folder_suffix {folder_suffix}"
    print(f"{i+1}/{n_combinations} {command}")
    cuda_device = "1" if switch_gpus and i % 2 == 0 else "0"
    env = dict(environ, CUDA_DEVICE_ORDER="PCI_BUS_ID", CUDA_VISIBLE_DEVICES=cuda_device)
    name = path.join(stdout_dump_path, folder_suffix)
    with open(name, 'w') as f[i]:
        pids[i] = subprocess.Popen(command.split(), env=env, stdout=f[i])
    if i == n_combinations - 1:
        last_process = True
    if ((i + 1) % n_parallel_threads == 0 and i >= n_parallel_threads - 1) or last_process:
        if last_process and not ((i + 1) % n_parallel_threads) == 0:
            n_parallel_threads = (i + 1) % n_parallel_threads
        start = datetime.now()
        print('Waiting for processes to finish...')
        for t in range(n_parallel_threads - 1, -1, -1):
            pids[i - t].wait()
        end = datetime.now()
        print('Batch execution time:', end - start)
if not get_results_only:
    tabulate_results.write_results(args)
else:
    tabulate_results.write_results(args)
    print("Done tabulation")