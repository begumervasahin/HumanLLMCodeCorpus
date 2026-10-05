import os
import json
import matplotlib.pyplot as plt
import collections
def combine_json(path, root_name, new_file_name):
    files = os.listdir(path)
    new_dict = {root_name: []}
    for file in files:
        with open(os.path.join(path, file)) as f:
            json_content = json.load(f)
        new_dict[root_name].append(json_content)
    with open(new_file_name, 'w') as f:
        json.dump(new_dict, f)
def plot_histogram(data, title, xlabel, ylabel, filename, bins=50):
    plt.clf()
    plt.hist(data, bins=bins, color='blue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(axis='y', alpha=0.75)
    plt.savefig(filename)
def plot_bar_chart(data_dict, title, xlabel, ylabel, filename):
    plt.clf()
    plt.bar(data_dict.keys(), data_dict.values(), color='blue')
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
files_task1 = os.listdir(path_task1)
integer_count_list = []
real_count_list = []
datetime_count_list = []
text_count_list = []
for file in files_task1:
    with open(os.path.join(path_task1, file)) as f:
        json_content = json.load(f)
    for column in json_content['columns']:
        data_types = column['data_types']
        integer_count = sum(1 for dt in data_types if dt['type'] == 'INTEGER(LONG)')
        real_count = sum(1 for dt in data_types if dt['type'] == 'REAL')
        datetime_count = sum(1 for dt in data_types if dt['type'] == 'DATE/TIME')
        text_count = sum(1 for dt in data_types if dt['type'] == 'TEXT')
        integer_count_list.append(integer_count)
        real_count_list.append(real_count)
        datetime_count_list.append(datetime_count)
        text_count_list.append(text_count)
print('Number of columns contain INTEGER(LONG) type:', sum(integer_count_list))
print('Number of columns contain REAL type:', sum(real_count_list))
print('Number of columns contain DATE/TIME type:', sum(datetime_count_list))
print('Number of columns contain TEXT type:', sum(text_count_list))
plot_histogram(integer_count_list, 'Histogram for INTEGER/LONG type', 'Number of columns with INTEGER(LONG) type', 'Count of datasets', 'integer.png')
plot_histogram(integer_count_list, 'Histogram for INTEGER/LONG type (under 100)', 'Number of columns with INTEGER(LONG) type (under 100)', 'Count of datasets', 'integer_under100.png', bins=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])
plot_histogram(real_count_list, 'Histogram for REAL type', 'Number of columns with REAL type', 'Count of datasets', 'real.png')
plot_histogram(datetime_count_list, 'Histogram for DATE/TIME type', 'Number of columns with DATE/TIME type', 'Count of datasets', 'datetime.png')
plot_histogram(text_count_list, 'Histogram for TEXT type', 'Number of columns with TEXT type', 'Count of datasets', 'text.png')
plot_histogram(text_count_list, 'Histogram for TEXT type (under 100)', 'Number of columns with TEXT type (under 100)', 'Count of datasets', 'text_under100.png', bins=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])
files_task2 = os.listdir(path_task2)
semantic_type_count_list = []
for file in files_task2:
    with open(os.path.join(path_task2, file)) as f:
        json_content = json.load(f)
    semantic_type_count_list.append(len(json_content['semantic_types']))
semantic_type_dict = collections.Counter(semantic_type_count_list)
semantic_type_dict = dict(sorted(semantic_type_dict.items()))
plt.bar(semantic_type_dict.keys(), semantic_type_dict.values(), color='blue')
plt.title('Prevalence of heterogeneous columns')
plt.xlabel('Number of semantic types in the column')
plt.ylabel('Count of columns')
plt.grid(axis='y', alpha=0.75)
plt.savefig('heterogeneous.png')