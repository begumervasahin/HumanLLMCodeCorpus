import numpy as np
import matplotlib.pyplot as plt
def read_idx(filename, offset):
    with open(filename, 'rb') as file:
        data = file.read()
    data = bytearray(data)
    data = data[offset:]
    return np.array(data, dtype="float64")
def preprocess_images(filename, offset, threshold=100.0):
    images = read_idx(filename, offset) > threshold
    return images
def visualize_images(images, image_size=(28, 28), grid_size=(20, 20)):
    fig = plt.figure()
    for k in range(grid_size[0] * grid_size[1]):
        a = fig.add_subplot(grid_size[0], grid_size[1], k + 1)
        plt.imshow(images[k].reshape(image_size), cmap=plt.cm.bone)
        a.set_axis_off()
    plt.show()
def calculate_class_priors(labels, num_classes):
    counts = np.bincount(labels.astype(int), minlength=num_classes)
    priors = counts / len(labels)
    log_priors = np.log10(priors)
    return priors, log_priors
def calculate_class_conditional_probabilities(images, labels, num_classes):
    num_pixels = images.shape[1]
    theta = np.zeros((num_classes, num_pixels), dtype="float64")
    for i in range(num_classes):
        mask = (labels == i)
        theta[i] = (np.sum(images[mask], axis=0, dtype="float64") + 1.0) / (mask.sum() + num_classes)
    log_theta = np.log10(theta)
    log_complement = np.log10(1.0 - theta)
    return log_theta, log_complement
def classify_images(test_images, log_priors, log_theta, log_complement):
    num_classes = log_priors.shape[0]
    num_test_images = test_images.shape[0]
    test_labels_hat = np.zeros((num_test_images, 1))
    for i in range(num_test_images):
        log_likelihood = (
            np.sum(log_theta[:, test_images[i].astype(bool)], axis=1) +
            np.sum(log_complement[:, np.logical_not(test_images[i].astype(bool))], axis=1)
        )
        log_posterior = log_priors + log_likelihood
        test_labels_hat[i] = np.argmax(log_posterior)
    return test_labels_hat
def calculate_accuracy(true_labels, predicted_labels):
    accuracy = np.sum(true_labels == predicted_labels) / len(true_labels) * 100
    return accuracy
def main():
    training_images = preprocess_images('train-images.idx3-ubyte', 16)
    training_labels = read_idx('train-labels.idx1-ubyte', 8)
    training_images = training_images.reshape(-1, 28 * 28)
    visualize_images(training_images)
    num_classes = 10
    priors, log_priors = calculate_class_priors(training_labels, num_classes)
    log_theta, log_complement = calculate_class_conditional_probabilities(training_images, training_labels, num_classes)
    test_images = preprocess_images('t10k-images.idx3-ubyte', 16)
    test_labels = read_idx('t10k-labels.idx1-ubyte', 8)
    test_images = test_images.reshape(-1, 28 * 28)
    test_labels_hat = classify_images(test_images, log_priors, log_theta, log_complement)
    accuracy = calculate_accuracy(test_labels, test_labels_hat)
    print("Naive Bayes classifier classification accuracy: {:.2f}%".format(accuracy))
if __name__ == "__main__":
    main()