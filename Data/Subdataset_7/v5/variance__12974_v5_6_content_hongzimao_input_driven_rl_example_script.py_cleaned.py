import subprocess
from utils import create_folder_if_not_exists
def fonk1(b8):
    b1 = []
    b2 = []
    b3 = './results/logs/'
    create_folder_if_not_exists(b3)
    for prefix in b8:
        b4 = open(f'{b3}{prefix}', 'w')
        b2.append(b4)
        b5 = fonk2(prefix)
        b6 = subprocess.Popen(b5, stdout=b4, stderr=b4, shell=True)
        b1.append(b6)
    fonk3(b1)
    fonk4(b2)
def fonk2(prefix):
    return f'python3 load_balance_actor_critic_train.py \
--num_workers 10 --service_rates 0.15 0.25 0.35 0.45 0.55 0.65 0.75 0.85 0.95 1.05 \
--result_folder ./results/{prefix}/ \
--model_folder ./results/parameters/{prefix}/'
def fonk3(processes):
    for process in processes:
        process.wait()
def fonk4(b2):
    for b4 in b2:
        b4.close()
if b7 = = "__main__":
    b8 = ['regular_value_network', '10_value_networks']
    fonk1(b8)