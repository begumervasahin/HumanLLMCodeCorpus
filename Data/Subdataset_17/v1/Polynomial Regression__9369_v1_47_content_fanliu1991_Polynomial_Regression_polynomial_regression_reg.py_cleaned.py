import numpy as np
import matplotlib.pyplot as plt
import assignment1 as a1
(countries, features, values) = a1.load_unicef_data()
targets = values[:, 1]
x = values[:, 7:]
x = a1.normalize_data(x)
N_TRAIN = 100
x_train = x[0:N_TRAIN, :]
t_train = targets[0:N_TRAIN]
lambda_set = [0, 0.01, 0.1, 1, 10, 100, 1000, 10000]
w0_term_train = np.ones(shape=(N_TRAIN, 1))
phi = w0_term_train
for degree_index in range(2):
    degree = degree_index + 1
    phi = np.concatenate((phi, np.power(x_train, degree)), axis=1)
coefficient_M = np.shape(phi)[1]
identity_matrix = np.identity(coefficient_M)
partition = N_TRAIN
lambda_error = []
for lambda_value in lambda_set:
    validation_error = []
    for validation_index in range(10):
        validation_set_start = validation_index * partition
        validation_set_end = validation_set_start + partition
        validation_phi = phi[validation_set_start:validation_set_end, :]
        validation_t = t_train[validation_set_start:validation_set_end]
        training_phi = np.concatenate((phi[:validation_set_start, :], phi[validation_set_end:, :]), axis=0)
        training_t = np.concatenate((t_train[:validation_set_start], t_train[validation_set_end:]), axis=0)
        w = np.linalg.inv(lambda_value * identity_matrix + training_phi.T @ training_phi) @ training_phi.T @ training_t
        validation_partition_error = np.sqrt(0.5 * np.sum((validation_phi @ w - validation_t) ** 2) * 2 / len(validation_t))
        validation_error.append(validation_partition_error)
    lambda_error.append(np.mean(validation_error))
print(lambda_error)
plt.semilogx(lambda_set[1:], lambda_error[1:])
plt.xlabel('Lambda Value on log Scale')
plt.ylabel('Average Validation Set Error')
plt.title('Average Validation Set Error vs. Lambda Value on log Scale')
plt.axhline(y=lambda_error[0], linewidth=2, color='g')
plt.legend(['Average validation set error', 'Unregularized result, Lambda = 0'])
plt.show()