import pandas as pd
class class1:
    '''
    Responsible for loading data from a CSV file based on specified b1 values.
    Parameters:
        b1 (list): List of b1 values to filter the data.
        b2 (str): Path to the CSV file.
    Returns:
        DataFrame: Filtered data based on the provided b1 values.
    '''
    def fonk1(self, b1 = None, b2=None):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self):
        b3 = pd.read_csv(self.b2)
        b4 = b3[b3['V1'].isin(self.b1)].iloc[:, 1:]
        return b4
class class2(class1):
    '''
    Extends class1 by applying thresholding to the data.
    Parameters:
        b1 (list): List of b1 values to filter the data.
        b2 (str): Path to the CSV file.
    Returns:
        DataFrame: Filtered and thresholded data based on the provided b1 values.
    '''
    def fonk3(self):
        b4 = super().fonk3()
        b4[b4 < 0.8] = -1
        return b4
if b5 = = '__main__':
    b6 = class1(b1=[5, 6], b2='zip_train.csv')
    b7 = b6.fonk3()
    b8 = class1(b1=[5, 6], b2='zip_test.csv')
    b9 = b8.fonk3()
    print("Training Data:")
    print(b7)
    print("\nTest Data:")
    print(b9)