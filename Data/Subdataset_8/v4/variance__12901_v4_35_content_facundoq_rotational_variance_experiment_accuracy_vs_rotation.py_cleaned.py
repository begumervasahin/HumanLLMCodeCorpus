import matplotlib.pyplot as plt
import logging
import torch
from pytorch import dataset as datasets
import pytorch.experiment.utils as utils
from pytorch.experiment import rotation, invariance_evaluation
logging.getLogger().setLevel(logging.DEBUG)
plt.rcParams['image.cmap'] = 'gray'
use_cuda = torch.cuda.is_available()
model_name, dataset_name = utils.parse_model_and_dataset("Accuracy vs rotation Experiment.")
verbose = False
if verbose:
    dataset = datasets.get_dataset(dataset_name)
    print(dataset.summary())
model, rotated_model, scores, config = rotation.load_models(dataset_name, model_name, use_cuda)
if verbose:
    rotation.print_scores(scores)
n_rotations = 16
rotated_results, classes, rotations = invariance_evaluation.run(rotated_model, dataset, config, n_rotations)
results, _, _ = invariance_evaluation.run(model, dataset, config, n_rotations)
base_folder = "plots/accuracy_rotation"
rotated_fig = invariance_evaluation.plot_results(rotated_results, classes, rotations)
rotated_fig_name = f"{base_folder}/{dataset_name}_{model_name}_rotated.png"
rotated_fig.savefig(rotated_fig_name)
fig = invariance_evaluation.plot_results(results, classes, rotations)
fig_name = f"{base_folder}/{dataset_name}_{model_name}_unrotated.png"
fig.savefig(fig_name)