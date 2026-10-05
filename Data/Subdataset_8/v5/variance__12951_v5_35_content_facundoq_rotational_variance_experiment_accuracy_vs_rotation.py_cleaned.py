import matplotlib.pyplot as plt
import logging
import torch
from pytorch import dataset as datasets
import pytorch.experiment.utils as utils
from pytorch.experiment import rotation, invariance_evaluation
logging.getLogger().setLevel(logging.DEBUG)
plt.rcParams['image.cmap'] = 'gray'
def load_dataset(name, verbose=False):
    if verbose:
        dataset = datasets.get_dataset(name)
        print(dataset.summary())
    return datasets.get_dataset(name)
def evaluate_invariance(model, dataset, config, n_rotations):
    results, classes, rotations = invariance_evaluation.run(model, dataset, config, n_rotations)
    return results, classes, rotations
def save_plot(fig, folder, dataset_name, model_name, rotation_type):
    file_name = f"{folder}/{dataset_name}_{model_name}_{rotation_type}.png"
    fig.savefig(file_name)
use_cuda = torch.cuda.is_available()
experiment_description = "Accuracy vs rotation Experiment."
model_name, dataset_name = utils.parse_model_and_dataset(experiment_description)
dataset = load_dataset(dataset_name, verbose)
model, rotated_model, scores, config = rotation.load_models(dataset_name, model_name, use_cuda)
if verbose:
    rotation.print_scores(scores)
n_rotations = 16
rotated_results, classes, rotations = evaluate_invariance(rotated_model, dataset, config, n_rotations)
results, _, _ = evaluate_invariance(model, dataset, config, n_rotations)
base_folder = "plots/accuracy_rotation"
rotated_fig = invariance_evaluation.plot_results(rotated_results, classes, rotations)
save_plot(rotated_fig, base_folder, dataset_name, model_name, "rotated")
fig = invariance_evaluation.plot_results(results, classes, rotations)
save_plot(fig, base_folder, dataset_name, model_name, "unrotated")