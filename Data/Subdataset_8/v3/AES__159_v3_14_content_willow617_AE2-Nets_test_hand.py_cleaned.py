import os
from utils.Dataset import Dataset
from model import model
from utils.print_result import print_result
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
if __name__ == '__main__':
    dataset = Dataset('handwritten_2views')
    x1, x2, ground_truth = dataset.load_data()
    x1_normalized = dataset.normalize(x1, 0)
    x2_normalized = dataset.normalize(x2, 0)
    num_clusters = len(set(ground_truth))
    ae_activation_1, ae_activation_2, dg_activation_1, dg_activation_2 = 'sigmoid', 'sigmoid', 'sigmoid', 'sigmoid'
    ae_dimensions_1 = [240, 200]
    ae_dimensions_2 = [216, 200]
    dg_dimensions_1 = [64, 200]
    dg_dimensions_2 = [64, 200]
    regularization_parameter = 1
    batch_size = 100
    lr_pretraining = 1.0e-3
    lr_autoencoder = 1.0e-3
    lr_discriminator = 1.0e-3
    lr_hypernetwork = 1.0e-1
    epochs_pretraining = 10
    total_epochs = 20
    activations = [ae_activation_1, ae_activation_2, dg_activation_1, dg_activation_2]
    dimensions = [ae_dimensions_1, ae_dimensions_2, dg_dimensions_1, dg_dimensions_2]
    learning_rates = [lr_pretraining, lr_autoencoder, lr_discriminator, lr_hypernetwork]
    hypernetwork_epochs = 50
    epochs = [epochs_pretraining, total_epochs, hypernetwork_epochs]
    learned_representation, ground_truth = model(x1_normalized, x2_normalized, ground_truth, regularization_parameter, dimensions, activations, learning_rates, epochs, batch_size)
    print_result(num_clusters, learned_representation, ground_truth)