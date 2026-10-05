import numpy as np
import scipy.cluster.vq as vq
class Classifier:
    def __init__(self, classifier_type):
        self._type = classifier_type
    def type(self, new_type=None):
        if new_type is not None:
            self._type = new_type
        return self._type
    def confusion_matrix(self, true_categories, classified_categories):
        true_categories = true_categories.T.tolist()[0]
        classified_categories = classified_categories.T.tolist()[0]
        unique_true, mappings_true = np.unique(true_categories, return_inverse=True)
        unique_classified, mappings_classified = np.unique(classified_categories, return_inverse=True)
        conf_matrix = np.zeros((len(unique_true), len(unique_true)))
        for i in range(len(classified_categories)):
            conf_matrix[classified_categories[i], true_categories[i]] += 1
        return conf_matrix
    def confusion_matrix_str(self, confusion_matrix):
        s = 'Confusion Matrix\n'
        s += '          '
        for i in range(confusion_matrix.shape[0]):
            s += f" TrueC{i}"
        label_matrix = np.array([f"PredC{i}" for i in range(confusion_matrix.shape[0])]).reshape(-1, 1)
        confusion_matrix = np.hstack((label_matrix, confusion_matrix))
        s += "\n"
        for i in range(confusion_matrix.shape[0]):
            s += str(confusion_matrix[i, :])[1:-1] + "\n"
        return s
    def __str__(self):
        return str(self._type)
class NaiveBayes(Classifier):
    def __init__(self, data_obj=None, headers=[], categories=None):
        super().__init__('Naive Bayes Classifier')
        self.headers = headers
        self.num_features = len(headers)
        self.num_classes = None
        self.categories = categories
        self.means = []
        self.variances = []
        self.scales = []
        if data_obj is not None:
            data = data_obj.get_data(headers)
            self.build(data, categories)
    def build(self, data, categories):
        unique, mapping = np.unique(np.array(categories.T), return_inverse=True)
        self.num_classes = len(unique)
        self.num_features = data.shape[1]
        self.categories = categories
        self.means = np.zeros((self.num_classes, self.num_features))
        self.variances = np.zeros((self.num_classes, self.num_features))
        self.scales = np.zeros((self.num_classes, self.num_features))
        for i in range(self.num_classes):
            self.means[i, :] = np.mean(data[(mapping == i), :], axis=0)
            self.variances[i, :] = np.var(data[(mapping == i), :], axis=0)
            self.scales[i, :] = 1 / (np.sqrt(2 * np.pi * self.variances[i, :]))
        return
    def classify(self, data, return_likelihoods=False):
        if data.shape[1] != self.means.shape[1]:
            print("Error")
            return
        probabilities = np.zeros((data.shape[0], self.num_classes))
        for i in range(self.num_classes):
            probabilities[:, i] = np.prod(np.multiply(self.scales[i, :], np.exp(-(np.square(data - self.means[i, :])) / (2 * self.variances[i, :]))), axis=1)
        classifications = np.argmax(probabilities, axis=1)
        labels = self.categories[classifications]
        if return_likelihoods:
            return classifications, labels, probabilities
        return classifications, labels
    def __str__(self):
        s = "\nNaive Bayes Classifier\n"
        for i in range(self.num_classes):
            s += f'Class {i} --------------------\n'
            s += 'Mean  : ' + str(self.means[i, :]) + "\n"
            s += 'Var   : ' + str(self.variances[i, :]) + "\n"
            s += 'Scales: ' + str(self.scales[i, :]) + "\n"
        s += "\n"
        return s
    def write(self, filename):
        pass
    def read(self, filename):
        pass
class KNN(Classifier):
    def __init__(self, data_obj=None, headers=[], categories=None, K=None):
        super().__init__('KNN Classifier')
        self.headers = headers
        self.num_features = len(headers)
        self.num_classes = 0
        self.categories = categories
        self.exemplars = []
        if data_obj is not None:
            data = data_obj.get_data(headers)
            self.build(data, categories)
    def build(self, data, categories, K=None):
        unique, mapping = np.unique(np.array(categories.T), return_inverse=True)
        self.num_classes = len(unique)
        self.num_features = data.shape[0]
        self.categories = categories
        for i in range(self.num_classes):
            if K is None:
                self.exemplars.append(data[(mapping == i), :])
            else:
                codebook, codes = vq.kmeans(data[(mapping == i), :], K)
                self.exemplars.append(codebook)
        return
    def classify(self, data, K=3, return_distances=False):
        distances = np.zeros((data.shape[0], self.num_classes))
        print("Classifying using KNN")
        for i in range(self.num_classes):
            temp = np.zeros((data.shape[0], self.exemplars[i].shape[0]))
            for j in range(self.exemplars[i].shape[0]):
                temp[:, j] = np.sum(np.square(data - self.exemplars[i][j, :]), axis=1)
            temp = np.sort(temp, axis=1)
            distances[:, i] = np.sum(temp[:, K], axis=1)
        print(distances)
        classifications = np.argmin(distances, axis=1)
        labels = self.categories[classifications]
        if return_distances:
            return classifications, labels, distances
        return classifications, labels
    def __str__(self):
        s = "\nKNN Classifier\n"
        for i in range(self.num_classes):
            s += f'Class {i} --------------------\n'
            s += f'Number of Exemplars: {self.exemplars[i].shape[0]}\n'
            s += 'Mean of Exemplars  :' + str(np.mean(self.exemplars[i], axis=0)) + "\n"
        s += "\n"
        return s
    def write(self, filename):
        pass
    def read(self, filename):
        pass