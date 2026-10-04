import csv
import pandas as pd
import numpy as np
import DataPreProcessing as dp
class NaiveBayesClassifier:
    def __init__(self, num_of_bins):
        self.m_param = 2
        self.class_dict = {}
        self.cols_dict = {}
        self.total_rows = 0
        self.classes = []
        self.attributes = []
        self.p_params = []
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
        class_dict = dataset['class'].value_counts().to_dict()
        self.classes = list(class_dict.keys())
        return class_dict
    def _fill_values_dict(self, dataset, class_values):
        colnames = dataset.columns[:-1]
        self.attributes = colnames
        p_params_list = []
        for colname in colnames:
            unique_values = dataset[colname].unique()
            p_params_list.append(1 / len(unique_values))
            values_dict = {f"{v}_{c}": 0 for c in class_values for v in unique_values}
            for _, row in dataset.iterrows():
                key = f"{row[colname]}_{row['class']}"
                values_dict[key] += 1
            self.cols_dict[colname] = values_dict
        self.p_params = p_params_list
    def predict(self, test_file, out_path):
        test_df = self._clean_df(test_file)
        predictions = []
        for index, row in test_df.iterrows():
            class_scores = self._get_record_class_scores(row)
            best_class = self._get_max_score_class(class_scores)
            predictions.append(f"{index + 1} {best_class}")
        self._write_output_to_file(out_path, predictions)
        return predictions
    def _clean_df(self, test_file):
        df = pd.read_csv(test_file)
        df = dp.fillDatasetNANumerical(df)
        df = dp.fillDatasetNACategorical(df)
        df = dp.discretizeDataset(df, self.num_of_bins)
        return df
    def _get_record_class_scores(self, row):
        class_scores = []
        for c in self.classes:
            attribute_scores = []
            for k, (att_value, att_name) in enumerate(zip(row, self.attributes)):
                key = f"{att_value}_{c}"
                m_estimate_score = (self.cols_dict[att_name].get(key, 0) + self.m_param * self.p_params[k]) / (self.class_dict[c] + self.m_param)
                attribute_scores.append(m_estimate_score)
            class_score = self.class_dict[c] / self.total_rows
            for score in attribute_scores:
                class_score *= score
            class_scores.append(class_score)
        return class_scores
    def _get_max_score_class(self, class_scores):
        return self.classes[np.argmax(class_scores)]
    def _write_output_to_file(self, path, predictions):
        with open(path, 'w') as file:
            for prediction in predictions:
                file.write(f"{prediction}\n")
def main():
    labels = ['Sport', 'Entertainment', 'Household', 'House Property', 'Education', 'Fashion', 'Current Politics', 'Game', 'Science and Technology', 'Finance']
    stop_path = './cnews/cnews.vocab.txt'
    train_path = './cnews/cnews.train.txt'
    test_path = './cnews/cnews.test.txt'
    classifier = NaiveBayesClassifier(num_of_bins=10)
    raw_features, raw_classes = dp.loadDataSet(train_path, stop_path)
    unique_set_list = classifier.create_unique_set(raw_features)
    train_matrix = [classifier.words_to_vec(unique_set_list, features) for features in raw_features]
    train_df = pd.DataFrame(train_matrix, columns=unique_set_list).assign(class=raw_classes)
    classifier.train(train_df)
    predictions = classifier.predict(test_path, 'output.txt')
    np.save('models/pos.npy', np.array(classifier.p_params))
    with open('models/unique_set_list.txt', 'w') as file:
        for word in unique_set_list:
            file.write(f"{word}\n")
    np.save('models/p_vectors.npy', np.array(classifier.cols_dict))
    print("Model training completed and parameters saved.")
if __name__ == "__main__":
    main()