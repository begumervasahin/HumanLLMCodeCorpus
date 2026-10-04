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
def calculate_rmse(actual, predicted):
    size = actual.shape[0]
    rmse = np.sqrt(np.mean((actual - predicted) ** 2))
    return rmse
def calculate_r2_score(actual, predicted):
    mean_actual = np.mean(actual)
    total_variance = np.sum((actual - mean_actual) ** 2)
    residual_variance = np.sum((actual - predicted) ** 2)
    r_squared_score = 1 - (residual_variance / total_variance)
    return r_squared_score
def display_performance_info(actual, predicted, degree, theta, training_technique):
    r2_score = calculate_r2_score(actual, predicted)
    rmse = calculate_rmse(actual, predicted)
    weights_str = ', '.join(map(str, theta))
    print(f"\n\n\n{Color.BOLD}{Color.UNDERLINE}{training_technique}:{Color.END}\n")
    print(f"R2-Score: {r2_score}")
    print(f"RMSE: {rmse}")
    print(f"Weights Generated for Degree {degree}: {weights_str}")
    print("\n\n\n")
def plot_cost_vs_iterations(cost, interval):
    iterations = np.arange(1, len(cost) + 1, interval)
    cost_values = [cost[i - 1] for i in iterations]
    plt.figure()
    plt.plot(iterations, cost_values)
    plt.xlabel('Number of Iterations')
    plt.ylabel('Cost (Halved Mean Square Error)')
    plt.title(f'Plot of Cost vs Iterations (every {interval} iterations)')
    plt.show()