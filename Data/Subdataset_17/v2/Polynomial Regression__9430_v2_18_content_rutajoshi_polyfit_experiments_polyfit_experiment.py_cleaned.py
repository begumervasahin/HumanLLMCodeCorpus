import numpy as np
import matplotlib.pyplot as plt
def set_axis_ranges(x, y):
    plt.xlim(min(x) - 1, max(x) + 1)
    plt.ylim(min(y) - 1, max(y) + 1)
def plot_function(x, func, style, color, label):
    y = func(x)
    plt.plot(x, y, style, color=color, label=label)
def plot_data(x, y, style, color, label):
    plt.plot(x, y, style, color=color, label=label)
def show_all(legend_loc='upper right'):
    plt.legend(loc=legend_loc)
    plt.show()
def make_function(w):
    def func(x):
        return evaluate_function(x, w)
    return func
def evaluate_function(x, w):
    y = 0
    for i in range(len(w)):
        y += (w[i] * (x ** i))
    return y
def evaluate_function_vec(x_values, w):
    y_values = [evaluate_function(x, w) for x in x_values]
    return np.array(y_values)
def sample_function(d, w, n, lower=-100, upper=100):
    assert len(w) == d + 1, "Must pass in d+1 coefficients"
    func_range = upper - lower
    x_values = np.array([lower + func_range * np.random.sample() for _ in range(n)])
    y_values = evaluate_function_vec(x_values, w)
    return x_values, y_values
def polynomial_regression(x_train, y_train, d, noise_mean=0, noise_std=1):
    X_mtx = []
    for x in x_train:
        evaluated_orders = [x ** i for i in range(d + 1)]
        X_mtx.append(np.array(evaluated_orders))
    X_mtx = np.array(X_mtx)
    y_train = np.array([i + np.random.normal(noise_mean, noise_std) for i in y_train])
    w = np.matmul(np.linalg.inv(np.matmul(X_mtx.T, X_mtx)), np.matmul(X_mtx.T, y_train))
    return w
def run_experiment(sample_coefficients, model_degree, n, noise_mean=0, noise_std=0.5):
    sample_degree = len(sample_coefficients) - 1
    x_train, y_train = sample_function(sample_degree, sample_coefficients, n, lower=-5, upper=5)
    polyfit_coefficients = polynomial_regression(x_train, y_train, model_degree)
    true_function = make_function(sample_coefficients)
    learned_function = make_function(polyfit_coefficients)
    y_model = evaluate_function_vec(x_train, polyfit_coefficients)
    variance = sum([(y_model[i] - y_train[i]) ** 2 for i in range(len(x_train))]) / len(x_train)
    print("\nVariance of the polyfit = " + str(variance) + "\n")
    set_axis_ranges(x_train, y_train)
    plot_function(x_train, true_function, '-', color='r', label='ground truth function')
    plot_function(x_train, learned_function, '--', color='b', label='model fit function')
    plot_data(x_train, y_train, '.', color='g', label='sample points')
    show_all(legend_loc='upper right')
def main():
    w = [3, 1, 1, -2]
    run_experiment(w, 3, 6, noise_mean=0, noise_std=0.5)
if __name__ == "__main__":
    main()