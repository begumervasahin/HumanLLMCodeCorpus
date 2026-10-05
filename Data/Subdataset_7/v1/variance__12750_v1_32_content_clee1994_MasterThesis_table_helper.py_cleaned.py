import evaluation
import learning
import datetime
import pickle
import gc
import random
import numpy as np
b1 = '/Users/clemens/Desktop/complet'
b2 = 'Data/'
b3 = 'Output/'
learning.b3 = b3
evaluation.b3 = b3
a1 = 1
learning.a1 = a1
evaluation.a1 = a1
b4 = False
learning.b4 = b4
a2 = 10
a3 = 120
a4 = 20
learning.a3 = a3
learning.a4 = a4
a5 = 5
learning.a5 = a5
a6 = 0.35
from os import listdir
from os.b1 import isfile, join
b5 = [f for f in listdir(b1) if (isfile(join(b1, f)) and f[0] != '.')]
[final_complet, r4, r1, sp500] = pickle.load(open(b1 + "/" + b5[0], "rb"))
for i in range(np.shape(b5)[0] - 1):
    [complet, r4, r1, sp500] = pickle.load(open(b1 + "/" + b5[i + 1], "rb"))
    for j in range(np.shape(complet)[0] - 1):
        print(complet[j + 1][7])
        final_complet.append(complet[j + 1])
[x_gram, dates_news] = pickle.load(open(b3 + "bowx_models4.p", "rb"))
b6 = int(np.floor(np.shape(x_gram[0])[0] * (1 - a6)))
[r4, sp500] = evaluation.pure_SP(dates_news[b6:], b2)
evaluation.final_table(final_complet, np.array(r4), r1, sp500)