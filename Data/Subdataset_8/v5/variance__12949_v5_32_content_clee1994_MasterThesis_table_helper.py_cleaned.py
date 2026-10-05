import evaluation
import learning
import datetime
import pickle
import numpy as np
import os
path = '/Users/clemens/Desktop/complet'
path_data = 'Data/'
path_output = 'Output/'
learning.path_output = path_output
evaluation.path_output = path_output
number_jobs = 1
learning.number_jobs = number_jobs
evaluation.number_jobs = number_jobs
learning_params = {
    'past_obs_int': False,
    'firms_used': 10,
    'n_past': 120,
    'n_past_add': 20,
    'n_cov': 5
}
learning.set_parameters(**learning_params)
test_split = 0.35
onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f[0] != '.']
with open(os.path.join(path, onlyfiles[0]), 'rb') as file:
    final_complet, r4, r1, sp500 = pickle.load(file)
for filename in onlyfiles[1:]:
    with open(os.path.join(path, filename), 'rb') as file:
        complet, r4, r1, sp500 = pickle.load(file)
        for data in complet[1:]:
            print(data[7])
            final_complet.append(data)
with open(os.path.join(path_output, "bowx_models4.p"), 'rb') as file:
    x_gram, dates_news = pickle.load(file)
split_point = int(np.floor(np.shape(x_gram[0])[0] * (1 - test_split)))
r4, sp500 = evaluation.pure_SP(dates_news[split_point:], path_data)
evaluation.final_table(final_complet, np.array(r4), r1, sp500)