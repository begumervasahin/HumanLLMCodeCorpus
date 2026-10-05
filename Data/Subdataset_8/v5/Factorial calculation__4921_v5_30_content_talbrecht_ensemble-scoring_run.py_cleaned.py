import numpy as np
import matplotlib.pyplot as plt
import os
import config as cf
import tools as tl
import get_score as gs
import get_paleo as ps
import compare_score as cs
reload_list = [cf, tl, gs, ps, cs]
for module in reload_list:
    reload(module)
do_paleo = True
cal_individual_misfits = True
show_plots = False
save_to_pdf = True
print_info = True
ens_min = cf.ens_min
ens_max = cf.ens_max
ensnums = np.arange(ens_min, ens_max + 1)
shownprint = [show_plots, save_to_pdf, print_info]
if save_to_pdf:
    plots_dir = cf.output_data_path + "plots"
    os.makedirs(plots_dir, exist_ok=True)
observations = tl.load_observations(cf.obsfile, cf.velobsfile)
if cal_individual_misfits:
    for ensnum in ensnums:
        print("Ensemble number:", ensnum)
        pds = gs.pd_score(ensnum, observations, shownprint)
        if do_paleo:
            pls = ps.paleo_score(ensnum, observations, shownprint)
        if show_plots:
            plt.show()
ens = cs.compare_score(ensnums, do_paleo, shownprint)
score = ens.score