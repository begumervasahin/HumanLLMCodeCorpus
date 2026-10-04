import pandas as pd
import re
test_bins_dict = {}
def preprocess(structure_file, df, num_of_intervals):
    attribute_dict = set_attribute_dict(structure_file)
    df_no_missing_vals = handle_missing_values(df, attribute_dict)
    df_final = discretize_attributes(attribute_dict, df_no_missing_vals, num_of_intervals)
    return df_final
def preprocess_test(structure_file, df):
    attribute_dict = set_attribute_dict(structure_file)
    df_no_missing_vals = handle_missing_values(df, attribute_dict)
    df_final = discretize_test_attributes(test_bins_dict, df_no_missing_vals)
    return df_final
def set_attribute_dict(structure_file):
    attribute_dict = {}
    for line in structure_file:
        split_line = re.split(r'\s+', line.strip())
        attribute_type = "N" if split_line[2] == "NUMERIC" else "C"
        attribute_dict[split_line[1]] = attribute_type
    return attribute_dict
def handle_missing_values(df, attribute_dict):
    for key, attr_type in attribute_dict.items():
        if attr_type == "N":
            df[key].fillna(df.groupby("class")[key].transform("mean"), inplace=True)
        elif attr_type == "C":
            df[key].fillna(df[key].mode()[0], inplace=True)
    return df
def binning(col, k, key):
    global test_bins_dict
    min_val = col.min()
    max_val = col.max()
    cut_points = [min_val + (i + 1) * (max_val - min_val) / k for i in range(k - 1)]
    break_points = [min_val] + cut_points + [max_val]
    global labels
    labels = range(len(cut_points) + 1)
    test_bins_dict[key] = (break_points, labels)
    col_bin = pd.cut(col, bins=break_points, labels=labels, include_lowest=True)
    return col_bin
def binning_test(col, break_points, labels):
    return pd.cut(col, bins=break_points, labels=labels, include_lowest=True)
def discretize_attributes(attribute_dict, df, num_of_intervals):
    for key, attr_type in attribute_dict.items():
        if attr_type == "N":
            df[key] = binning(df[key], num_of_intervals, key)
    return df
def discretize_test_attributes(test_bins_dict, df):
    for key, (break_points, labels) in test_bins_dict.items():
        df[key] = binning_test(df[key], break_points, labels)
    return df