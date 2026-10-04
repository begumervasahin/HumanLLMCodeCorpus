import numpy as np
from matplotlib import pyplot as plt
class SVM:
    def __init__(self, visualize=True):
        self.visualize = visualize
        self.colors = {1: 'r', -1: 'b'}
        if self.visualize:
            self.fig, self.ax = plt.subplots()
    def train(self, data):
        self.data = data
        opt_dict = {}
        transforms = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
        self.max_feature_value = max(max(features) for label in data for features in data[label])
        self.min_feature_value = min(min(features) for label in data for features in data[label])
        step_sizes = [self.max_feature_value * factor for factor in [0.1, 0.01, 0.001]]
        b_range_multiple = 5
        b_multiple = 5
        latest_optimum = self.max_feature_value * 10
        for step in step_sizes:
            w = np.array([latest_optimum, latest_optimum])
            optimized = False
            while not optimized:
                for b in np.arange(-self.max_feature_value * b_range_multiple,
                                   self.max_feature_value * b_range_multiple,
                                   step * b_multiple):
                    for transformation in transforms:
                        w_t = w * transformation
                        found_option = True
                        for label in data:
                            for x in data[label]:
                                if not label * (np.dot(w_t, x) + b) >= 1:
                                    found_option = False
                                    break
                            if not found_option:
                                break
                        if found_option:
                            opt_dict[np.linalg.norm(w_t)] = [w_t, b]
                if w[0] < 0:
                    optimized = True
                else:
                    w -= step
            norms = sorted(opt_dict.keys())
            opt_choice = opt_dict[norms[0]]
            self.w, self.b = opt_choice
            latest_optimum = opt_choice[0][0] + step * 2
    def predict(self, features):
        classification = np.sign(np.dot(np.array(features), self.w) + self.b)
        if classification != 0 and self.visualize:
            self.ax.scatter(features[0], features[1], s=300, marker='*', c=self.colors[classification])
        return classification
    def visualize(self):
        for label in self.data:
            for x in self.data[label]:
                self.ax.scatter(x[0], x[1], s=50, c=self.colors[label])
        def hyperplane(x, w, b, v):
            return (-w[0] * x - b + v) / w[1]
        datarange = (self.min_feature_value * 0.9, self.max_feature_value * 1.1)
        hyp_x_min, hyp_x_max = datarange
        for v, color in zip([1, -1, 0], ['k', 'k', 'y--']):
            p1 = hyperplane(hyp_x_min, self.w, self.b, v)
            p2 = hyperplane(hyp_x_max, self.w, self.b, v)
            self.ax.plot([hyp_x_min, hyp_x_max], [p1, p2], color)
        plt.show()
if __name__ == '__main__':
    data_set = {
        -1: np.array([[1, 7], [2, 8], [3, 8]]),
        1: np.array([[5, 1], [6, -1], [7, 3]])
    }
    svm = SVM()
    svm.train(data_set)
    test_points = [[0, 10], [2, 6], [1, 3], [4, 3], [5.5, 7.5], [8, 3]]
    for point in test_points:
        print(f"Prediction for {point}: {svm.predict(point)}")
    svm.visualize()