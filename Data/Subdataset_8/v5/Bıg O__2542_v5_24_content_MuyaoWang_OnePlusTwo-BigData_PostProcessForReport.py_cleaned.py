import os
import json
import matplotlib.pyplot as plt
import collections
def combine_json(path, root_name, new_file_name):
    files = os.listdir(path)
    combined_data = {root_name: []}
    for file in files:
        with open(os.path.join(path, file)) as f:
            json_content = json.load(f)
        combined_data[root_name].append(json_content)
    with open(new_file_name, 'w') as f:
        json.dump(combined_data, f)
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
            for data_type in data_types:
                type_name = data_type['type']
                if type_name == 'INTEGER(LONG)':
                    integer_count += 1
                elif type_name == 'REAL':
                    real_count += 1
                elif type_name == 'DATE/TIME':
                    datetime_count += 1
                elif type_name == 'TEXT':
                    text_count += 1
    return integer_count, real_count, datetime_count, text_count
files_task1 = os.listdir(path_task1)
integer_count, real_count, datetime_count, text_count = analyze_task1(files_task1)
print('Number of columns contain INTEGER(LONG) type:', integer_count)
print('Number of columns contain REAL type:', real_count)
print('Number of columns contain DATE/TIME type:', datetime_count)
print('Number of columns contain TEXT type:', text_count)
plt.clf()
plt.hist(integer_count, bins=50, color='blue')
plt.title('Histogram for INTEGER/LONG type')
plt.xlabel('Number of columns with INTEGER(LONG) type')
plt.ylabel('Count of datasets')
plt.grid(axis='y', alpha=0.75)
plt.savefig('integer.png')
plt.clf()
plt.hist(integer_count, bins=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100], color='blue')
plt.title('Histogram for INTEGER/LONG type (under 100)')
plt.xlabel('Number of columns with INTEGER(LONG) type (under 100)')
plt.ylabel('Count of datasets')
plt.grid(axis='y', alpha=0.75)
plt.savefig('integer_under100.png')
files_task2 = os.listdir(path_task2)
semantic_type_count_list = [len(json.load(open(os.path.join(path_task2, file)))['semantic_types']) for file in files_task2]
semantic_type_dict = collections.Counter(semantic_type_count_list)
semantic_type_dict = dict(sorted(semantic_type_dict.items()))
plt.clf()
plt.bar(semantic_type_dict.keys(), semantic_type_dict.values(), color='blue')
plt.title('Prevalence of heterogeneous columns')
plt.xlabel('Number of semantic types in the column')
plt.ylabel('Count of columns')
plt.grid(axis='y', alpha=0.75)
plt.savefig('heterogeneous.png')
