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
if __name__ == "__main__":
    data = np.array([1, 2, 3, 4, 5])
    normal_scaler = NormalScaler()
    normal_scaler.fit(data)
    transformed_data = normal_scaler.transform(data)
    print("Normalized data:", transformed_data)
    minmax_scaler = MinMaxScaler()
    minmax_scaler.fit(data)
    transformed_data = minmax_scaler.transform(data)
    print("Min-Max scaled data:", transformed_data)
    original_data = minmax_scaler.inv_transform(transformed_data)
    print("Inverse transformed data:", original_data)