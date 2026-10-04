
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
class class1:
    def fonk1(self):
        self.b1 = None
        self.b2 = None
        self.b3 = None
    def fonk2(self, b4 = 'supermall.csv'):
        b5 = pd.read_csv(b4)
        self.b1 = b5.iloc[:, [2, 3]].values
        self.b2 = b5.iloc[:, 4].values
    def fonk3(self):
        self.b3 = StandardScaler()
        self.b1 = self.b3.fit_transform(self.b1)
    def fonk4(self):
        self.fonk2()
        self.fonk3()
        b6 = GaussianNB()
        b6.fit(self.b1, self.b2)
        b7 = float(input("Enter the user's age: "))
        b8 = float(input("What is the salary of the user? "))
        b9 = self.b3.transform([[b7, b8]])
        b10 = b6.predict(b9)
        if b10[0] == 1:
            print('This user is most likely to buy the product.')
        else:
            print('This user is not likely to buy your product.')
if b11 = = "__main__":
    b12 = class1()
    b12.fonk4()