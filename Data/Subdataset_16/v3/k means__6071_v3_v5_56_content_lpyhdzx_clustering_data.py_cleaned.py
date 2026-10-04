import pandas as pd
class class1:
    def fonk1(self, b1 = None, b2=None):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self):
        b3 = pd.read_csv(self.b2)
        b4 = b3[b3['V1'].isin(self.b1)].iloc[:, 1:]
        return b4
class class2(class1):
    def fonk3(self):
        b4 = super().fonk3()
        b4[b4 < 0.8] = -1
        return b4
def fonk4():
    b5 = class1(b1=[5, 6], b2='zip_train.csv')
    b6 = b5.fonk3()
    print("Training Data:")
    print(b6)
    b7 = class1(b1=[5, 6], b2='zip_test.csv')
    b8 = b7.fonk3()
    print("Test Data:")
    print(b8)
    b9 = class2(b1=[5, 6], b2='zip_train.csv')
    b10 = b9.fonk3()
    print("Thresholded Training Data:")
    print(b10)
    b11 = class2(b1=[5, 6], b2='zip_test.csv')
    b12 = b11.fonk3()
    print("Thresholded Test Data:")
    print(b12)
if b13 = = '__main__':
    fonk4()