import pandas as pd
import re
test_bins_dict = {}
def preProcess(structure_file, df, num_intervals):
    attribute_dict = set_attribute_dict(structure_file)
    df_no_missing_vals = deal_with_missing_values(df, attribute_dict)
    df_final = perform_discretization(attribute_dict, df_no_missing_vals, num_intervals)
    return df_final
def preProcess_test(structure_file, df):
    attribute_dict = set_attribute_dict(structure_file)
    df_no_missing_vals = deal_with_missing_values(df, attribute_dict)
    df_final = perform_discretization_for_test(test_bins_dict, df_no_missing_vals)
    return df_final
def set_attribute_dict(structure_file):
    attribute_dict = {}
    for line in structure_file:
        split_line = re.split(r'\s+', line.strip())
        value_type = "N" if split_line[2] == "NUMERIC" else "C"
        attribute_dict[split_line[1]] = value_type
    return attribute_dict
def set_attribute_values_dict(structure_file):
    attribute_values_dict = {}
    for line in structure_file:
        split_line = re.split(r'\s+', line.strip())
        if split_line[2] == "NUMERIC":
            att_values = labels
        else:
            att_values = split_line[2].replace('{', '').replace('}', '').split(',')
        attribute_values_dict[split_line[1]] = att_values
    return attribute_values_dict
def deal_with_missing_values(df, attribute_dict):
    for key, value_type in attribute_dict.items():
        if value_type == "N":
            df[key].fillna(df.groupby("class")[key].transform("mean"), inplace=True)
        elif value_type == "C":
            df[key].fillna(df[key].mode()[0], inplace=True)
    return df
def binning(col, num_intervals, key):
    global test_bins_dict
    min_val, max_val = col.min(), col.max()
    cut_points = [min_val + (i + 1) * (max_val - min_val) / num_intervals for i in range(num_intervals - 1)]
    break_points = [min_val] + cut_points + [max_val]
    labels = range(len(cut_points) + 1)
    test_bins_dict[key] = [break_points, labels]
    return pd.cut(col, bins=break_points, labels=labels, include_lowest=True)
def binning_test(col, break_points, labels):
    return pd.cut(col, bins=break_points, labels=labels, include_lowest=True)
def perform_discretization(attribute_dict, df, num_intervals):
    for key, value_type in attribute_dict.items():
        if value_type == "N":
            df[key] = binning(df[key], num_intervals, key)
    return df
def perform_discretization_for_test(test_bins_dict, df):
    for key, (break_points, labels) in test_bins_dict.items():
        df[key] = binning_test(df[key], break_points, labels)
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
    num_intervals = 3
    df_train_processed = preProcess(structure_file, df, num_intervals)
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