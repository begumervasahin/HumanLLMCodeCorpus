
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
class class1:
    b1 = None
    b2 = None
    b3 = None
    def fonk1(self):
        b4 = pd.read_csv('supermall.csv')
        self.b1 = b4.iloc[:, [2,3]].values
        self.b2 = b4.iloc[:, 4].values
    def fonk2(self):
        self.b3 = StandardScaler()
        self.b1 = self.b3.fit_transform(self.b1)
    def fonk3(self):
        self.fonk1()
        self.fonk2()
        b5 = GaussianNB()
        b5.fit(self.b1, self.b2)
        b6 = float(raw_input("Enter the user's age? "))
        b7 = float(raw_input("What is the salary of user? "))
        b8 = self.b3.transform([[b6, b7]])
        b9 = b5.predict(b8)
        print 'This user is most likely to buy the product' if  b9[0] == 1 else 'This user is not gonna buy the your product.'
b10 = class1()
b10.fonk3()