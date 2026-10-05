import pandas as pd
import numpy as np
class DataPreProcessing:
    @staticmethod
    def fill_dataset_na_numerical(dataset):
        return dataset.fillna(dataset.mean())
    @staticmethod
    def fill_dataset_na_categorical(dataset):
        return dataset.fillna(dataset.mode().iloc[0])
    @staticmethod
    def discretize_dataset(dataset, num_of_bins):
        for col in dataset.select_dtypes(include=['number']):
            dataset[col] = pd.cut(dataset[col], bins=num_of_bins, labels=False)
        return dataset
class NaiveBayesAlgorithm:
    def __init__(self, num_of_bins):
        self.m_param = 2
        self.class_dict = dict()
        self.cols_dict = dict()
        self.total_rows = 0
        self.classes = []
        self.attributes = []
        self.p_param = 0
        self.num_of_bins = num_of_bins
        self.trained = False
    def train(self, dataset):
        self.total_rows = dataset.shape[0]
        self.class_dict = self.fill_class_dict(dataset)
        dataset = DataPreProcessing.fill_dataset_na_numerical(dataset)
        dataset = DataPreProcessing.fill_dataset_na_categorical(dataset)
        dataset = DataPreProcessing.discretize_dataset(dataset, self.num_of_bins)
        self.fill_values_dict(dataset=dataset, class_values=list(self.class_dict.keys()))
        self.trained = True
    def fill_class_dict(self, dataset):
        unique_class_values = dataset['class'].unique()
        self.classes = unique_class_values
        class_dict = {c: 0 for c in unique_class_values}
        for _, value in dataset.iterrows():
            class_dict[value['class']] += 1
        return class_dict
    def fill_values_dict(self, dataset, class_values):
        p_params_list = []
        col_names = list(dataset)
        col_names = col_names[:-1]
        self.attributes = col_names
        for col_name in col_names:
            unique_values = list(dataset[col_name].unique())
            p_params_list.append(1 / len(unique_values))
            values_dict = {f'{c}_{str(v)}': 0 for c in class_values for v in unique_values}
            for class_value in class_values:
                for v in unique_values:
                    v = str(v)
                    for _, value in dataset.iterrows():
                        if value[col_name] == v and value['class'] == class_value:
                            values_dict[f'{v}_{class_value}'] += 1
            self.cols_dict[col_name] = values_dict
        self.p_param = p_params_list
    def predict(self, test_file, out_path):
        ans = []
        test_file_df = pd.read_csv(test_file)
        test_file_df = self.clean_df(test_file_df)
        for index, row in test_file_df.iterrows():
            record_score_all_classes = self.get_record_classes_scores(row)
            best_class_fit = self.get_max_score_class(record_score_all_classes)
            ans.append(f"{index+1} {best_class_fit}")
        self.write_output_to_file(out_path, ans)
        return ans
    def clean_df(self, test_file):
        test_file_df = pd.read_csv(test_file)
        test_file_df = DataPreProcessing.fill_dataset_na_numerical(test_file_df)
        test_file_df = DataPreProcessing.fill_dataset_na_categorical(test_file_df)
        test_file_df = DataPreProcessing.discretize_dataset(test_file_df, self.num_of_bins)
        return test_file_df
    def get_record_classes_scores(self, row):
        record_classes_scores = []
        for c in self.classes:
            att_scores = []
            k = 0
            for att_value, att_name in zip(row, self.attributes):
                try:
                    m_estimate_score = (self.cols_dict[att_name][f'{att_value}_{c}'] + self.m_param * self.p_param[k]) / (self.class_dict[c] + self.m_param)
                    k += 1
                    att_scores.append(m_estimate_score)
                except KeyError:
                    att_scores.append(1 / self.total_rows)
            record_class_score = self.class_dict[c] / self.total_rows
            for att_score in att_scores:
                record_class_score *= att_score
            record_classes_scores.append(record_class_score)
        return record_classes_scores
    def get_max_score_class(self, classes_scores):
        chosen_class = max(classes_scores)
        chosen_idx = classes_scores.index(chosen_class)
        return self.classes[chosen_idx]
    @staticmethod
    def write_output_to_file(path, ans):
        with open(path, 'w') as f:
            f.write('\n'.join(ans))
if __name__ == "__main__":
    nb = NaiveBayesAlgorithm(num_of_bins=5)
    train_dataset = pd.read_csv("train_dataset.csv")
    nb.train(train_dataset)
    test_predictions = nb.predict("test_dataset.csv", "output.txt")
    print("Predictions written to output.txt")