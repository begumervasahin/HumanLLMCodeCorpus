import pandas as pd
from sklearn.externals import joblib
def fonk1(file_path):
    return joblib.load(file_path)
def fonk2(file_path):
    b1 = pd.read_csv(file_path)
    b2 = b1.pop('label')
    return b1, b2
def fonk3(test_data, training_data_columns):
    return test_data[training_data_columns]
def fonk4(predictions_nn, predictions_rf, b8):
    b3 = ((predictions_nn == predictions_rf) & (predictions_nn == b8)).sum()
    b4 = ((predictions_nn != predictions_rf)).sum()
    b5 = ((predictions_nn == predictions_rf) & (predictions_nn != b8)).sum()
    return b3, b4, b5
def fonk5():
    b6 = fonk1('Random_Forest.pkl')
    b7 = fonk1('Neural_Network.pkl')
    test_data, b8 = fonk2("Test_Data_Table.csv")
    preprocessed_training_data, b9 = fonk2("Data_Table_Preprocessed.csv")
    b10 = fonk3(test_data, preprocessed_training_data.columns)
    b3 = 0
    b4 = 0
    b5 = 0
    for i in range(len(test_data)):
        b11 = b10.iloc[[i]]
        b12 = b8.iloc[i]
        b13 = b7.predict(b11)
        b14 = b6.predict(b11)
        correct, no_pred, b15 = fonk4(b13, b14, b12)
        b3 += correct
        b4 += no_pred
        b5 += b15
        print("Correct Predictions: ", b3)
        print("No Predictions: ", b4)
        print("Incorrect Predictions: ", b5)
if b16 = = "__main__":
    fonk5()