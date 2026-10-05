import subprocess
import os
def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
log_path = './results/logs/'
create_folder_if_not_exists(log_path)
prefixes = ['regular_value_network', '10_value_networks']
procs = []
for prefix in prefixes:
    log_file_path = os.path.join(log_path, prefix)
    with open(log_file_path, 'w') as log_file:
        if prefix == 'regular_value_network':
            command = (
                'python3 load_balance_actor_critic_train.py '
                '--num_workers 10 '
                '--service_rates 0.15 0.25 0.35 0.45 0.55 0.65 0.75 0.85 0.95 1.05 '
                f'--result_folder ./results/{prefix}/ '
                f'--model_folder ./results/parameters/{prefix}/'
            )
        elif prefix == '10_value_networks':
            command = (
                'python3 load_balance_actor_multi_critic_train.py '
                '--num_workers 10 '
                '--service_rates 0.15 0.25 0.35 0.45 0.55 0.65 0.75 0.85 0.95 1.05 '
                f'--result_folder ./results/{prefix}/ '
                f'--model_folder ./results/parameters/{prefix}/'
            )
        p = subprocess.Popen(command, stdout=log_file, stderr=log_file, shell=True)
        procs.append(p)
for p in procs:
    p.wait()