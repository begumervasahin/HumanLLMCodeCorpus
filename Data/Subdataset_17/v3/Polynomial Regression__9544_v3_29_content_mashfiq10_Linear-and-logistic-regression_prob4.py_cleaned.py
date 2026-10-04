import numpy as np
from scipy.optimize import minimize
def flower_to_float(s):
    flower_dict = {b'Iris-setosa': 0., b'Iris-versicolor': 1., b'Iris-virginica': 2.}
    return flower_dict[s]
def phi(x, i):
    phi_vector = np.ones(5)
    phi_vector[1:5] = x[i, 1:5]
    return phi_vector
def log_likelihood(w, training_x, training_y, prior):
    N, K = training_x.shape[0], 3
    log_likelihood_value = 0.
    for n in range(N):
        ll2, ll3 = 0., 0.
        for k in range(K):
            ll2 += training_y[n, k] * w[5*k:(5*k)+5].T.dot(phi(training_x, n))
        for l in range(K):
            ll3 += np.exp(w[5*l:(5*l)+5].T.dot(phi(training_x, n)))
        log_likelihood_value += ll2 - np.log(ll3)
        if log_likelihood_value == -np.inf:
            log_likelihood_value = 0.
    return prior - log_likelihood_value
def load_and_preprocess_data(file_path):
    irises = np.loadtxt(file_path, delimiter=',', converters={4: flower_to_float})
    M = irises.shape[0]
    x = np.concatenate((np.ones(shape=(M, 1)), irises[:, :4]), axis=1)
    y = np.zeros(shape=(M, 3))
    for i in range(M):
        y[i, int(irises[i, 4])] = 1
    return x, y, M
def shuffle_and_split_data(x, y, M, train_ratio=0.5):
    indices = np.arange(M)
    np.random.shuffle(indices)
    x, y = x[indices], y[indices]
    train_size = int(M * train_ratio)
    training_x, training_y = x[:train_size], y[:train_size]
    test_x, test_y = x[train_size:], y[train_size:]
    return training_x, training_y, test_x, test_y
def predict(test_x, w_hat, K):
    predicted_labels = []
    for i in range(test_x.shape[0]):
        z = np.array([np.exp(w_hat[5*k:(5*k)+5].T.dot(phi(test_x, i))) for k in range(K)])
        z[z == np.inf] = 1000.
        s = z / np.sum(z)
        predicted_labels.append(np.argmax(s))
    return predicted_labels
def calculate_accuracy(predicted_labels, test_y):
    true_labels = [np.argmax(test_y[i, :]) for i in range(test_y.shape[0])]
    accuracy = np.mean(np.equal(predicted_labels, true_labels)) * 100.
    return accuracy
def main():
    x, y, M = load_and_preprocess_data('iris.txt')
    training_x, training_y, test_x, test_y = shuffle_and_split_data(x, y, M)
    alpha = 0.0031257
    w_init = np.ones(15)
    prior = (alpha / 2.) * w_init.T.dot(w_init)
    w_hat = minimize(log_likelihood, w_init, args=(training_x, training_y, prior)).x
    predicted_labels = predict(test_x, w_hat, K=3)
    accuracy = calculate_accuracy(predicted_labels, test_y)
    print("Overall classification accuracy = {:.2f}%".format(accuracy))
if __name__ == "__main__":
    main()