import subprocess
import os
def fonk1(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
b1 = './results/logs/'
fonk1(b1)
b2 = ['regular_value_network', '10_value_networks']
b3 = []
for b5 in b2:
    b4 = os.path.join(b1, b5)
    with open(b4, 'w') as log_file:
        if b5 = = 'regular_value_network':
            b6 = (
                'python3 load_balance_actor_critic_train.py '
                '--num_workers 10 '
                '--service_rates 0.15 0.25 0.35 0.45 0.55 0.65 0.75 0.85 0.95 1.05 '
                f'--result_folder ./results/{b5}/ '
                f'--model_folder ./results/parameters/{b5}/'
            )
        elif b5 = = '10_value_networks':
            b6 = (
                'python3 load_balance_actor_multi_critic_train.py '
                '--num_workers 10 '
                '--service_rates 0.15 0.25 0.35 0.45 0.55 0.65 0.75 0.85 0.95 1.05 '
                f'--result_folder ./results/{b5}/ '
                f'--model_folder ./results/parameters/{b5}/'
            )
        b7 = subprocess.Popen(b6, stdout=log_file, stderr=log_file, shell=True)
        b3.append(b7)
for b7 in b3:
    b7.wait()