import numpy as np
import matplotlib.pyplot as plt
def load_images(filename):
    with open(filename, 'rb') as f:
        images = f.read()
    images = bytearray(images)
    images = np.array(images[16:], dtype='float64') > 100.
    return images
def load_labels(filename):
    with open(filename, 'rb') as f:
        labels = f.read()
    labels = bytearray(labels)
    labels = np.array(labels[8:])
    return labels
def plot_images(images, num_images=400, cols=20):
    d = 28 * 28
    rows = num_images
    fig = plt.figure(figsize=(10, 10))
    for k in range(num_images):
        ax = fig.add_subplot(rows, cols, k + 1)
        plt.imshow(images[k*d:(k+1)*d].reshape(28, 28), cmap=plt.cm.bone)
        ax.set_axis_off()
    plt.show()
def calculate_priors(labels, num_classes):
    counts = np.bincount(labels, minlength=num_classes)
    priors = counts / len(labels)
    log_priors = np.log10(priors)
    return log_priors
def calculate_likelihoods(images, labels, num_classes, num_features):
    theta = np.zeros((num_classes, num_features), dtype='float64')
    for i in range(num_classes):
        class_mask = (labels == i)
        theta[i] = (np.sum(images[class_mask], axis=0, dtype='float64') + 1.) / (np.sum(class_mask) + num_classes)
    log_theta = np.log10(theta)
    log_complement = np.log10(1. - theta)
    return log_theta, log_complement
def predict_labels(test_images, log_prior, log_theta, log_complement):
    num_tests = test_images.shape[0]
    num_classes = log_prior.shape[0]
    predictions = np.zeros(num_tests, dtype=int)
    for i in range(num_tests):
        log_likelihood = np.sum(log_theta[:, test_images[i].reshape(-1)], axis=1) + \
                         np.sum(log_complement[:, np.logical_not(test_images[i].reshape(-1))], axis=1)
        log_posterior = log_prior + log_likelihood
        predictions[i] = np.argmax(log_posterior)
    return predictions
def main():
    train_images = load_images('train-images.idx3-ubyte')
    train_labels = load_labels('train-labels.idx1-ubyte')
    plot_images(train_images)
    d = 28 * 28
    n_train = train_images.shape[0]
    train_images = train_images.reshape(int(n_train), d)
    k = 10
    log_prior = calculate_priors(train_labels, k)
    log_theta, log_complement = calculate_likelihoods(train_images, train_labels, k, d)
    test_images = load_images('t10k-images.idx3-ubyte')
    test_labels = load_labels('t10k-labels.idx1-ubyte')
    n_test = test_images.shape[0]
    test_images = test_images.reshape(int(n_test), d)
    test_labels_hat = predict_labels(test_images, log_prior, log_theta, log_complement)
    accuracy = np.mean(test_labels == test_labels_hat)
    print("Naive Bayes classifier classification accuracy:", accuracy * 100., '%')
if __name__ == "__main__":
    main()