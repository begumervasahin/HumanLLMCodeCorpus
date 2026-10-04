
import numpy as np
class NormalScaler:
    def fit(self, arr):
        self.mean = np.mean(arr)
        self.std = np.std(arr)
    def transform(self, arr):
        return (arr - self.mean) / self.std
class MinMaxScaler:
    def fit(self, arr):
        self.min = np.min(arr)
        self.max = np.max(arr)
    def transform(self, arr):
        return (arr - self.min) / (self.max - self.min)
    def inv_transform(self, arr):
        return arr * (self.max - self.min) + self.min