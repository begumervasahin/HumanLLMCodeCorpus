import pandas as pd
class class1:
    '''
    input: b1: list[], b2: str
    return: data(num,257) returns vectors containing only the specified targets
    '''
    def fonk1(self, b1 = None, b2=None):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self):
        b3 = pd.read_csv(self.b2)
        b4 = pd.DataFrame(b3)
        b5 = self.b1
        b6 = b4.iloc[:, 1:][b4['V1'].isin(b5)]
        return b6
class class2(class1):
    '''
    input: b1: list[], b2: str
    return: Thresholded data (num,257)
    '''
    def fonk3(self):
        b3 = pd.read_csv(self.b2)
        b4 = pd.DataFrame(b3)
        b5 = self.b1
        b6 = b4.iloc[:, 1:][b4['V1'].isin(b5)]
        b6[b6 < 0.8] = -1
        return b6
if b7 = = '__main__':
    b8 = class1(b1=[5, 6], b2='zip_train.csv')
    b9 = b8.fonk3()
    b10 = class1(b1=[5, 6], b2='zip_test.csv')
    b11 = b10.fonk3()
    print(b9)