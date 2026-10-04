import argparse
from datetime import datetime as dt
import numpy as np
import a1q1d
import a1q1e
import a1q1f
import a1q1g
import a1q2
def load_data(normalize=True):
    print("\nLoading data...")
    x = np.loadtxt('./hw1x.dat')
    y = np.loadtxt('./hw1y.dat')
    if normalize:
        x = (x - np.mean(x, axis=0)) / np.std(x, axis=0)
    print(f"x = {x.shape}")
    print(f"y = {y.shape}")
    return x, y
def split_data(x, y, test_size=0.2):
    print(f"\nSplitting data into {1-test_size:.2f} train {test_size:.2f} test...")
    seed = dt.now().microsecond
    np.random.seed(seed)
    indices = np.random.permutation(x.shape[0])
    x = x[indices]
    y = y[indices]
    split_idx = int(x.shape[0] * test_size)
    x_train, x_test = x[split_idx:], x[:split_idx]
    y_train, y_test = y[split_idx:], y[:split_idx]
    print(f"x_train = {x_train.shape}")
    print(f"x_test = {x_test.shape}")
    print(f"y_train = {y_train.shape}")
    print(f"y_test = {y_test.shape}")
    return x_train, y_train, x_test, y_test
def parse_bool(value):
    return value.lower() in ['1', 'true', 'yes']
def main():
    parser = argparse.ArgumentParser(description='COMP 652 - Machine Learning - Assignment 1')
    parser.add_argument('--q1d', action="store_true", help='produce only plots for q1.d')
    parser.add_argument('--q1f', action="store_true", help='produce only plots for q1.f')
    parser.add_argument('--q1g', action="store_true", help='produce only plots for q1.g')
    parser.add_argument('--q2', action="store_true", help='produce only plots for q2.c')
    parser.add_argument('--normalize', type=parse_bool, default=True, help='normalize the X matrix when loading it')
    parser.add_argument('--use_sgd', type=parse_bool, default=True, help='run logistic regression using stochastic gradient descent')
    parser.add_argument('--n_iter', type=int, default=10000, help='number of iterations for SGD, or max number of iterations for LogReg')
    args = parser.parse_args()
    print(args)
    x, y = load_data(normalize=args.normalize)
    x_train, y_train, x_test, y_test = split_data(x, y, test_size=0.2)
    data = None
    sigmas = [0.1, 0.5, 1, 5, 10]
    means = np.linspace(-10, 10, len(sigmas))
    gaussian_data = None
    plot_all = not any([args.q1d, args.q1f, args.q1g, args.q2])
    if plot_all or args.q1d:
        data = a1q1d.log_reg(x_train, y_train, x_test, y_test, args.n_iter, args.use_sgd)
        a1q1d.plot(data)
    if plot_all or args.q1f:
        if data is None:
            data = a1q1d.log_reg(x_train, y_train, x_test, y_test, args.n_iter, args.use_sgd)
        gaussian_data = a1q1e.reformat(x_train, x_test, sigmas, means)
        gaussian_data = a1q1f.log_reg(gaussian_data, y_train, y_test, sigmas, args.n_iter, args.use_sgd)
        a1q1f.plot(gaussian_data, sigmas, data)
    if plot_all or args.q1g:
        if gaussian_data is None:
            gaussian_data = a1q1e.reformat(x_train, x_test, sigmas, means)
            gaussian_data = a1q1f.log_reg(gaussian_data, y_train, y_test, sigmas, args.n_iter, args.use_sgd)
        full_x_train, full_x_test = a1q1g.build_feature_matrices(gaussian_data, sigmas)
        data = a1q1g.log_reg(full_x_train, full_x_test, sigmas, y_train, y_test, args.n_iter, args.use_sgd)
        a1q1g.plot(data)
    if plot_all or args.q2:
        data = a1q2.log_reg(x_train, y_train, x_test, y_test)
        a1q2.plot(data)
if __name__ == '__main__':
    main()