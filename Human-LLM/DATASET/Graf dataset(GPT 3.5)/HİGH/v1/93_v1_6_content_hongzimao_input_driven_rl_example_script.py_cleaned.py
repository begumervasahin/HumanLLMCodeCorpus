import subprocess
import os
def fonk1(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
b1 = []
b2 = []
b3 = './results/logs/'
fonk1(b3)
b4 = ['regular_value_network', '10_value_networks']
for b6 in b4:
    b5 = open(os.path.join(b3, b6), 'w')
    b2.append(b5)
    if b6 = = 'regular_value_network':
        b7 = 'python3 load_balance_actor_critic_train.py ' + \
                  '--num_workers 10 --service_rates 0.15 0.25 0.35 0.45 0.55 0.65 0.75 0.85 0.95 1.05 ' + \
                  '--result_folder ./results/' + b6 + '/ ' + \
                  '--model_folder ./results/parameters/' + b6 + '/'
    elif b6 = = '10_value_networks':
        b7 = 'python3 load_balance_actor_multi_critic_train.py ' + \
                  '--num_workers 10 --service_rates 0.15 0.25 0.35 0.45 0.55 0.65 0.75 0.85 0.95 1.05 ' + \
                  '--result_folder ./results/' + b6 + '/ ' + \
                  '--model_folder ./results/parameters/' + b6 + '/'
    b8 = subprocess.Popen(b7, stdout=b5, stderr=b5, shell=True)
    b1.append(b8)
for b8 in b1:
    b8.wait()
for f in b2:
    f.close()