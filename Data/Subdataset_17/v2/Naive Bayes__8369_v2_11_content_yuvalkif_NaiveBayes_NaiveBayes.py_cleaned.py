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
        self.class_dict = self._fill_class_dict(dataset)
        dataset = dp.fillDatasetNANumerical(dataset)
        dataset = dp.fillDatasetNACategorical(dataset)
        dataset = dp.discretizeDataset(dataset, self.num_of_bins)
        self._fill_values_dict(dataset, list(self.class_dict.keys()))
        self.trained = True
    def _fill_class_dict(self, dataset):
        unique_class_values = dataset['class'].unique()
        self.classes = unique_class_values
        class_dict = {c: 0 for c in unique_class_values}
        for index, value in dataset.iterrows():
            class_dict[value['class']] += 1
        return class_dict
    def _fill_values_dict(self, dataset, class_values):
        p_params_list = []
        col_names = dataset.columns[:-1]
        self.attributes = col_names
        for col_name in col_names:
            unique_values = dataset[col_name].unique()
            p_params_list.append(1 / len(unique_values))
            values_dict = {}
            for class_value in class_values:
                for value in unique_values:
                    key = f"{value}_{class_value}"
                    values_dict[key] = sum((dataset[col_name] == value) & (dataset['class'] == class_value))
            self.cols_dict[col_name] = values_dict
        self.p_param = p_params_list
    def predict(self, test_file, out_path):
        test_df = self._clean_df(test_file)
        results = []
        for index, row in test_df.iterrows():
            class_scores = self._get_record_classes_scores(row)
            best_class = self._get_max_score_class(class_scores)
            results.append(f"{index + 1} {best_class}")
        self._write_output_to_file(out_path, results)
        return results
    def _clean_df(self, test_file):
        test_df = pd.read_csv(test_file)
        test_df = dp.fillDatasetNANumerical(test_df)
        test_df = dp.fillDatasetNACategorical(test_df)
        test_df = dp.discretizeDataset(test_df, self.num_of_bins)
        return test_df
    def _get_record_classes_scores(self, row):
        class_scores = []
        for c in self.classes:
            attribute_scores = []
            for attr_value, attr_name in zip(row, self.attributes):
                key = f"{attr_value}_{c}"
                attr_score = self.cols_dict[attr_name].get(key, 1 / self.total_rows)
                m_estimate_score = (attr_score + self.m_param * self.p_param[self.attributes.index(attr_name)]) / (self.class_dict[c] + self.m_param)
                attribute_scores.append(m_estimate_score)
            class_score = self.class_dict[c] / self.total_rows
            for score in attribute_scores:
                class_score *= score
            class_scores.append(class_score)
        return class_scores
    def _get_max_score_class(self, class_scores):
        max_score = max(class_scores)
        return self.classes[class_scores.index(max_score)]
    def _write_output_to_file(self, path, results):
        with open(path, 'w') as file:
            for result in results:
                file.write(f"{result}\n")
if __name__ == "__main__":
    train_file = 'train.csv'
    test_file = 'test.csv'
    output_file = 'output.txt'
    num_of_bins = 10
    train_data = pd.read_csv(train_file)
    nb = NaiveBayesAlgorithm(num_of_bins)
    nb.train(train_data)
    nb.predict(test_file, output_file)