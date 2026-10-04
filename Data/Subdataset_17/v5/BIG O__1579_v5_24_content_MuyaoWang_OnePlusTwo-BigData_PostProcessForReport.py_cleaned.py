import os
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import collections
def combine_json(path, root_name, new_file_name):
    files = os.listdir(path)
    content_list = []
    for file in files:
        with open(os.path.join(path, file)) as f:
            json_content = json.load(f)
        content_list.append(json_content)
    new_dict = {root_name: content_list}
    with open(new_file_name, 'w') as f:
        json.dump(new_dict, f)
def analyze_data(path1, path2):
    combine_json(path1, 'datasets', 'task1.json')
    combine_json(path2, 'predicted_types', 'task2.json')
    integer_count_list, real_count_list, datetime_count_list, text_count_list = [], [], [], []
    total_type_list = []
    files = os.listdir(path1)
    for file in files:
        with open(os.path.join(path1, file)) as f:
            json_content = json.load(f)
        integer_count, real_count, datetime_count, text_count = 0, 0, 0, 0
        for column in json_content['columns']:
            types = set()
            for data_type in column['data_types']:
                type_name = data_type['type']
                types.add(type_name)
                if type_name == 'INTEGER(LONG)':
                    integer_count += 1
                elif type_name == 'REAL':
                    real_count += 1
                elif type_name == 'DATE/TIME':
                    datetime_count += 1
                else:
                    text_count += 1
            total_type_list.append(types)
        integer_count_list.append(integer_count)
        real_count_list.append(real_count)
        datetime_count_list.append(datetime_count)
        text_count_list.append(text_count)
    print(f"Number of columns containing INTEGER(LONG) type: {sum(integer_count_list)}")
    print(f"Number of columns containing REAL type: {sum(real_count_list)}")
    print(f"Number of columns containing DATE/TIME type: {sum(datetime_count_list)}")
    print(f"Number of columns containing TEXT type: {sum(text_count_list)}")
    def plot_histogram(data, title, xlabel, ylabel, filename, bins=50):
        plt.clf()
        plt.hist(data, bins=bins, color='blue')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(axis='y', alpha=0.75)
        plt.savefig(filename)
    plot_histogram(integer_count_list, 'Histogram for INTEGER/LONG type', 'Number of columns with INTEGER(LONG) type', 'Count of datasets', 'integer.png')
    plot_histogram(integer_count_list, 'Histogram for INTEGER/LONG type (under 100)', 'Number of columns with INTEGER(LONG) type (under 100)', 'Count of datasets', 'integer_under100.png', bins=range(0, 101, 5))
    plot_histogram(real_count_list, 'Histogram for REAL type', 'Number of columns with REAL type', 'Count of datasets', 'real.png')
    plot_histogram(datetime_count_list, 'Histogram for DATE/TIME type', 'Number of columns with DATE/TIME type', 'Count of datasets', 'datetime.png')
    plot_histogram(text_count_list, 'Histogram for TEXT type', 'Number of columns with TEXT type', 'Count of datasets', 'text.png')
    plot_histogram(text_count_list, 'Histogram for TEXT type (under 100)', 'Number of columns with TEXT type (under 100)', 'Count of datasets', 'text_under100.png', bins=range(0, 101, 5))
    type_mapping = {
        frozenset({'INTEGER(LONG)'}): 'I',
        frozenset({'REAL'}): 'R',
        frozenset({'DATE/TIME'}): 'D',
        frozenset({'TEXT'}): 'T',
        frozenset({'INTEGER(LONG)', 'REAL'}): 'IR',
        frozenset({'INTEGER(LONG)', 'DATE/TIME'}): 'ID',
        frozenset({'INTEGER(LONG)', 'TEXT'}): 'IT',
        frozenset({'REAL', 'DATE/TIME'}): 'RD',
        frozenset({'REAL', 'TEXT'}): 'RT',
        frozenset({'DATE/TIME', 'TEXT'}): 'DT',
        frozenset({'INTEGER(LONG)', 'REAL', 'DATE/TIME'}): 'IRD',
        frozenset({'INTEGER(LONG)', 'REAL', 'TEXT'}): 'IRT',
        frozenset({'INTEGER(LONG)', 'DATE/TIME', 'TEXT'}): 'IDT',
        frozenset({'REAL', 'DATE/TIME', 'TEXT'}): 'RDT',
        frozenset({'INTEGER(LONG)', 'REAL', 'DATE/TIME', 'TEXT'}): 'IRDT'
    }
    type_set = [type_mapping.get(frozenset(types), 'Empty') for types in total_type_list]
    type_dict = dict(collections.Counter(type_set))
    sorted_dict = dict(sorted(type_dict.items(), key=lambda item: len(item[0])))
    plt.clf()
    plt.bar(sorted_dict.keys(), sorted_dict.values(), color='blue')
    plt.title('Frequent Itemsets')
    plt.xlabel('Frequent Itemsets')
    plt.ylabel('Count')
    plt.grid(axis='y', alpha=0.75)
    plt.savefig('frequent.png')
    semantic_type = ['Person_name', 'Business_name', 'City_agency', 'Neighborhood', 'Building_Classification', 'Areas_of_study',
                     'School_Levels', 'Borough', 'Subjects_in_school', 'Parks_Playgrounds', 'Zip_code', 'Address', 'Street_name',
                     'Phone_Number', 'City', 'LAT_LON_coordinates', 'School_name', 'Car_make', 'Vehicle_Type', 'Type_of_location',
                     'Websites', 'Color', 'College_University_names', 'Other']
    original_precision = [1.0, 1.0, 0.9166666666666666, 1.0, 1.0, 1.0, 1.0, 1.0, 0.125, 0.7142857142857143, 1.0, 1.0, 0.8095238095238095, 0.9090909090909091, 0.0, 1.0, 0.8461538461538461, 0.7, 0.0, 1.0, 1.0, 1.0, 0.0, 0.584]
    original_recall = [0.8387096774193549, 0.8888888888888888, 1.0, 0.7142857142857143, 1.0, 0.43478260869565216, 0.8666666666666667, 0.5909090909090909, 1.0, 0.5, 0.7857142857142857, 0.38095238095238093, 0.8095238095238095, 0.8333333333333334, 0.0, 0.9, 0.5789473684210527, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.6636363636363637]
    optimized_precision = [1.0, 1.0, 0.9166666666666666, 0.75, 1.0, 0.8846153846153846, 0.6363636363636364, 0.6666666666666666, 0.6666666666666666, 0.3333333333333333, 1.0, 0.5714285714285714, 0.6551724137931034, 0.9090909090909091, 0.5294117647058824, 1.0, 0.8, 0.7, 0.5, 1.0, 1.0, 1.0, 0.0, 0.4858490566037736]
    optimized_recall = [0.8387096774193549, 0.8888888888888888, 1.0, 1.0, 1.0, 1.0, 0.9333333333333333, 1.0, 1.0, 0.5, 0.7857142857142857, 0.7619047619047619, 0.9047619047619048, 0.8333333333333334, 1.0, 0.9, 0.8421052631578947, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.9363636363636364]
    def plot_precision_recall(metric, original, optimized, title, ylabel, filename):
        plt.clf()
        plt.figure(figsize=(10, 8))
        plt.plot(semantic_type, original, color='b', label='Original')
        plt.plot(semantic_type, optimized, color='r', label='Optimized')
        plt.title(title)
        plt.xlabel('Semantic Type')
        plt.ylabel(ylabel)
        plt.xticks(rotation=-90, fontsize=5)
        plt.legend()
        plt.savefig(filename)
    plot_precision_recall('Precision', original_precision, optimized_precision, 'Original precision vs. Optimized precision', 'Precision', 'precision.png')
    plot_precision_recall('Recall', original_recall, optimized_recall, 'Original recall vs. Optimized recall', 'Recall', 'recall.png')
    files = os.listdir(path2)
    semantic_type_count_list = []
    for file in files:
        with open(os.path.join(path2, file)) as f:
            json_content = json.load(f)
        semantic_type_list = json_content['semantic_types']
        semantic_type_count_list.append(len(semantic_type_list))
    semantic_dict = dict(collections.Counter(semantic_type_count_list))
    semantic_dict = collections.OrderedDict(sorted(semantic_dict.items()))
    plt.clf()
    plt.bar(semantic_dict.keys(), semantic_dict.values(), color='blue')
    plt.title('Prevalence of heterogeneous columns')
    plt.xlabel('Number of semantic types in the column')
    plt.ylabel('Count of columns')
    plt.grid(axis='y', alpha=0.75)
    plt.savefig('heterogeneous.png')
if __name__ == "__main__":
    path1 = 'Result-Task1'
    path2 = 'Result-Task2'
    analyze_data(path1, path2)