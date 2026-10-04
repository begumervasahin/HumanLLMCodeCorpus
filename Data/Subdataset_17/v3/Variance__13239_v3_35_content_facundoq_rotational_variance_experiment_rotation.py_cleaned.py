import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import logging
import torch
from pytorch import dataset as datasets, models
from pytorch.experiment import model_loading, rotation
import pytorch.experiment.utils as utils
logging.getLogger().setLevel(logging.DEBUG)
use_cuda = torch.cuda.is_available()
def main():
    model_name, dataset_name = get_model_and_dataset_names()
    run_experiment(model_name, dataset_name, verbose=False)
def get_model_and_dataset_names():
    return utils.parse_model_and_dataset(
        "Experiment: accuracy of model for rotated vs unrotated dataset."
    )
def run_experiment(model_name, dataset_name, verbose=False):
    dataset = load_dataset(dataset_name, verbose)
    model, optimizer, rotated_model, rotated_optimizer = load_models_and_optimizers(
        model_name, dataset, verbose
    )
    config = configure_training(
        dataset, model_name, optimizer, rotated_optimizer
    )
    scores = train_models(config, model, rotated_model, dataset)
    display_scores(scores)
    save_trained_models(dataset, model, rotated_model, scores, config)
def load_dataset(dataset_name, verbose):
    dataset = datasets.get_dataset(dataset_name)
    if verbose:
        print(f"Experimenting with dataset: {dataset_name}")
        print(dataset.summary())
    return dataset
def load_models_and_optimizers(model_name, dataset, verbose):
    model, optimizer, rotated_model, rotated_optimizer = model_loading.get_model(
        model_name, dataset, use_cuda
    )
    if verbose:
        print(f"Training with model: {model_name}")
        print(model)
        print(rotated_model)
    return model, optimizer, rotated_model, rotated_optimizer
def configure_training(dataset, model_name, optimizer, rotated_optimizer):
    pre_rotated_epochs = 0
    batch_size = 256
    epochs, rotated_epochs = model_loading.get_epochs(dataset.name, model_name)
    return rotation.TrainRotatedConfig(
        batch_size=batch_size,
        epochs=epochs,
        rotated_epochs=rotated_epochs,
        pre_rotated_epochs=pre_rotated_epochs,
        optimizer=optimizer,
        rotated_optimizer=rotated_optimizer,
        use_cuda=use_cuda
    )
def train_models(config, model, rotated_model, dataset):
    return rotation.run(
        config, model, rotated_model, dataset, plot_accuracy=True, save_plots=True
    )
def display_scores(scores):
    rotation.print_scores(scores)
def save_trained_models(dataset, model, rotated_model, scores, config):
    save_model = True
    if save_model:
        rotation.save_models(dataset, model, rotated_model, scores, config)
if __name__ == "__main__":
    main()
else:
    dataset_name = "cifar10"
    model_name = models.AllConvolutional.__name__
    run_experiment(model_name, dataset_name, verbose=False)