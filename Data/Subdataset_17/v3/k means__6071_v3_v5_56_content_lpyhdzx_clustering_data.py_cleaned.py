import pandas as pd
class DataLoader:
    def __init__(self, target=None, path=None):
        self.target = target
        self.path = path
    def load_data(self):
        df = pd.read_csv(self.path)
        filtered_data = df[df['V1'].isin(self.target)].iloc[:, 1:]
        return filtered_data
class ThresholdDataLoader(DataLoader):
    def load_data(self):
        filtered_data = super().load_data()
        filtered_data[filtered_data < 0.8] = -1
        return filtered_data
def main():
    train_loader = DataLoader(target=[5, 6], path='zip_train.csv')
    train_data = train_loader.load_data()
    print("Training Data:")
    print(train_data)
    test_loader = DataLoader(target=[5, 6], path='zip_test.csv')
    test_data = test_loader.load_data()
    print("Test Data:")
    print(test_data)
    threshold_train_loader = ThresholdDataLoader(target=[5, 6], path='zip_train.csv')
    threshold_train_data = threshold_train_loader.load_data()
    print("Thresholded Training Data:")
    print(threshold_train_data)
    threshold_test_loader = ThresholdDataLoader(target=[5, 6], path='zip_test.csv')
    threshold_test_data = threshold_test_loader.load_data()
    print("Thresholded Test Data:")
    print(threshold_test_data)
if __name__ == '__main__':
    main()