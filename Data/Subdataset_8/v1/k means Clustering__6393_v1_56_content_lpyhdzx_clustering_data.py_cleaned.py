import pandas as pd
class DataLoader:
    '''
    input: target: list[], path: str
    return: data(num,257) returns vectors containing only the specified targets
    '''
    def __init__(self, target=None, path=None):
        self.target = target
        self.path = path
    def load_data(self):
        dataset = pd.read_csv(self.path)
        df = pd.DataFrame(dataset)
        index = self.target
        df_data = df.iloc[:, 1:][df['V1'].isin(index)]
        return df_data
class NewData(DataLoader):
    '''
    input: target: list[], path: str
    return: Thresholded data (num,257)
    '''
    def load_data(self):
        dataset = pd.read_csv(self.path)
        df = pd.DataFrame(dataset)
        index = self.target
        df_data = df.iloc[:, 1:][df['V1'].isin(index)]
        df_data[df_data < 0.8] = -1
        return df_data
if __name__ == '__main__':
    loader = DataLoader(target=[5, 6], path='zip_train.csv')
    data_train = loader.load_data()
    loader_test = DataLoader(target=[5, 6], path='zip_test.csv')
    data_test = loader_test.load_data()
    print(data_train)