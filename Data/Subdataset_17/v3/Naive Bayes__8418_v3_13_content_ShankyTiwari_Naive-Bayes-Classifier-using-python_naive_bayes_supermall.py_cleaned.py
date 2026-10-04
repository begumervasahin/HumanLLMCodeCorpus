
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
class Model:
    def __init__(self):
        self.X = None
        self.Y = None
        self.standardScaler = StandardScaler()
        self.classifier = GaussianNB()
    def import_data(self, file_path):
        dataset = pd.read_csv(file_path)
        self.X = dataset.iloc[:, [2, 3]].values
        self.Y = dataset.iloc[:, 4].values
    def do_feature_scaling(self):
        self.X = self.standardScaler.fit_transform(self.X)
    def get_user_input(self):
        try:
            user_age = float(input("Enter the user's age: "))
            user_salary = float(input("What is the salary of the user: "))
            return user_age, user_salary
        except ValueError:
            print("Invalid input. Please enter numerical values for age and salary.")
            return None, None
    def predict_purchase(self, user_age, user_salary):
        test_data = self.standardScaler.transform([[user_age, user_salary]])
        prediction = self.classifier.predict(test_data)
        return prediction[0] == 1
    def is_buying(self):
        self.import_data('supermall.csv')
        self.do_feature_scaling()
        self.classifier.fit(self.X, self.Y)
        user_age, user_salary = self.get_user_input()
        if user_age is not None and user_salary is not None:
            if self.predict_purchase(user_age, user_salary):
                print('This user is most likely to buy the product.')
            else:
                print('This user is not going to buy your product.')
if __name__ == "__main__":
    model = Model()
    model.is_buying()