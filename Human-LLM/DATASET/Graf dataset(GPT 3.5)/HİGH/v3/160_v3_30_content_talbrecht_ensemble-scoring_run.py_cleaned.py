import numpy as np
import matplotlib.pyplot as plt
import os
import config as cf
import tools as tl
import get_score as gs
import get_paleo as ps
import compare_score as cs
b1 = True
b2 = True
b3 = False
b4 = True
b5 = True
b6 = [cf, tl, gs, ps, cs]
for module in b6:
    reload(module)
b7 = cf.b7
b8 = cf.b8
b9 = np.arange(b7, b8 + 1)
b10 = {'b3': b3, 'b4': b4, 'b5': b5}
if b4:
    b11 = cf.output_data_path + "plots"
    if not os.path.exists(b11):
        os.makedirs(b11)
b12 = tl.load_observations(cf.observations_file, cf.velocity_observations_file)
if b2:
    for ensemble_number in b9:
        print("Ensemble number:", ensemble_number)
        b13 = gs.calculate_pd_score(ensemble_number, b12, b10)
        if b1:
            b14 = ps.calculate_paleo_score(ensemble_number, b12, b10)
        if b3:
            plt.show()
b15 = cs.compare_ensemble_scores(b9, b1, b10)
b16 = b15.score