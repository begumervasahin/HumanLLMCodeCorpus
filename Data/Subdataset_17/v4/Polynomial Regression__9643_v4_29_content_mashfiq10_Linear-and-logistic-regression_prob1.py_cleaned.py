import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt("crash.txt")
training = data[1::2]
test = data[0:-1:2]
training_x = np.array(training[:, 0]).reshape(len(training), 1)
training_t = np.array(training[:, 1]).reshape(len(training), 1)
test_x = np.array(test[:, 0]).reshape(len(test), 1)
test_t = np.array(test[:, 1]).reshape(len(test), 1)
Erms_training = np.zeros(20)
Erms_test = np.zeros(20)
Erms_reference_training = 1000.0
best_w_training = 0
best_L_training = 0
Erms_reference_test = 1000.0
best_w_test = 0
best_L_test = 0
for L in range(1, 21):
    phi_training = training_x ** np.arange(L).reshape(1, -1)
    w = np.linalg.solve(phi_training.T.dot(phi_training), phi_training.T.dot(training_t))
    E_training = 0.5 * np.square(np.linalg.norm(training_t - phi_training.dot(w)))
    Erms_training[L-1] = np.sqrt(2.0 * E_training / len(training))
    if Erms_training[L-1] < Erms_reference_training:
        Erms_reference_training = Erms_training[L-1]
        best_L_training = L
        best_w_training = w
    phi_test = test_x ** np.arange(L).reshape(1, -1)
    E_test = 0.5 * np.square(np.linalg.norm(test_t - phi_test.dot(w)))
    Erms_test[L-1] = np.sqrt(2.0 * E_test / len(test))
    if Erms_test[L-1] < Erms_reference_test:
        Erms_reference_test = Erms_test[L-1]
        best_L_test = L
        best_w_test = w
print('Maximum likelihood RMS error between the actual data and the model\'s prediction (for Training sets): \n', Erms_training)
print('Maximum likelihood RMS error between the actual data and the model\'s prediction (for Test sets): \n', Erms_test)
plt.figure(figsize=(16, 12))
plt.plot(Erms_training, '-o', markerfacecolor='none', color='b', label='Training')
plt.plot(Erms_test, '-o', markerfacecolor='none', color='r', label='Test')
plt.suptitle('Maximum likelihood RMS error between the actual data and the model\'s prediction', fontsize=24)
plt.legend(fontsize=22)
plt.xlabel("M", fontsize=22)
plt.ylabel("Erms", fontsize=22)
plt.show()
x = np.linspace(np.min(training_x), np.max(training_x), 100).reshape(100, 1)
phi = x ** np.arange(best_L_training).reshape(1, -1)
y = phi.dot(best_w_training)
print('Lowest RMS L for training data:', best_L_training)
plt.figure(figsize=(16, 12))
plt.plot(training_x, training_t, 'bo', label='Training data')
plt.plot(x, y, 'r-', label='Lowest RMS model output')
plt.suptitle('Best fit on the training set', fontsize=24)
plt.legend(fontsize=22)
plt.xlabel("time", fontsize=22)
plt.ylabel("acceleration", fontsize=22)
plt.show()
x = np.linspace(np.min(test_x), np.max(test_x), 100).reshape(100, 1)
phi = x ** np.arange(best_L_test).reshape(1, -1)
y = phi.dot(best_w_test)
print('Lowest RMS L for test data:', best_L_test)
plt.figure(figsize=(16, 12))
plt.plot(test_x, test_t, 'bo', label='Test data')
plt.plot(x, y, 'r-', label='Lowest RMS model output')
plt.suptitle('Best fit on the test set', fontsize=24)
plt.legend(fontsize=22)
plt.xlabel("time", fontsize=22)
plt.ylabel("acceleration", fontsize=22)
plt.show()