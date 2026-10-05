import pandas as pd
from sklearn.externals import joblib
random_forest_model = joblib.load('Random_Forest.pkl')
neural_network_model = joblib.load('Neural_Network.pkl')
test_data = pd.read_csv("Test_Data_Table.csv")
test_labels = test_data.pop('label')
train_data = pd.read_csv("Data_Table_Preprocessed.csv")
train_data.drop(train_data.columns[0], axis=1, inplace=True)
final_test_data = test_data[train_data.columns]
correct_predictions = 0
no_predictions = 0
incorrect_predictions = 0
for i, sample in final_test_data.iterrows():
    X = sample.values.reshape(1, -1)
    y = test_labels[i]
    nn_prediction = neural_network_model.predict(X)
    rf_prediction = random_forest_model.predict(X)
    if nn_prediction == rf_prediction == y:
        correct_predictions += 1
    elif nn_prediction != rf_prediction:
        no_predictions += 1
    elif nn_prediction == rf_prediction != y:
        incorrect_predictions += 1
    print("Correct predictions:", correct_predictions)
    print("No predictions:", no_predictions)
    print("Incorrect predictions:", incorrect_predictions)