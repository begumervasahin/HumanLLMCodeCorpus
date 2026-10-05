import sys
import numpy as np
import scipy.cluster.vq as vq
class Classifier:
    def __init__(self, classifier_type):
        '''Initialize the classifier with a given type'''
        self._type = classifier_type
    def type(self, new_type=None):
        '''Get or set the type of the classifier'''
        if new_type is not None:
            self._type = new_type
        return self._type
    def confusion_matrix(self, true_cats, class_cats):
        '''Compute the confusion matrix'''
        true_cats = true_cats.T.tolist()[0]
        class_cats = class_cats.T.tolist()[0]
        unique_true, mappings_true = np.unique(true_cats, return_inverse=True)
        unique_class, mappings_class = np.unique(class_cats, return_inverse=True)
        conf_matrix = np.zeros((len(unique_true), len(unique_true)))
        for i in range(len(class_cats)):
            conf_matrix[class_cats[i], true_cats[i]] += 1
        return conf_matrix
    def confusion_matrix_str(self, cmtx):
        '''Convert the confusion matrix to a printable string'''
        s = 'Confusion Matrix\n'
        s += '          '
        for i in range(cmtx.shape[0]):
            s += f" TrueC{i}"
        l = np.array([f"PredC{i}" for i in range(cmtx.shape[0])]).reshape(-1, 1)
        cmtx = np.hstack((l, cmtx))
        s += "\n"
        for row in cmtx:
            s += ' '.join(map(str, row)) + "\n"
        return s
    def __str__(self):
        '''Convert the classifier object to a string'''
        return str(self._type)
class NaiveBayes(Classifier):
    '''Class for Naive Bayes classifier'''
    def __init__(self, data_obj=None, headers=[], categories=None):
        '''Initialize Naive Bayes classifier'''
        super().__init__('Naive Bayes Classifier')
        self.headers = headers
        self.num_features = len(headers)
        self.num_classes = None
        self.categories = categories
        self.means = []
        self.variances = []
        self.scales = []
        if data_obj is not None:
            A = data_obj.get_data(headers)
            self.build(A, categories)
    def build(self, A, categories):
        '''Build Naive Bayes classifier'''
        unique, mapping = np.unique(np.array(categories.T), return_inverse=True)
        self.num_classes = len(unique)
        self.num_features = A.shape[1]
        self.categories = categories
        self.means = np.zeros((self.num_classes, self.num_features))
        self.variances = np.zeros((self.num_classes, self.num_features))
        self.scales = np.zeros((self.num_classes, self.num_features))
        for i in range(self.num_classes):
            class_data = A[(mapping == i), :]
            self.means[i, :] = np.mean(class_data, axis=0)
            self.variances[i, :] = np.var(class_data, axis=0)
            self.scales[i, :] = 1 / (np.sqrt(2 * np.pi * self.variances[i, :]))
        return
    def classify(self, A, return_likelihoods=False):
        '''Classify using Naive Bayes'''
        if A.shape[1] != self.means.shape[1]:
            print("Error")
            return
        P = np.zeros((A.shape[0], self.num_classes))
        for i in range(self.num_classes):
            P[:, i] = np.prod(np.multiply(self.scales[i,:], np.exp(-(np.square(A - self.means[i,:]))/(2*self.variances[i,:]))), axis=1)
        cats = np.argmax(P, axis=1)
        labels = self.categories[cats]
        if return_likelihoods:
            return cats, labels, P
        return cats, labels
    def __str__(self):
        '''Convert NaiveBayes object to a string'''
        s = "\nNaive Bayes Classifier\n"
        for i in range(self.num_classes):
            s += f'Class {i} --------------------\n'
            s += f'Mean  : {self.means[i, :]}\n'
            s += f'Var   : {self.variances[i, :]}\n'
            s += f'Scales: {self.scales[i, :]}\n'
        s += "\n"
        return s
    def write(self, filename):
        '''Write NaiveBayes classifier to a file'''
        pass
    def read(self, filename):
        '''Read NaiveBayes classifier from a file'''
        pass
class KNN(Classifier):
    '''Class for K Nearest Neighbors classifier'''
    def __init__(self, data_obj=None, headers=[], categories=None, K=None):
        '''Initialize KNN classifier'''
        super().__init__('KNN Classifier')
        self.headers = headers
        self.num_features = len(headers)
        self.num_classes = 0
        self.categories = categories
        self.exemplars = []
        if data_obj is not None:
            self.data_obj = data_obj
            A = data_obj.get_data(headers)
            self.build(A, categories)
    def build(self, A, categories, K=None):
        '''Build KNN classifier'''
        unique, mapping = np.unique(np.array(categories.T), return_inverse=True)
        self.num_classes = len(unique)
        self.num_features = A.shape[0]
        self.categories = categories
        for i in range(self.num_classes):
            if K is None:
                self.exemplars.append(A[(mapping == i), :])
            else:
                codebook, codes = vq.kmeans(A[(mapping == i), :], K)
                self.exemplars.append(codebook)
        return
    def classify(self, A, K=3, return_distances=False):
        '''Classify using KNN'''
        D = np.zeros((A.shape[0], self.num_classes))
        print("Classifying using KNN")
        for i in range(self.num_classes):
            temp = np.zeros((A.shape[0], self.exemplars[i].shape[0]))
            for j in range(self.exemplars[i].shape[0]):
                temp[:, j] = np.sum(np.square(A - self.exemplars[i][j, :]), axis=1)
            temp = np.sort(temp, axis=1)
            D[:, i] = np.sum(temp[:, K], axis=1)
        print(D)
        cats = np.argmin(D, axis=1)
        labels = self.categories[cats]
        if return_distances:
            return cats, labels, D
        return cats, labels
    def __str__(self):
        '''Convert KNN object to a string'''
        s = "\nKNN Classifier\n"
        for i in range(self.num_classes):
            s += f'Class {i} --------------------\n'
            s += f'Number of Exemplars: {self.exemplars[i].shape[0]}\n'
            s += f'Mean of Exemplars  : {np.mean(self.exemplars[i], axis=0)}\n'
        s += "\n"
        return s
    def write(self, filename):
        '''Write KNN classifier to a file'''
        pass
    def read(self, filename):
        '''Read KNN classifier from a file'''
        pass