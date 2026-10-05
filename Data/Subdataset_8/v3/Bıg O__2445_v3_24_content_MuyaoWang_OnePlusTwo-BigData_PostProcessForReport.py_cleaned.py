import os
import json
import matplotlib.pyplot as plt
import collections
def combine_json(path, root_name, new_file_name):
    files = os.listdir(path)
    data = {root_name: []}
    for file in files:
        with open(os.path.join(path, file)) as f:
            json_content = json.load(f)
        data[root_name].append(json_content)
    with open(new_file_name, 'w') as f:
        json.dump(data, f)
def plot_histogram(data, title, xlabel, ylabel, filename, bins=50):
    plt.clf()
    plt.hist(data, bins=bins, color='blue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(axis='y', alpha=0.75)
    plt.savefig(filename)
path_task1 = 'Result-Task1'
root_name_task1 = 'datasets'
new_file_name_task1 = 'task1.json'
combine_json(path_task1, root_name_task1, new_file_name_task1)
path_task2 = 'Result-Task2'
root_name_task2 = 'presicted_types'
new_file_name_task2 = 'task2.json'
combine_json(path_task2, root_name_task2, new_file_name_task2)
def analyze_task1(files):
    integer_count, real_count, datetime_count, text_count = 0, 0, 0, 0
    for file in files:
        with open(os.path.join(path_task1, file)) as f:
            json_content = json.load(f)
        for column in json_content['columns']:
            data_types = column['data_types']
            integer_count += sum(1 for dt in data_types if dt['type'] == 'INTEGER(LONG)')
            real_count += sum(1 for dt in data_types if dt['type'] == 'REAL')
            datetime_count += sum(1 for dt in data_types if dt['type'] == 'DATE/TIME')
            text_count += sum(1 for dt in data_types if dt['type'] == 'TEXT')
    return integer_count, real_count, datetime_count, text_count
files_task1 = os.listdir(path_task1)
integer_count, real_count, datetime_count, text_count = analyze_task1(files_task1)
print('Number of columns contain INTEGER(LONG) type:', integer_count)
print('Number of columns contain REAL type:', real_count)
print('Number of columns contain DATE/TIME type:', datetime_count)
print('Number of columns contain TEXT type:', text_count)
plot_histogram(integer_count, 'Histogram for INTEGER/LONG type', 'Number of columns with INTEGER(LONG) type', 'Count of datasets', 'integer.png')
plot_histogram(integer_count, 'Histogram for INTEGER/LONG type (under 100)', 'Number of columns with INTEGER(LONG) type (under 100)', 'Count of datasets', 'integer_under100.png', bins=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])
plot_histogram(real_count, 'Histogram for REAL type', 'Number of columns with REAL type', 'Count of datasets', 'real.png')
plot_histogram(datetime_count, 'Histogram for DATE/TIME type', 'Number of columns with DATE/TIME type', 'Count of datasets', 'datetime.png')
plot_histogram(text_count, 'Histogram for TEXT type', 'Number of columns with TEXT type', 'Count of datasets', 'text.png')
plot_histogram(text_count, 'Histogram for TEXT type (under 100)', 'Number of columns with TEXT type (under 100)', 'Count of datasets', 'text_under100.png', bins=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])
files_task2 = os.listdir(path_task2)
semantic_type_count_list = [len(json.load(open(os.path.join(path_task2, file)))['semantic_types']) for file in files_task2]
semantic_type_dict = collections.Counter(semantic_type_count_list)
semantic_type_dict = dict(sorted(semantic_type_dict.items()))
plt.bar(semantic_type_dict.keys(), semantic_type_dict.values(), color='blue')
plt.title('Prevalence of heterogeneous columns')
plt.xlabel('Number of semantic types in the column')
plt.ylabel('Count of columns')
plt.grid(axis='y', alpha=0.75)
plt.savefig('heterogeneous.png')