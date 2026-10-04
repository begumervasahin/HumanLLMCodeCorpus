
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
class class1:
    def fonk1(self):
        self.b1 = None
        self.b2 = None
        self.b3 = None
    def fonk2(self):
        b4 = pd.read_csv('supermall.csv')
        self.b1 = b4.iloc[:, [2, 3]].values
        self.b2 = b4.iloc[:, 4].values
    def fonk3(self):
        self.b3 = StandardScaler()
        self.b1 = self.b3.fit_transform(self.b1)
    def fonk4(self):
        self.fonk2()
        self.fonk3()
        b5 = GaussianNB()
        b5.fit(self.b1, self.b2)
        b6 = float(input("Enter the user's age: "))
        b7 = float(input("What is the salary of the user: "))
        b8 = self.b3.transform([[b6, b7]])
        b9 = b5.predict(b8)
        if b9[0] == 1:
            print('This user is most likely to buy the product.')
        else:
            print('This user is not going to buy your product.')
if b10 = = "__main__":
    b11 = class1()
    b11.fonk4()