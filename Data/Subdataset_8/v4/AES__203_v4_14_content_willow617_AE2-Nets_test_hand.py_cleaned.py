import os
from utils.Dataset import Dataset
from model import model
from utils.print_result import print_result
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
def main():
    dataset = Dataset('handwritten_2views')
    x1, x2, ground_truth = dataset.load_data()
    x1 = dataset.normalize(x1, axis=0)
    x2 = dataset.normalize(x2, axis=0)
    n_clusters = len(set(ground_truth))
    activation_functions = {
        'ae1': 'sigmoid',
        'ae2': 'sigmoid',
        'dg1': 'sigmoid',
        'dg2': 'sigmoid'
    }
    dimensions = {
        'ae1': [240, 200],
        'ae2': [216, 200],
        'dg1': [64, 200],
        'dg2': [64, 200]
    }
    learning_rates = {
        'pretraining': 1.0e-3,
        'autoencoder': 1.0e-3,
        'discriminator': 1.0e-3,
        'hybrid': 1.0e-1
    }
    epochs = {
        'pretraining': 10,
        'total': 20,
        'hybrid': 50
    }
    para_lambda = 1
    batch_size = 100
    H, gt_adjusted = model(x1=x1,
                           x2=x2,
                           gt=ground_truth,
                           para_lambda=para_lambda,
                           dims=list(dimensions.values()),
                           act=list(activation_functions.values()),
                           lr=list(learning_rates.values()),
                           epochs=list(epochs.values()),
                           batch_size=batch_size)
    print_result(n_clusters, H, gt_adjusted)
if __name__ == '__main__':
    main()