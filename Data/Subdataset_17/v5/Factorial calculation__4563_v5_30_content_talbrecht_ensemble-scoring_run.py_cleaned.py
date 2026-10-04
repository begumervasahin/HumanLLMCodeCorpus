import numpy as np
import matplotlib.pyplot as plt
import os
import importlib
do_paleo = True
cal_individual_misfits = True
show_plots = False
save_to_pdf = True
print_info = True
import config as cf
import tools as tl
import get_score as gs
import get_paleo as ps
import compare_score as cs
modules = [cf, tl, gs, ps, cs]
for module in modules:
    importlib.reload(module)
ens_min = cf.ens_min
ens_max = cf.ens_max
ensnums = np.arange(ens_min, ens_max + 1)
shownprint = [show_plots, save_to_pdf, print_info]
if save_to_pdf:
    plots_path = os.path.join(cf.output_data_path, "plots")
    os.makedirs(plots_path, exist_ok=True)
obsfile = cf.obsfile
velobsfile = cf.velobsfile
observations = tl.load_observations(obsfile, velobsfile)
def calculate_individual_misfits(ensnums, observations, shownprint):
    for ensnum in ensnums:
        print(f"Ensemble number: {ensnum}")
        gs.pd_score(ensnum, observations, shownprint)
        if do_paleo:
            ps.paleo_score(ensnum, observations, shownprint)
        if show_plots:
            plt.show()
if cal_individual_misfits:
    calculate_individual_misfits(ensnums, observations, shownprint)
ens = cs.compare_score(ensnums, do_paleo, shownprint)
score = ens.score
if print_info:
    print(f"Final score: {score}")