import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt("crash.txt")
training = data[1::2]
test = data[0:-1:2]
training_x = training[:, 0].reshape(-1, 1)
training_t = training[:, 1].reshape(-1, 1)
test_x = test[:, 0].reshape(-1, 1)
test_t = test[:, 1].reshape(-1, 1)
num_degrees = 20
Erms_training = np.zeros(num_degrees)
Erms_test = np.zeros(num_degrees)
best_training = {"Erms": float('inf'), "L": 0, "w": None}
best_test = {"Erms": float('inf'), "L": 0, "w": None}
def compute_design_matrix(x, degree):
    return np.hstack([x ** i for i in range(degree)])
for L in range(1, num_degrees + 1):
    phi_training = compute_design_matrix(training_x, L)
    w = np.linalg.solve(phi_training.T @ phi_training, phi_training.T @ training_t)
    E_training = 0.5 * np.square(np.linalg.norm(training_t - phi_training @ w))
    Erms_training[L-1] = np.sqrt(2.0 * E_training / len(training))
    if Erms_training[L-1] < best_training["Erms"]:
        best_training["Erms"] = Erms_training[L-1]
        best_training["L"] = L
        best_training["w"] = w
    phi_test = compute_design_matrix(test_x, L)
    E_test = 0.5 * np.square(np.linalg.norm(test_t - phi_test @ w))
    Erms_test[L-1] = np.sqrt(2.0 * E_test / len(test))
    if Erms_test[L-1] < best_test["Erms"]:
        best_test["Erms"] = Erms_test[L-1]
        best_test["L"] = L
        best_test["w"] = w
print('Maximum likelihood RMS error between the actual data and the model\'s prediction (for Training sets): \n', Erms_training)
print('Maximum likelihood RMS error between the actual data and the model\'s prediction (for Test sets): \n', Erms_test)
plt.figure(figsize=(16, 12))
plt.plot(Erms_training, '-o', markerfacecolor='none', color='b', label='Training')
plt.plot(Erms_test, '-o', markerfacecolor='none', color='r', label='Test')
plt.suptitle('Maximum likelihood RMS error between the actual data and the model\'s prediction', fontsize=24)
plt.legend(fontsize=22)
plt.xlabel("Polynomial Degree (M)", fontsize=22)
plt.ylabel("Erms", fontsize=22)
plt.show()
def plot_best_fit(x, t, title, best_model):
    x_fit = np.linspace(np.min(x), np.max(x), 100).reshape(-1, 1)
    phi_fit = compute_design_matrix(x_fit, best_model["L"])
    y_fit = phi_fit @ best_model["w"]
    plt.figure(figsize=(16, 12))
    plt.plot(x, t, 'bo', label='Data')
    plt.plot(x_fit, y_fit, 'r-', label='Best fit model')
    plt.suptitle(title, fontsize=24)
    plt.legend(fontsize=22)
    plt.xlabel("Time", fontsize=22)
    plt.ylabel("Acceleration", fontsize=22)
    plt.show()
print('Lowest RMS L for training data:', best_training["L"])
plot_best_fit(training_x, training_t, 'Best fit on the training set', best_training)
print('Lowest RMS L for test data:', best_test["L"])
plot_best_fit(test_x, test_t, 'Best fit on the test set', best_test)