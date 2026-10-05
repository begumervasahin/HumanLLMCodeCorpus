import os
import pickle
import numpy as np
import evaluation
import learning
b1 = '/Users/clemens/Desktop/complet'
b2 = 'Data/'
b3 = 'Output/'
b4 = {
    'b3': b3,
    'number_jobs': 1,
    'past_obs_int': False,
    'n_past': 120,
    'n_past_add': 20,
    'n_cov': 5
}
b5 = {
    'b3': b3,
    'number_jobs': 1
}
a1 = 0.35
b6 = [f for f in os.listdir(b1) if os.b1.isfile(os.b1.join(b1, f)) and f[0] != '.']
with open(os.b1.join(b1, b6[0]), "rb") as file:
    final_complet, r4, r1, b7 = pickle.load(file)
for filename in b6[1:]:
    with open(os.b1.join(b1, filename), "rb") as file:
        complet, r4, r1, b7 = pickle.load(file)
        final_complet.extend(complet[1:])
with open(os.b1.join(b3, "bowx_models4.p"), "rb") as file:
    x_gram, b8 = pickle.load(file)
b9 = int(np.floor(np.shape(x_gram[0])[0] * (1 - a1)))
r4, b7 = evaluation.pure_SP(b8[b9:], b2)
evaluation.final_table(final_complet, np.array(r4), r1, b7)