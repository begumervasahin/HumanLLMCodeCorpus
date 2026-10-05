import csv
import pandas as pd
import numpy as np
import DataPreProcessing as dp
class NaiveBayesAlgorithm:
    def __init__(self, num_of_bins):
        self.m_param = 2
        self.class_dict = {}
        self.cols_dict = {}
        self.total_rows = 0
        self.classes = []
        self.attributes = []
        self.p_param = 0
        self.num_of_bins = num_of_bins
        self.trained = False
    def train(self, dataset):
        self.total_rows = dataset.shape[0]
        self.class_dict = self.fill_class_dict(dataset)
        dataset = self.preprocess_dataset(dataset)
        self.fill_values_dict(dataset)
        self.trained = True
    def fill_class_dict(self, dataset):
        unique_classes = dataset['class'].unique()
        self.classes = unique_classes
        class_dict = {c: 0 for c in unique_classes}
        for _, row in dataset.iterrows():
            class_dict[row['class']] += 1
        return class_dict
    def preprocess_dataset(self, dataset):
        dataset = dp.fill_dataset_na_numerical(dataset)
        dataset = dp.fill_dataset_na_categorical(dataset)
        dataset = dp.discretize_dataset(dataset, self.num_of_bins)
        return dataset
    def fill_values_dict(self, dataset):
        p_params = []
        col_names = list(dataset)[:-1]
        self.attributes = col_names
        for col_name in col_names:
            unique_values = dataset[col_name].unique()
            p_params.append(1 / len(unique_values))
            values_dict = {str(c) + '_' + str(class_value): 0
                           for class_value in self.classes
                           for c in unique_values}
            for _, row in dataset.iterrows():
                for c in unique_values:
                    c = str(c)
                    if (row[col_name] == c) and (row['class'] in self.classes):
                        values_dict[c + '_' + str(row['class'])] += 1
            self.cols_dict[col_name] = values_dict
        self.p_param = p_params
    def predict(self, test_file, out_path):
        predictions = []
        test_df = self.preprocess_test_data(test_file)
        for index, row in test_df.iterrows():
            record_scores = self.calculate_class_scores(row)
            best_class = self.get_best_class(record_scores)
            predictions.append(f"{index + 1} {best_class}")
        self.write_output_to_file(out_path, predictions)
        return predictions
    def preprocess_test_data(self, test_file):
        test_df = pd.read_csv(test_file)
        test_df = self.preprocess_dataset(test_df)
        return test_df
    def calculate_class_scores(self, row):
        class_scores = []
        for c in self.classes:
            att_scores = []
            k = 0
            for att_value, att_name in zip(row, self.attributes):
                try:
                    m_estimate_score = (self.cols_dict[att_name][str(att_value) + '_' + str(c)] +
                                        float(self.m_param) * float(self.p_param[k])) / \
                                       (self.class_dict[c] + self.m_param)
                    k += 1
                    att_scores.append(m_estimate_score)
                except KeyError:
                    att_scores.append(1 / self.total_rows)
            record_class_score = self.class_dict[c] / self.total_rows
            for att_score in att_scores:
                record_class_score *= att_score
            class_scores.append(record_class_score)
        return class_scores
    def get_best_class(self, class_scores):
        max_score = -1
        chosen_idx = -1
        for i, score in enumerate(class_scores):
            if max_score < score:
                max_score = score
                chosen_idx = i
        return self.classes[chosen_idx]
    def write_output_to_file(self, path, predictions):
        with open(path, 'w') as f:
            f.writelines("%s\n" % row for row in predictions)