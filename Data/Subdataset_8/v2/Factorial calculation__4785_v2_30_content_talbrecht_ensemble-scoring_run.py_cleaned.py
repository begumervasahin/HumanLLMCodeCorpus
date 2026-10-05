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
modules_to_reload = [cf, tl, gs, ps, cs]
for module in modules_to_reload:
    reload(module)
ensemble_min = cf.ensemble_min
ensemble_max = cf.ensemble_max
ensemble_numbers = np.arange(ensemble_min, ensemble_max + 1)
display_options = [show_plots, save_to_pdf, print_info]
if save_to_pdf:
    plots_directory = cf.output_data_path + "plots"
    if not os.path.exists(plots_directory):
        os.makedirs(plots_directory)
observations_file = cf.observations_file
velocity_observations_file = cf.velocity_observations_file
observations = tl.load_observations(observations_file, velocity_observations_file)
if cal_individual_misfits:
    for ensemble_number in ensemble_numbers:
        print("Ensemble number:", ensemble_number)
        pd_score = gs.calculate_pd_score(ensemble_number, observations, display_options)
        if do_paleo:
            paleo_score = ps.calculate_paleo_score(ensemble_number, observations, display_options)
        if show_plots:
            plt.show()
ensemble_comparison = cs.compare_ensemble_scores(ensemble_numbers, do_paleo, display_options)
final_score = ensemble_comparison.score