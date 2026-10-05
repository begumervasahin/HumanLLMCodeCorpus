import pandas as pd
class DataLoader:
    def __init__(self, target=None, path=None):
        self.target = target
        self.path = path
    def load_data(self):
        dataset = pd.read_csv(self.path)
        df = pd.DataFrame(dataset)
        target_values = self.target
        filtered_data = df.iloc[:, 1:][df['V1'].isin(target_values)]
        return filtered_data
class NewData(DataLoader):
    def load_data(self):
        dataset = pd.read_csv(self.path)
        df = pd.DataFrame(dataset)
        target_values = self.target
        filtered_data = df.iloc[:, 1:][df['V1'].isin(target_values)]
        filtered_data[filtered_data < 0.8] = -1
        return filtered_data
if __name__ == '__main__':
    train_loader = DataLoader(target=[5, 6], path='zip_train.csv')
    train_data = train_loader.load_data()
    test_loader = DataLoader(target=[5, 6], path='zip_test.csv')
    test_data = test_loader.load_data()
    print(train_data)