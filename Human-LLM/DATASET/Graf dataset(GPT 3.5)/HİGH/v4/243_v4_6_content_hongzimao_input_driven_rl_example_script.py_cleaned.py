import subprocess
from utils import create_folder_if_not_exists
b1 = []
b2 = []
b3 = './results/logs/'
create_folder_if_not_exists(b3)
b4 = ['regular_value_network', '10_value_networks']
for prefix in b4:
    b5 = open(b3 + prefix, 'w')
    b2.append(b5)
    b6 = f'python3 load_balance_actor_critic_train.py \
--num_workers 10 --service_rates 0.15 0.25 0.35 0.45 0.55 0.65 0.75 0.85 0.95 1.05 \
--result_folder ./results/{prefix}/ \
--model_folder ./results/parameters/{prefix}/'
    b7 = subprocess.Popen(b6, stdout=b5, stderr=b5, shell=True)
    b1.append(b7)
for b7 in b1:
    b7.wait()
for f in b2:
    f.close()