import pandas as pd
from sklearn.externals import joblib
def load_model(file_path):
    return joblib.load(file_path)
def load_data(file_path):
    data = pd.read_csv(file_path)
    labels = data.pop('label')
    return data, labels
def prepare_final_test_data(test_data, training_data_columns):
    return test_data[training_data_columns]
def evaluate_predictions(predictions_nn, predictions_rf, actual_labels):
    correct_predictions = ((predictions_nn == predictions_rf) & (predictions_nn == actual_labels)).sum()
    no_predictions = ((predictions_nn != predictions_rf)).sum()
    incorrect_predictions = ((predictions_nn == predictions_rf) & (predictions_nn != actual_labels)).sum()
    return correct_predictions, no_predictions, incorrect_predictions
def main():
    random_forest_model = load_model('Random_Forest.pkl')
    neural_network_model = load_model('Neural_Network.pkl')
    test_data, actual_labels = load_data("Test_Data_Table.csv")
    preprocessed_training_data, _ = load_data("Data_Table_Preprocessed.csv")
    final_test_data = prepare_final_test_data(test_data, preprocessed_training_data.columns)
    correct_predictions = 0
    no_predictions = 0
    incorrect_predictions = 0
    for i in range(len(test_data)):
        single_sample_test_data = final_test_data.iloc[[i]]
        actual_label = actual_labels.iloc[i]
        prediction_nn = neural_network_model.predict(single_sample_test_data)
        prediction_rf = random_forest_model.predict(single_sample_test_data)
        correct, no_pred, incorrect = evaluate_predictions(prediction_nn, prediction_rf, actual_label)
        correct_predictions += correct
        no_predictions += no_pred
        incorrect_predictions += incorrect
        print("Correct Predictions: ", correct_predictions)
        print("No Predictions: ", no_predictions)
        print("Incorrect Predictions: ", incorrect_predictions)
if __name__ == "__main__":
    main()