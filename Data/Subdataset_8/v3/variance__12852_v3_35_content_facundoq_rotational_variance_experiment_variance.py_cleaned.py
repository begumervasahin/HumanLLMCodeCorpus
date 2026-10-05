import matplotlib.pyplot as plt
import logging
from pytorch import models, dataset as datasets
import torch
import pytorch.experiment.utils as utils
from pytorch.experiment import rotation, variance
logging.basicConfig(level=logging.INFO)
def main():
    model_name, dataset_name = utils.parse_model_and_dataset("Experiment: accuracy of model for rotated vs unrotated dataset.")
    use_cuda = torch.cuda.is_available()
    dataset = datasets.get_dataset(dataset_name)
    model, rotated_model, scores, config = rotation.load_models(dataset, model_name, use_cuda)
    run_rotation_experiment(model, rotated_model, dataset, config)
def run_rotation_experiment(model, rotated_model, dataset, config):
    n_rotations = 16
    conv_aggregation_function = "sum"
    logging.info(f"Calculating measure with aggregation function {conv_aggregation_function} for conv layers and {n_rotations} rotations...")
    results = variance.run_all(model, rotated_model, dataset, config, n_rotations, conv_aggregation_function, batch_size=64)
    logging.info("Saving results...")
    variance.save_results(model.name, dataset.name, results, conv_aggregation_function)
if __name__ == "__main__":
    main()