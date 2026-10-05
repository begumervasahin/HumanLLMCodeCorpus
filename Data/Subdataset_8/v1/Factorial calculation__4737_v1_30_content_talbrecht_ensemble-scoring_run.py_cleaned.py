import numpy as np
import matplotlib.pyplot as plt
import os
import config as cf
import tools as tl
import get_score as gs
import get_paleo as ps
import compare_score as cs
do_paleo = True
cal_individual_misfits = True
show_plots = False
save_to_pdf = True
print_info = True
reload_list = [cf, tl, gs, ps, cs]
for module in reload_list:
    reload(module)
ens_min = cf.ens_min
ens_max = cf.ens_max
ensnums = np.arange(ens_min, ens_max + 1)
shownprint = [show_plots, save_to_pdf, print_info]
if save_to_pdf:
    plots_dir = cf.output_data_path + "plots"
    if not os.path.exists(plots_dir):
        os.makedirs(plots_dir)
obsfile = cf.obsfile
velobsfile = cf.velobsfile
observations = tl.load_observations(obsfile, velobsfile)
if cal_individual_misfits:
    for ensnum in ensnums:
        print("ensemble number:", ensnum)
        pds = gs.pd_score(ensnum, observations, shownprint)
        if do_paleo:
            pls = ps.paleo_score(ensnum, observations, shownprint)
        if show_plots:
            plt.show()
ens = cs.compare_score(ensnums, do_paleo, shownprint)
score = ens.score