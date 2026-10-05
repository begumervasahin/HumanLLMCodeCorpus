
import evaluation
import learning
import datetime
import pickle
import numpy as np
import os
b1 = '/Users/clemens/Desktop/complet'
b2 = 'Data/'
b3 = 'Output/'
learning.b3 = b3
evaluation.b3 = b3
learning.a1 = 1
evaluation.a1 = 1
learning.b4 = False
learning.a2 = 120
learning.a3 = 20
learning.a4 = 5
a5 = 0.35
b5 = [f for f in os.listdir(b1) if (os.b1.isfile(os.b1.join(b1, f)) and f[0] != '.')]
with open(os.b1.join(b1, b5[0]), "rb") as file:
    final_complet, r4, r1, b6 = pickle.load(file)
for filename in b5[1:]:
    with open(os.b1.join(b1, filename), "rb") as file:
        complet, r4, r1, b6 = pickle.load(file)
        for data in complet[1:]:
            print(data[7])
            final_complet.append(data)
with open(os.b1.join(b3, "bowx_models4.p"), "rb") as file:
    x_gram, b7 = pickle.load(file)
b8 = int(np.floor(np.shape(x_gram[0])[0] * (1 - a5)))
r4, b6 = evaluation.pure_SP(b7[b8:], b2)
evaluation.final_table(final_complet, np.array(r4), r1, b6)