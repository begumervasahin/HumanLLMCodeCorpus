
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
class class1:
    def fonk1(self):
        self.b1 = None
        self.b2 = None
        self.b3 = StandardScaler()
        self.b4 = GaussianNB()
    def fonk2(self, file_path):
        b5 = pd.read_csv(file_path)
        self.b1 = b5.iloc[:, [2, 3]].values
        self.b2 = b5.iloc[:, 4].values
    def fonk3(self):
        self.b1 = self.b3.fit_transform(self.b1)
    def fonk4(self):
        try:
            b6 = float(input("Enter the user's age: "))
            b7 = float(input("What is the salary of the user: "))
            return b6, b7
        except ValueError:
            print("Invalid input. Please enter numerical values for age and salary.")
            return None, None
    def fonk5(self, b6, b7):
        b8 = self.b3.transform([[b6, b7]])
        b9 = self.b4.predict(b8)
        return b9[0] == 1
    def fonk6(self):
        self.fonk2('supermall.csv')
        self.fonk3()
        self.b4.fit(self.b1, self.b2)
        b6, b7 = self.fonk4()
        if b6 is not None and b7 is not None:
            if self.fonk5(b6, b7):
                print('This user is most likely to buy the product.')
            else:
                print('This user is not going to buy your product.')
if b10 = = "__main__":
    b11 = class1()
    b11.fonk6()