import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['image.cmap'] = 'gray'
import logging
from pytorch import models
from pytorch import dataset as datasets
import torch
import pytorch.experiment.utils as utils
from pytorch.experiment import rotation, variance
def parse_model_and_dataset(description):
    return utils.parse_model_and_dataset(description)
def load_default_settings():
    return "cifar10", models.AllConvolutional.__name__
def print_verbose_summary(dataset):
    print(dataset.summary())
def calculate_and_save_results(model, rotated_model, dataset, config, n_rotations, conv_aggregation_function):
    logging.info(f"Calculating measure with aggregation function {conv_aggregation_function} for conv layers and {n_rotations} rotations...")
    results = variance.run_all(model, rotated_model, dataset, config, n_rotations, conv_aggregation_function, batch_size=64)
    logging.info("Saving results...")
    variance.save_results(model.name, dataset.name, results, conv_aggregation_function)
if __name__ == "__main__":
    model_name, dataset_name = parse_model_and_dataset("Experiment: accuracy of model for rotated vs unrotated dataset.")
    else:
        dataset_name, model_name = load_default_settings()
    use_cuda = torch.cuda.is_available()
    dataset = datasets.get_dataset(dataset_name)
    verbose = False
    if verbose:
        print_verbose_summary(dataset)
    model, rotated_model, scores, config = rotation.load_models(dataset, model_name, use_cuda)
    if verbose:
        print("\n" * 3)
        rotation.print_scores(scores)
    n_rotations = 16
    conv_aggregation_function = "sum"
    calculate_and_save_results(model, rotated_model, dataset, config, n_rotations, conv_aggregation_function)