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
    def inverse_transform(self, arr):
        return arr * (self.max - self.min) + self.min
def main():
    data = np.array([1, 2, 3, 4, 5])
    normal_scaler = NormalScaler()
    normal_scaler.fit(data)
    normalized_data = normal_scaler.transform(data)
    print("Normalized data:", normalized_data)
    minmax_scaler = MinMaxScaler()
    minmax_scaler.fit(data)
    scaled_data = minmax_scaler.transform(data)
    print("Min-Max scaled data:", scaled_data)
    original_data = minmax_scaler.inverse_transform(scaled_data)
    print("Inverse transformed data:", original_data)
if __name__ == "__main__":
    main()