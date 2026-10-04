import pandas as pd
import numpy as np
import DataPreProcessing as dp
class NaiveBayesAlgorithm:
    def __init__(self, num_of_bins):
        self.m_param = 2
        self.classdict = dict()
        self.colsDict = dict()
        self.totalRows = 0
        self.classes = []
        self.attributes = []
        self.p_param = 0
        self.num_of_bins = num_of_bins
        self.trained = False
    def train(self, dataset):
        self.totalRows = dataset.shape[0]
        self.classdict = self.fillClassDict(dataset)
        dataset = dp.fillDatasetNANumerical(dataset)
        dataset = dp.fillDatasetNACategorical(dataset)
        dataset = dp.discretizeDataset(dataset, self.num_of_bins)
        self.fillValuesDict(dataset=dataset, classvalues=list(self.classdict.keys()))
        self.trained = True
    def fillClassDict(self, dataset):
        uniqueClassValues = dataset['class'].unique()
        self.classes = uniqueClassValues
        classdict = dict()
        for c in uniqueClassValues:
            classdict[c] = 0
        for index, value in dataset.iterrows():
            classdict[value['class']] += 1
        return classdict
    def fillValuesDict(self, dataset, classvalues):
        p_params_list = []
        colnames = list(dataset)
        colnames = colnames[0:len(colnames)-1]
        self.attributes = colnames
        for colname in colnames:
            uniqueValues = list(dataset[colname].unique())
            p_params_list.append(float(1 / len(uniqueValues)))
            valuesdict = dict()
            for classvalue in classvalues:
                for c in uniqueValues:
                    c = str(c)
                    valuesdict[c + '_' + str(classvalue)] = 0
                    for index, value in dataset.iterrows():
                        if (value[colname] == c) and (value['class'] == classvalue):
                            valuesdict[c + '_' + classvalue] += 1
            self.colsDict[colname] = valuesdict
        self.p_param = p_params_list
        return uniqueValues
    def predict(self, test_file, out_path):
        ans = []
        test_file_df = self.clean_df(test_file)
        for index, row in test_file_df.iterrows():
            record_score_all_classes = self.get_record_classes_scores(row)
            best_class_fit = self.get_max_score_class(record_score_all_classes)
            ans.append(str(index + 1) + " " + best_class_fit)
        self.write_output_to_file(out_path, ans)
        return ans
    def clean_df(self, test_file):
        test_file_df = pd.read_csv(test_file)
        test_file_df = dp.fillDatasetNANumerical(test_file_df)
        test_file_df = dp.fillDatasetNACategorical(test_file_df)
        test_file_df = dp.discretizeDataset(test_file_df, self.num_of_bins)
        return test_file_df
    def get_record_classes_scores(self, row):
        record_classes_scores = []
        for c in self.classes:
            att_scores = []
            k = 0
            for att_value, att_name in zip(row, self.attributes):
                try:
                    m_estimate_score = float(
                        (self.colsDict[att_name][str(att_value) + '_' + str(c)] + float(self.m_param) * float(
                            self.p_param[k])) / (self.classdict[c] + self.m_param))
                    k += 1
                    att_scores.append(m_estimate_score)
                except KeyError:
                    att_scores.append(float(1 / self.totalRows))
            record_class_score = float(self.classdict[c]) / float(self.totalRows)
            for att_score in att_scores:
                record_class_score *= att_score
            record_classes_scores.append(record_class_score)
        return record_classes_scores
    def get_max_score_class(self, classes_scores):
        chosen_class = -1
        chosen_idx = -1
        for i in range(len(classes_scores)):
            if chosen_class < classes_scores[i]:
                chosen_class = classes_scores[i]
                chosen_idx = i
        return self.classes[chosen_idx]
    def write_output_to_file(self, path, ans):
        with open(path, 'w') as f:
            f.writelines("%s\n" % row for row in ans)
if __name__ == "__main__":
    train_file = 'train.csv'
    test_file = 'test.csv'
    output_file = 'output.txt'
    num_of_bins = 10
    train_data = pd.read_csv(train_file)
    nb = NaiveBayesAlgorithm(num_of_bins)
    nb.train(train_data)
    nb.predict(test_file, output_file)