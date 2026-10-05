import os
from utils.Dataset import Dataset
from model import model
from utils.print_result import print_result
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
if __name__ == '__main__':
    dataset = Dataset('handwritten_2views')
    x1, x2, ground_truth = dataset.load_data()
    x1 = dataset.normalize(x1, 0)
    x2 = dataset.normalize(x2, 0)
    num_clusters = len(set(ground_truth))
    activation_ae1, activation_ae2, activation_dg1, activation_dg2 = 'sigmoid', 'sigmoid', 'sigmoid', 'sigmoid'
    dimensions_ae1 = [240, 200]
    dimensions_ae2 = [216, 200]
    dimensions_dg1 = [64, 200]
    dimensions_dg2 = [64, 200]
    regularization_parameter = 1
    batch_size = 100
    learning_rate_pretraining = 1.0e-3
    learning_rate_autoencoder = 1.0e-3
    learning_rate_discriminator = 1.0e-3
    learning_rate_hypernetwork = 1.0e-1
    epochs_pretraining = 10
    total_epochs = 20
    activations = [activation_ae1, activation_ae2, activation_dg1, activation_dg2]
    dimensions = [dimensions_ae1, dimensions_ae2, dimensions_dg1, dimensions_dg2]
    learning_rates = [learning_rate_pretraining, learning_rate_autoencoder, learning_rate_discriminator, learning_rate_hypernetwork]
    hypernetwork_epochs = 50
    epochs = [epochs_pretraining, total_epochs, hypernetwork_epochs]
    H, ground_truth = model(x1, x2, ground_truth, regularization_parameter, dimensions, activations, learning_rates, epochs, batch_size)
    print_result(num_clusters, H, ground_truth)