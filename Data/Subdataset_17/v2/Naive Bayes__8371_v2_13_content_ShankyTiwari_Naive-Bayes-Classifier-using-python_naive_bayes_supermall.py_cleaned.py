
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
class Model:
    def __init__(self):
        self.X = None
        self.Y = None
        self.standardScaler = StandardScaler()
    def import_data(self, file_path):
        dataset = pd.read_csv(file_path)
        self.X = dataset.iloc[:, [2, 3]].values
        self.Y = dataset.iloc[:, 4].values
    def do_feature_scaling(self):
        self.X = self.standardScaler.fit_transform(self.X)
    def is_buying(self):
        self.import_data('supermall.csv')
        self.do_feature_scaling()
        classifier = GaussianNB()
        classifier.fit(self.X, self.Y)
        try:
            user_age = float(input("Enter the user's age: "))
            user_salary = float(input("What is the salary of the user: "))
        except ValueError:
            print("Invalid input. Please enter numerical values for age and salary.")
            return
        test_data = self.standardScaler.transform([[user_age, user_salary]])
        prediction = classifier.predict(test_data)
        if prediction[0] == 1:
            print('This user is most likely to buy the product.')
        else:
            print('This user is not going to buy your product.')
if __name__ == "__main__":
    model = Model()
    model.is_buying()