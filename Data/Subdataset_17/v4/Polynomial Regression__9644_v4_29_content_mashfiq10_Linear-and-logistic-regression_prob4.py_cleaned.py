import numpy as np
from scipy.optimize import minimize
def flower_to_float(s):
    species_map = {b'Iris-setosa': 0., b'Iris-versicolor': 1., b'Iris-virginica': 2.}
    return species_map[s]
def phi(x, i):
    phi_vector = np.ones(5)
    phi_vector[1:5] = x[i, 1:5]
    return phi_vector
def f(w, training_x, training_y, prior):
    N = training_x.shape[0]
    K = 3
    log_likelihood = 0.
    for n in range(N):
        ll2 = 0.
        ll3 = 0.
        for k in range(K):
            ll2 += training_y[n, k] * w[5 * k:5 * k + 5].T.dot(phi(training_x, n))
        for l in range(K):
            ll3 += np.exp(w[5 * l:5 * l + 5].T.dot(phi(training_x, n)))
        log_likelihood += ll2
        log_likelihood -= np.log(ll3)
        if log_likelihood == -np.inf:
            log_likelihood = 0.
    return prior - log_likelihood
irises = np.loadtxt('iris.txt', delimiter=',', converters={4: flower_to_float})
M = irises.shape[0]
K = 3
x = np.array(irises[:, :4])
x = np.concatenate((np.ones((M, 1)), x), axis=1)
y = np.zeros((M, K))
for i in range(M):
    y[i, int(irises[i, 4])] = 1
r = np.arange(M)
np.random.shuffle(r)
x = x[r]
y = y[r]
training_x = x[:int(M / 2)]
training_y = y[:int(M / 2)]
test_x = x[int(M / 2):]
test_y = y[int(M / 2):]
alpha = 0.0031257
w_init = np.ones(15)
prior = (alpha / 2.) * w_init.T.dot(w_init)
w_hat = minimize(f, w_init, args=(training_x, training_y, prior)).x
predicted_labels = []
true_labels = []
for i in range(test_x.shape[0]):
    z = np.zeros(K)
    for k in range(K):
        z[k] = np.exp(w_hat[5 * k:5 * k + 5].T.dot(phi(test_x, i)))
        if z[k] == np.inf:
            z[k] = 1000.
    s = z / np.sum(z)
    predicted_labels.append(np.argmax(s))
for i in range(test_y.shape[0]):
    true_labels.append(np.argmax(test_y[i, :]))
accuracy = np.mean(np.equal(predicted_labels, true_labels)) * 100.
print("Overall classification accuracy = ", accuracy, '%')