import pandas as pd
import re
test_bins_dict = {}
def preProcess(structure_file, df, numOfIntervals):
    attributeDict = setAttributeDict(structure_file)
    df_noMissingVals = dealWithMissingValues(df, attributeDict)
    dfFinal = performDiscretization(attributeDict, df_noMissingVals, numOfIntervals)
    return dfFinal
def preProcess_test(structure_file, df):
    attributeDict = setAttributeDict(structure_file)
    df_noMissingVals = dealWithMissingValues(df, attributeDict)
    dfFinal = perform_Discretization_For_Test(test_bins_dict, df_noMissingVals)
    return dfFinal
def setAttributeDict(structure_file):
    attributeDict = {}
    valueType = ""
    for line in structure_file:
        splitedLine = re.split('\s+', line.strip())
        if splitedLine[2] == "NUMERIC":
            valueType = "N"
        else:
            valueType = "C"
        attributeDict[splitedLine[1]] = valueType
    return attributeDict
def set_attribute_values_dict(structure_file):
    attribute_values_dict = {}
    for line in structure_file:
        splitedLine = re.split('\s+', line.strip())
        if splitedLine[2] == "NUMERIC":
            att_values = labels
        else:
            sN = splitedLine[2].replace('{', '')
            sNN = sN.replace('}', '')
            att_values = sNN.split(',')
        attribute_values_dict[splitedLine[1]] = att_values
    return attribute_values_dict
def dealWithMissingValues(df, attributeDict):
    for key in attributeDict:
        if attributeDict[key] == "N":
            df[key].fillna(df.groupby("class")[key].transform("mean"), inplace=True)
    for key in attributeDict:
        if attributeDict[key] == "C":
            df[key] = df[key].fillna(df[key].mode()[0])
    return df
def binning(col, k, key):
    global test_bins_dict
    minval = col.min()
    maxval = col.max()
    cut_points = []
    w = (maxval - minval) / k
    for i in range(0, k - 1):
        cut_point = minval + (i + 1) * w
        if cut_point != minval and cut_point != maxval:
            cut_points.append(cut_point)
    break_points = [minval] + cut_points + [maxval]
    global labels
    labels = range(len(cut_points) + 1)
    test_bins_dict_value = [break_points, labels]
    test_bins_dict[key] = test_bins_dict_value
    colBin = pd.cut(col, bins=break_points, labels=labels, include_lowest=True)
    return colBin
def binning_Test(col, break_points, labels):
    colBin = pd.cut(col, bins=break_points, labels=labels, include_lowest=True)
    return colBin
def performDiscretization(attributeDict, df, numOfIntervals):
    for key in attributeDict:
        if attributeDict[key] == "N":
            df[key] = binning(df[key], numOfIntervals, key)
    return df
def perform_Discretization_For_Test(test_bins_dict, df):
    for key in test_bins_dict:
        df[key] = binning_Test(df[key], test_bins_dict[key][0], test_bins_dict[key][1])
    return df
if __name__ == "__main__":
    structure_file_content =
    structure_file = structure_file_content.strip().split('\n')
    data = {
        'age': [25, 30, 35, None, 40],
        'income': [50000, 60000, None, 80000, 100000],
        'student': ['yes', 'no', 'yes', None, 'no'],
        'credit_rating': ['fair', 'excellent', 'fair', 'excellent', None],
        'class': ['yes', 'no', 'yes', 'no', 'yes']
    }
    df = pd.DataFrame(data)
    numOfIntervals = 3
    df_train_processed = preProcess(structure_file, df, numOfIntervals)
    print("Training data after preprocessing:")
    print(df_train_processed)
    test_data = {
        'age': [28, 34, None, 45, 50],
        'income': [54000, 72000, 81000, 92000, None],
        'student': ['yes', 'no', 'yes', 'no', None],
        'credit_rating': ['excellent', 'fair', 'fair', 'excellent', 'fair'],
        'class': ['no', 'yes', 'no', 'yes', 'no']
    }
    df_test = pd.DataFrame(test_data)
    df_test_processed = preProcess_test(structure_file, df_test)
    print("Test data after preprocessing:")
    print(df_test_processed)