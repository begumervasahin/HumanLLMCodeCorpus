
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
class class1:
    def fonk1(self):
        self.b1 = None
        self.b2 = None
        self.b3 = StandardScaler()
        self.b4 = GaussianNB()
    def fonk2(self, b5 = 'supermall.csv'):
        b6 = pd.read_csv(b5)
        self.b1 = b6.iloc[:, [2, 3]].values
        self.b2 = b6.iloc[:, 4].values
    def fonk3(self):
        self.b1 = self.b3.fit_transform(self.b1)
    def fonk4(self):
        self.b4.fit(self.b1, self.b2)
    def fonk5(self, age, salary):
        b7 = self.b3.transform([[age, salary]])
        b8 = self.b4.predict(b7)
        return b8[0]
    def fonk6(self):
        self.fonk2()
        self.fonk3()
        self.fonk4()
        try:
            b9 = float(input("Enter the user's age: "))
            b10 = float(input("What is the salary of the user? "))
        except ValueError:
            print("Invalid input. Please enter numeric values for age and salary.")
            return
        b8 = self.fonk5(b9, b10)
        if b8 = = 1:
            print('This user is most likely to buy the product.')
        else:
            print('This user is not likely to buy your product.')
if b11 = = "__main__":
    b12 = class1()
    b12.fonk6()