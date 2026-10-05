import matplotlib as mpl
import matplotlib.pyplot as plt
import logging
from pytorch import dataset as datasets
import torch
import pytorch.experiment.utils as utils
from pytorch.experiment import rotation, invariance_evaluation
logging.getLogger().setLevel(logging.DEBUG)
mpl.use('Agg')
plt.rcParams['image.cmap'] = 'gray'
experiment_description = "Accuracy vs rotation Experiment."
verbose = False
n_rotations = 16
base_folder = "plots/accuracy_rotation"
model_name, dataset_name = utils.parse_model_and_dataset(experiment_description)
use_cuda = torch.cuda.is_available()
dataset = datasets.get_dataset(dataset_name)
if verbose:
    print(dataset.summary())
model, rotated_model, scores, config = rotation.load_models(dataset, model_name, use_cuda)
if verbose:
    rotation.print_scores(scores)
rotated_results, classes, rotations = invariance_evaluation.run(rotated_model, dataset, config, n_rotations)
results, _, _ = invariance_evaluation.run(model, dataset, config, n_rotations)
rotated_fig = invariance_evaluation.plot_results(rotated_results, classes, rotations)
rotated_fig_name = f"{base_folder}/{dataset.name}_{model.name}_rotated.png"
rotated_fig.savefig(rotated_fig_name)
fig = invariance_evaluation.plot_results(results, classes, rotations)
fig_name = f"{base_folder}/{dataset.name}_{model.name}_unrotated.png"
fig.savefig(fig_name)