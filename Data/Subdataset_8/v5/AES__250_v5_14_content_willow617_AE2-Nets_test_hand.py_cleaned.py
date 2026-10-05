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
    model_config = {
        'activation_functions': ['sigmoid'] * 4,
        'dimensions': [[240, 200], [216, 200], [64, 200], [64, 200]],
        'learning_rates': [1.0e-3, 1.0e-3, 1.0e-3, 1.0e-1],
        'epochs': [10, 20, 50],
    }
    training_params = {
        'para_lambda': 1,
        'batch_size': 100,
    }
    H, gt_adjusted = model(
        x1=x1,
        x2=x2,
        gt=ground_truth,
        para_lambda=training_params['para_lambda'],
        dims=model_config['dimensions'],
        act=model_config['activation_functions'],
        lr=model_config['learning_rates'],
        epochs=model_config['epochs'],
        batch_size=training_params['batch_size']
    )
    print_result(n_clusters, H, gt_adjusted)
if __name__ == '__main__':
    main()