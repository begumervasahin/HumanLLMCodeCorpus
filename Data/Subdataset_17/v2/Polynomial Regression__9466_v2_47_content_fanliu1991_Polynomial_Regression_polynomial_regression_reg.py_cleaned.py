import numpy as np
import matplotlib.pyplot as plt
import assignment1 as a1
(countries, features, values) = a1.load_unicef_data()
targets = values[:, 1]
x = values[:, 7:]
x = a1.normalize_data(x)
N_TRAIN = 100
x_train = x[:N_TRAIN, :]
t_train = targets[:N_TRAIN]
lambda_set = [0, 0.01, 0.1, 1, 10, 100, 1000, 10000]
phi = np.ones((N_TRAIN, 1))
for degree in range(2):
    phi = np.concatenate((phi, np.power(x_train, degree + 1)), axis=1)
coefficient_M = phi.shape[1]
identity_matrix = np.identity(coefficient_M)
partition_size = N_TRAIN
lambda_errors = []
for lambda_value in lambda_set:
    validation_errors = []
    for i in range(10):
        start = i * partition_size
        end = start + partition_size
        validation_phi = phi[start:end, :]
        validation_t = t_train[start:end]
        training_phi = np.concatenate((phi[:start, :], phi[end:, :]), axis=0)
        training_t = np.concatenate((t_train[:start], t_train[end:]), axis=0)
        w = np.linalg.inv(lambda_value * identity_matrix + training_phi.T @ training_phi) @ training_phi.T @ training_t
        validation_error = np.sqrt(np.mean((validation_phi @ w - validation_t) ** 2))
        validation_errors.append(validation_error)
    lambda_errors.append(np.mean(validation_errors))
print(lambda_errors)
plt.semilogx(lambda_set[1:], lambda_errors[1:], label='Average validation set error')
plt.xlabel('Lambda Value (log scale)')
plt.ylabel('Average Validation Set Error')
plt.title('Average Validation Set Error vs. Lambda Value on log Scale')
plt.axhline(y=lambda_errors[0], linewidth=2, color='g', label='Unregularized result, Lambda = 0')
plt.legend()
plt.show()