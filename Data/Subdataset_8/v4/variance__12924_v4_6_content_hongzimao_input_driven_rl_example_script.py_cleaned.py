import subprocess
from utils import create_folder_if_not_exists
procs = []
log_files = []
log_path = './results/logs/'
create_folder_if_not_exists(log_path)
prefixes = ['regular_value_network', '10_value_networks']
for prefix in prefixes:
    log_file = open(log_path + prefix, 'w')
    log_files.append(log_file)
    command = f'python3 load_balance_actor_critic_train.py \
--num_workers 10 --service_rates 0.15 0.25 0.35 0.45 0.55 0.65 0.75 0.85 0.95 1.05 \
--result_folder ./results/{prefix}/ \
--model_folder ./results/parameters/{prefix}/'
    p = subprocess.Popen(command, stdout=log_file, stderr=log_file, shell=True)
    procs.append(p)
for p in procs:
    p.wait()
for f in log_files:
    f.close()