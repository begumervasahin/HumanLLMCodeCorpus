import numpy as np
import matplotlib.pyplot as plt
import os
import importlib
import config as cf
import tools as tl
import get_score as gs
import get_paleo as ps
import compare_score as cs
importlib.reload(cf)
importlib.reload(tl)
importlib.reload(gs)
importlib.reload(ps)
importlib.reload(cs)
b1 = True
b2 = True
b3 = False
b4 = True
b5 = True
b6 = cf.b6
b7 = cf.b7
b8 = np.arange(b6, b7 + 1)
b9 = [b3, b4, b5]
if b4:
    b10 = os.path.join(cf.output_data_path, "plots")
    if not os.path.exists(b10):
        os.makedirs(b10)
b11 = cf.b11
b12 = cf.b12
b13 = tl.load_observations(b11, b12)
if b2:
    for ensnum in b8:
        print(f"Ensemble number: {ensnum}")
        b14 = gs.pd_score(ensnum, b13, b9)
        if b1:
            b15 = ps.paleo_score(ensnum, b13, b9)
        if b3:
            plt.show()
b16 = cs.compare_score(b8, b1, b9)
b17 = b16.b17