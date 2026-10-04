import numpy as np
import matplotlib.pyplot as plt
class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
def calc_rmse(actual, predicted):
    size = actual.shape[0]
    diff = actual - predicted
    rmse = np.sqrt(np.sum(diff ** 2) / size)
    return rmse
def calc_r2_score(actual, predicted):
    diff = actual - predicted
    residual_variance = np.sum(diff ** 2)
    mean_actual = np.mean(actual)
    total_variance = np.sum((actual - mean_actual) ** 2)
    r_squared_score = 1 - (residual_variance / total_variance)
    return r_squared_score
def get_performance_info(actual, predicted, degree, theta, training_technique):
    print(f"\n\n\n{Color.BOLD}{Color.UNDERLINE}{training_technique}:{Color.END}\n")
    print(f"R2-Score: {calc_r2_score(actual, predicted)}")
    print(f"RMSE: {calc_rmse(actual, predicted)}")
    print(f"Weights Generated for Degree {degree}: {', '.join(map(str, theta))}")
    print("\n\n\n")
def plot_cost_vs_iterations(cost, interval):
    plt.figure()
    x = np.arange(1, len(cost) + 1, interval)
    y = [cost[i - 1] for i in x]
    plt.plot(x, y)
    plt.xlabel('Number of Iterations')
    plt.ylabel('Cost (Halved Mean Square Error)')
    plt.title(f'Plot of Cost vs Iterations (every {interval} iterations)')
    plt.show()