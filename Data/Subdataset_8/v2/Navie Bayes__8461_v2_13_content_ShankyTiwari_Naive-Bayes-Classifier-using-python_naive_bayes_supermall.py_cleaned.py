import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
class PurchasePredictionModel:
    def __init__(self):
        self.X = None
        self.Y = None
        self.standard_scaler = None
    def import_data(self):
        dataset = pd.read_csv('supermall.csv')
        self.X = dataset.iloc[:, [2, 3]].values
        self.Y = dataset.iloc[:, 4].values
    def do_feature_scaling(self):
        self.standard_scaler = StandardScaler()
        self.X = self.standard_scaler.fit_transform(self.X)
    def predict_purchase_likelihood(self):
        self.import_data()
        self.do_feature_scaling()
        classifier = GaussianNB()
        classifier.fit(self.X, self.Y)
        user_age = float(input("Enter the user's age: "))
        user_salary = float(input("What is the salary of the user? "))
        test_data = self.standard_scaler.transform([[user_age, user_salary]])
        prediction = classifier.predict(test_data)
        if prediction[0] == 1:
            print("This user is most likely to buy the product.")
        else:
            print("This user is not likely to buy your product.")
purchase_model = PurchasePredictionModel()
purchase_model.predict_purchase_likelihood()