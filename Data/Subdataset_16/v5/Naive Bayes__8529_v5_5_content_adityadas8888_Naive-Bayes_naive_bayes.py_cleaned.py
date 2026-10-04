import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
def fonk1(mean, covariance, size):
    return np.random.multivariate_normal(mean, covariance, size).T
def fonk2(b18, b19):
    x0, b1 = b18
    x1, b2 = b19
    b3 = {
        'mean_x0': np.mean(x0), 'mean_y0': np.mean(b1),
        'std_x0': np.std(x0), 'std_y0': np.std(b1),
        'mean_x1': np.mean(x1), 'mean_y1': np.mean(b2),
        'std_x1': np.std(x1), 'std_y1': np.std(b2),
        'prior0': len(x0) / (len(x0) + len(x1)),
        'prior1': len(x1) / (len(x0) + len(x1))
    }
    return b3
def fonk3(b22, b3):
    b22['likelihood0'] = (
        norm.pdf(b22['x'], b4 = b3['mean_x0'], scale=b3['std_x0']) *
        norm.pdf(b22['y'], b4 = b3['mean_y0'], scale=b3['std_y0'])
    )
    b22['likelihood1'] = (
        norm.pdf(b22['x'], b4 = b3['mean_x1'], scale=b3['std_x1']) *
        norm.pdf(b22['y'], b4 = b3['mean_y1'], scale=b3['std_y1'])
    )
    b22['posterior0'] = b22['likelihood0'] * b3['prior0']
    b22['posterior1'] = b22['likelihood1'] * b3['prior1']
    b22['predicted'] = np.where(b22['posterior0'] > b22['posterior1'], 0, 1)
    b22['b14'] = np.where(b22['posterior0'] > b22['posterior1'], 'r', 'b')
    return b22
def fonk4(b22):
    b5 = np.sum((b22['predicted'] == 0) & (b22['actual'] == 0))
    b6 = np.sum((b22['predicted'] == 1) & (b22['actual'] == 1))
    b7 = np.sum((b22['predicted'] == 0) & (b22['actual'] == 1))
    b8 = np.sum((b22['predicted'] == 1) & (b22['actual'] == 0))
    b9 = (b6 + b5) / (b6 + b7 + b8 + b5)
    b10 = 1 - b9
    b11 = b6 / (b6 + b8)
    b12 = b6 / (b6 + b7)
    return {
        'b9': b9,
        'b10': b10,
        'b11': b11,
        'b12': b12,
        'b6': b6,
        'b5': b5,
        'b7': b7,
        'b8': b8
    }
def fonk5(b22):
    plt.figure(b13 = (10, 10))
    plt.scatter(b22['x'], b22['y'], b14 = b22['b14'], alpha=0.5, edgecolor='k', marker="x")
    plt.title('Test Data Predictions')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
def fonk6(train_size_class0, train_size_class1):
    b15 = [1, 0]
    b16 = [0, 1]
    b17 = [[1, 0.75], [0.75, 1]]
    b18 = fonk1(b15, b17, train_size_class0)
    b19 = fonk1(b16, b17, train_size_class1)
    b20 = fonk1(b15, b17, 100)
    b21 = fonk1(b16, b17, 100)
    b22 = pd.DataFrame({
        'x': np.concatenate((b20[0], b21[0])),
        'y': np.concatenate((b20[1], b21[1])),
        'actual': np.concatenate((np.zeros(100), np.ones(100)))
    })
    b3 = fonk2(b18, b19)
    b22 = fonk3(b22, b3)
    b23 = fonk4(b22)
    print(f"Accuracy: {b23['b9']}")
    print(f"Error Rate: {b23['b10']}")
    print(f"Recall: {b23['b11']}")
    print(f"Precision: {b23['b12']}")
    print(f"True Positives: {b23['b6']}, True Negatives: {b23['b5']}")
    print(f"False Positives: {b23['b7']}, False Negatives: {b23['b8']}")
    fonk5(b22)
    return b23['b9']
def fonk7():
    b9 = fonk6(500, 500)
    print("Accuracy of the model:", b9)
if b24 = = "__main__":
    fonk7()