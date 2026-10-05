import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
class NaiveBayesClassifier:
    def __init__(self):
        self.X = None
        self.Y = None
        self.scaler = None
    def load_data(self):
        dataset = pd.read_csv('supermall.csv')
        self.X = dataset.iloc[:, [2, 3]].values
        self.Y = dataset.iloc[:, 4].values
    def scale_features(self):
        self.scaler = StandardScaler()
        self.X = self.scaler.fit_transform(self.X)
    def predict_purchase_probability(self):
        self.load_data()
        self.scale_features()
        classifier = GaussianNB()
        classifier.fit(self.X, self.Y)
        user_age = float(input("Enter the user's age: "))
        user_salary = float(input("What is the salary of the user? "))
        test_data = self.scaler.transform([[user_age, user_salary]])
        prediction = classifier.predict(test_data)
        if prediction[0] == 1:
            print("This user is most likely to buy the product.")
        else:
            print("This user is not likely to buy the product.")
naive_bayes_model = NaiveBayesClassifier()
naive_bayes_model.predict_purchase_probability()