import pandas as pd
import re
test_bins_dict = {}
def preProcess(structure_file,df,numOfIntervals):
    attributeDict = setAtrributeDict(structure_file)
    df_noMissingVals = dealWithMissingValues(df, attributeDict)
    dfFinal = performDiscretization(attributeDict, df_noMissingVals, numOfIntervals)
    return dfFinal
def preProcess_test(structure_file,df):
    attributeDict = setAtrributeDict(structure_file)
    df_noMissingVals = dealWithMissingValues(df, attributeDict)
    dfFinal = perform_Discretization_For_Test(test_bins_dict, df_noMissingVals)
    return dfFinal
def setAtrributeDict(structure_file):
    attributeDict = {}
    valueType = ""
    for line in structure_file:
        splitedLine = re.split('\s', line)
        if splitedLine[2] == "NUMERIC":
            valueType = "N"
        else:
            valueType = "C"
        attributeDict[splitedLine[1]] = valueType
    return attributeDict
def set_attribute_values_dict(structure_file):
    attribute_values_dict={}
    for line in structure_file:
        splitedLine = re.split('\s', line)
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
def binning(col, k,key):
    global test_bins_dict
    minval = col.min()
    maxval = col.max()
    cut_points = []
    w = (maxval - minval)/k
    for i in range(0, k-1):
        if (minval + (i+1)*w) != minval and (minval + (i+1)*w) != maxval:
            cut_points.append(minval + (i+1)*w)
    break_points = [minval] + cut_points + [maxval]
    global labels
    labels = range(len(cut_points) + 1)
    test_bins_dict_value = [break_points, labels]
    test_bins_dict[key] = test_bins_dict_value
    colBin = pd.cut(col, bins=break_points, labels=labels, include_lowest=True)
    return colBin
def binning_Test(col,break_points,labels):
    colBin = pd.cut(col, bins=break_points, labels=labels, include_lowest=True)
    return colBin
def performDiscretization(attributeDict,df,numOfIntervals):
    for key in attributeDict:
        if attributeDict[key] == "N":
            df[key] = binning(df[key], numOfIntervals,key)
    return df
def perform_Discretization_For_Test(test_bins_dict,df):
    for key in test_bins_dict:
        df[key] = binning_Test(df[key],test_bins_dict[key][0],test_bins_dict[key][1])
    return df