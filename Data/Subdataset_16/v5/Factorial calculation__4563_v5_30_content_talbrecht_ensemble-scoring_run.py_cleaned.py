import numpy as np
import matplotlib.pyplot as plt
import os
import importlib
b1 = True
b2 = True
b3 = False
b4 = True
b5 = True
import config as cf
import tools as tl
import get_score as gs
import get_paleo as ps
import compare_score as cs
b6 = [cf, tl, gs, ps, cs]
for module in b6:
    importlib.reload(module)
b7 = cf.b7
b8 = cf.b8
b9 = np.arange(b7, b8 + 1)
b10 = [b3, b4, b5]
if b4:
    b11 = os.path.join(cf.output_data_path, "plots")
    os.makedirs(b11, b12 = True)
b13 = cf.b13
b14 = cf.b14
b15 = tl.load_observations(b13, b14)
def fonk1(b9, b15, b10):
    for ensnum in b9:
        print(f"Ensemble number: {ensnum}")
        gs.pd_score(ensnum, b15, b10)
        if b1:
            ps.paleo_score(ensnum, b15, b10)
        if b3:
            plt.show()
if b2:
    fonk1(b9, b15, b10)
b16 = cs.compare_score(b9, b1, b10)
b17 = b16.b17
if b5:
    print(f"Final b17: {b17}")