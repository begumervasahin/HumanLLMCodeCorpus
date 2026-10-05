
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
class Model:
    X = None
    Y = None
    standardScaler = None
    def importData(self):
        dataset = pd.read_csv('supermall.csv')
        self.X = dataset.iloc[:, [2,3]].values
        self.Y = dataset.iloc[:, 4].values
    def doFatureScaling(self):
        self.standardScaler = StandardScaler()
        self.X = self.standardScaler.fit_transform(self.X)
    def isBuying(self):
        self.importData()
        self.doFatureScaling()
        classifier = GaussianNB()
        classifier.fit(self.X, self.Y)
        userAge = float(raw_input("Enter the user's age? "))
        userSalary = float(raw_input("What is the salary of user? "))
        testData = self.standardScaler.transform([[userAge, userSalary]])
        prediction = classifier.predict(testData)
        print 'This user is most likely to buy the product' if  prediction[0] == 1 else 'This user is not gonna buy the your product.'
model = Model()
model.isBuying()