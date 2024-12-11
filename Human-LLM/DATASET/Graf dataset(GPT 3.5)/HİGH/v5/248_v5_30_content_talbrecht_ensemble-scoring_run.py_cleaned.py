import numpy as np
import matplotlib.pyplot as plt
import os
import config as cf
import tools as tl
import get_score as gs
import get_paleo as ps
import compare_score as cs
b1 = [cf, tl, gs, ps, cs]
for module in b1:
    reload(module)
b2 = True
b3 = True
b4 = False
b5 = True
b6 = True
b7 = cf.b7
b8 = cf.b8
b9 = np.arange(b7, b8 + 1)
b10 = [b4, b5, b6]
if b5:
    b11 = cf.output_data_path + "plots"
    os.makedirs(b11, b12 = True)
b13 = tl.load_observations(cf.obsfile, cf.velobsfile)
if b3:
    for ensnum in b9:
        print("Ensemble number:", ensnum)
        b14 = gs.pd_score(ensnum, b13, b10)
        if b2:
            b15 = ps.paleo_score(ensnum, b13, b10)
        if b4:
            plt.show()
b16 = cs.compare_score(b9, b2, b10)
b17 = b16.b17