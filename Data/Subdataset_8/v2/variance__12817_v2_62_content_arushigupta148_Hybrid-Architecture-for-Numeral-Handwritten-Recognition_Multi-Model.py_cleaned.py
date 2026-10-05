import pandas as pd
from sklearn.externals import joblib
random_forest_model = joblib.load('Random_Forest.pkl')
neural_network_model = joblib.load('Neural_Network.pkl')
test_data = pd.read_csv("Test_Data_Table.csv")
actual_labels = test_data.label
test_data = test_data.drop(test_data.columns[0], axis=1)
test_data = test_data.drop(labels=['label'], axis=1)
preprocessed_training_data = pd.read_csv("Data_Table_Preprocessed.csv")
preprocessed_training_data = preprocessed_training_data.drop(preprocessed_training_data.columns[0], axis=1)
final_test_data = pd.DataFrame()
for column in preprocessed_training_data.columns:
    final_test_data[column] = test_data[column]
correct_predictions = 0
no_predictions = 0
incorrect_predictions = 0
for i in range(10000):
    single_sample_test_data = pd.DataFrame(columns=final_test_data.columns)
    single_sample_test_data.loc[0] = final_test_data.loc[i]
    actual_label = actual_labels.loc[i]
    prediction_nn = neural_network_model.predict(single_sample_test_data)
    prediction_rf = random_forest_model.predict(single_sample_test_data)
    if prediction_nn == prediction_rf == actual_label:
        correct_predictions += 1
    elif prediction_nn != prediction_rf:
        no_predictions += 1
    elif prediction_nn == prediction_rf != actual_label:
        incorrect_predictions += 1
    print("Correct Predictions: ", correct_predictions)
    print("No Predictions: ", no_predictions)
    print("Incorrect Predictions: ", incorrect_predictions)