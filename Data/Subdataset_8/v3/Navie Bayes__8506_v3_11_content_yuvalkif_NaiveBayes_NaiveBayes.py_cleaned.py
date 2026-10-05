import pandas as pd
class DataPreProcessing:
    @staticmethod
    def fill_missing_numerical(dataset):
        return dataset.fillna(dataset.mean())
    @staticmethod
    def fill_missing_categorical(dataset):
        return dataset.fillna(dataset.mode().iloc[0])
    @staticmethod
    def discretize(dataset, num_of_bins):
        for col in dataset.select_dtypes(include=['number']):
            dataset[col] = pd.cut(dataset[col], bins=num_of_bins, labels=False)
        return dataset
class NaiveBayesAlgorithm:
    def __init__(self, num_of_bins):
        self.num_of_bins = num_of_bins
        self.m_param = 2
        self.class_dict = {}
        self.cols_dict = {}
        self.total_rows = 0
        self.classes = []
        self.attributes = []
        self.p_param = 0
        self.trained = False
    def train(self, dataset):
        self.total_rows = dataset.shape[0]
        self.class_dict = self.calculate_class_counts(dataset)
        dataset = DataPreProcessing.fill_missing_numerical(dataset)
        dataset = DataPreProcessing.fill_missing_categorical(dataset)
        dataset = DataPreProcessing.discretize(dataset, self.num_of_bins)
        self.calculate_attribute_probabilities(dataset)
        self.trained = True
    def calculate_class_counts(self, dataset):
        class_counts = dataset['class'].value_counts().to_dict()
        self.classes = list(class_counts.keys())
        return class_counts
    def calculate_attribute_probabilities(self, dataset):
        p_params_list = []
        col_names = dataset.columns[:-1]
        self.attributes = col_names
        for col_name in col_names:
            unique_values = dataset[col_name].unique()
            p_params_list.append(1 / len(unique_values))
            values_dict = {}
            for class_value in self.classes:
                for v in unique_values:
                    v = str(v)
                    count = dataset[(dataset['class'] == class_value) & (dataset[col_name] == v)].shape[0]
                    values_dict[f'{v}_{class_value}'] = count
            self.cols_dict[col_name] = values_dict
        self.p_param = p_params_list
    def predict(self, test_file, out_path):
        ans = []
        test_file_df = self.clean_test_dataset(test_file)
        for index, row in test_file_df.iterrows():
            record_score_all_classes = self.get_record_class_scores(row)
            best_class_fit = self.get_best_class(record_score_all_classes)
            ans.append(f"{index+1} {best_class_fit}")
        self.write_output_to_file(out_path, ans)
        return ans
    def clean_test_dataset(self, test_file):
        test_file_df = pd.read_csv(test_file)
        test_file_df = DataPreProcessing.fill_missing_numerical(test_file_df)
        test_file_df = DataPreProcessing.fill_missing_categorical(test_file_df)
        test_file_df = DataPreProcessing.discretize(test_file_df, self.num_of_bins)
        return test_file_df
    def get_record_class_scores(self, row):
        record_class_scores = []
        for c in self.classes:
            att_scores = []
            for att_value, att_name in zip(row, self.attributes):
                try:
                    numerator = self.cols_dict[att_name][f'{att_value}_{c}'] + self.m_param * self.p_param[k]
                    denominator = self.class_dict[c] + self.m_param
                    m_estimate_score = numerator / denominator
                    att_scores.append(m_estimate_score)
                except KeyError:
                    att_scores.append(1 / self.total_rows)
            record_class_score = self.class_dict[c] / self.total_rows
            for att_score in att_scores:
                record_class_score *= att_score
            record_class_scores.append(record_class_score)
        return record_class_scores
    def get_best_class(self, classes_scores):
        max_score = max(classes_scores)
        max_score_index = classes_scores.index(max_score)
        return self.classes[max_score_index]
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