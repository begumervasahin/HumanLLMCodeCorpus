import pandas as pd
class DataLoader:
    '''
    Responsible for loading data from a CSV file based on specified target values.
    Parameters:
        target (list): List of target values to filter the data.
        path (str): Path to the CSV file.
    Returns:
        DataFrame: Filtered data based on the provided target values.
    '''
    def __init__(self, target=None, path=None):
        self.target = target
        self.path = path
    def load_data(self):
        dataset = pd.read_csv(self.path)
        filtered_data = dataset[dataset['V1'].isin(self.target)].iloc[:, 1:]
        return filtered_data
class ThresholdDataLoader(DataLoader):
    '''
    Extends DataLoader by applying thresholding to the data.
    Parameters:
        target (list): List of target values to filter the data.
        path (str): Path to the CSV file.
    Returns:
        DataFrame: Filtered and thresholded data based on the provided target values.
    '''
    def load_data(self):
        filtered_data = super().load_data()
        filtered_data[filtered_data < 0.8] = -1
        return filtered_data
if __name__ == '__main__':
    train_loader = DataLoader(target=[5, 6], path='zip_train.csv')
    train_data = train_loader.load_data()
    test_loader = DataLoader(target=[5, 6], path='zip_test.csv')
    test_data = test_loader.load_data()
    print("Training Data:")
    print(train_data)
    print("\nTest Data:")
    print(test_data)