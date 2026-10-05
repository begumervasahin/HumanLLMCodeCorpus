import pandas as pd
from sklearn.externals import joblib
random_forest_model = joblib.load('Random_Forest.pkl')
neural_network_model = joblib.load('Neural_Network.pkl')
test_data = pd.read_csv("Test_Data_Table.csv")
test_labels = test_data.label
test_data = test_data.drop(test_data.columns[0], axis=1)
test_data = test_data.drop(labels=['label'], axis=1)
train_data = pd.read_csv("Data_Table_Preprocessed.csv")
train_data = train_data.drop(train_data.columns[0], axis=1)
final_test_data = pd.DataFrame()
for column in train_data.columns:
    final_test_data[column] = test_data[column]
correct_predictions = 0
no_predictions = 0
incorrect_predictions = 0
for i in range(len(test_data)):
    X = pd.DataFrame(columns=final_test_data.columns)
    X.loc[0] = final_test_data.loc[i]
    y = test_labels.loc[i]
    nn_prediction = neural_network_model.predict(X)
    rf_prediction = random_forest_model.predict(X)
    if nn_prediction == rf_prediction and nn_prediction == y:
        correct_predictions += 1
    elif nn_prediction != rf_prediction:
        no_predictions += 1
    elif nn_prediction == rf_prediction and nn_prediction != y:
        incorrect_predictions += 1
    print("Correct predictions:", correct_predictions)
    print("No predictions:", no_predictions)
    print("Incorrect predictions:", incorrect_predictions)