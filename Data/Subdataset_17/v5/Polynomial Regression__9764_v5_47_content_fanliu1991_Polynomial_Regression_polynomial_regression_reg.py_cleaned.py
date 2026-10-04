import assignment1 as a1
import numpy as np
import matplotlib.pyplot as plt
def load_and_prepare_data():
    countries, features, values = a1.load_unicef_data()
    targets = values[:, 1]
    x = values[:, 7:]
    x = a1.normalize_data(x)
    return x, targets
def add_polynomial_features(x_train, degree=2):
    phi = np.ones((x_train.shape[0], 1))
    for d in range(1, degree + 1):
        phi = np.concatenate((phi, np.power(x_train, d)), axis=1)
    return phi
def cross_validate(phi, t_train, lambda_set, partition_size):
    coefficient_M = phi.shape[1]
    identity_matrix = np.identity(coefficient_M)
    lambda_errors = []
    for lambda_value in lambda_set:
        validation_errors = []
        for validation_index in range(10):
            validation_start = validation_index * partition_size
            validation_end = validation_start + partition_size
            validation_phi = phi[validation_start:validation_end, :]
            validation_t = t_train[validation_start:validation_end]
            training_phi = np.concatenate((phi[:validation_start, :], phi[validation_end:, :]), axis=0)
            training_t = np.concatenate((t_train[:validation_start], t_train[validation_end:]), axis=0)
            w = np.linalg.inv(lambda_value * identity_matrix + training_phi.T @ training_phi) @ training_phi.T @ training_t
            validation_error = np.sqrt(np.mean((validation_phi @ w - validation_t) ** 2))
            validation_errors.append(validation_error)
        lambda_errors.append(np.mean(validation_errors))
    return lambda_errors
def plot_validation_errors(lambda_set, lambda_errors):
    plt.semilogx(lambda_set[1:], lambda_errors[1:], marker='o')
    plt.xlabel('Lambda Value (log scale)')
    plt.ylabel('Average Validation Set Error')
    plt.title('Average Validation Set Error vs. Lambda Value')
    plt.axhline(y=lambda_errors[0], linewidth=2, color='g', label='Unregularized result, Lambda = 0')
    plt.legend()
    plt.show()
def main():
    x, targets = load_and_prepare_data()
    N_TRAIN = 100
    x_train = x[:N_TRAIN, :]
    t_train = targets[:N_TRAIN]
    lambda_set = [0, 0.01, 0.1, 1, 10, 100, 1000, 10000]
    phi = add_polynomial_features(x_train, degree=2)
    partition_size = N_TRAIN
    lambda_errors = cross_validate(phi, t_train, lambda_set, partition_size)
    print(lambda_errors)
    plot_validation_errors(lambda_set, lambda_errors)
if __name__ == "__main__":
    main()