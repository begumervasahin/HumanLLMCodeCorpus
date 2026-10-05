import os
import json
import matplotlib.pyplot as plt
import collections
def fonk1(path, root_name, new_file_name):
    b1 = os.listdir(path)
    b2 = {root_name: []}
    for file in b1:
        with open(os.path.join(path, file)) as f:
            b3 = json.load(f)
        b2[root_name].append(b3)
    with open(new_file_name, 'w') as f:
        json.dump(b2, f)
def fonk2(data, title, xlabel, ylabel, filename, b4 = 50):
    plt.clf()
    plt.hist(data, b4 = b4, b6='blue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(b5 = 'y', alpha=0.75)
    plt.savefig(filename)
def fonk3(data_dict, title, xlabel, ylabel, filename):
    plt.clf()
    plt.bar(data_dict.keys(), data_dict.values(), b6 = 'blue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(b5 = 'y', alpha=0.75)
    plt.savefig(filename)
b7 = 'Result-Task1'
b8 = 'datasets'
b9 = 'task1.json'
fonk1(b7, b8, b9)
b10 = 'Result-Task2'
b11 = 'presicted_types'
b12 = 'task2.json'
fonk1(b10, b11, b12)
b13 = os.listdir(b7)
b14 = []
b15 = []
b16 = []
b17 = []
for file in b13:
    with open(os.path.join(b7, file)) as f:
        b3 = json.load(f)
    for column in b3['columns']:
        b18 = column['b18']
        b19 = sum(1 for dt in b18 if dt['type'] == 'INTEGER(LONG)')
        b20 = sum(1 for dt in b18 if dt['type'] == 'REAL')
        b21 = sum(1 for dt in b18 if dt['type'] == 'DATE/TIME')
        b22 = sum(1 for dt in b18 if dt['type'] == 'TEXT')
        b14.append(b19)
        b15.append(b20)
        b16.append(b21)
        b17.append(b22)
print('Number of columns contain INTEGER(LONG) type:', sum(b14))
print('Number of columns contain REAL type:', sum(b15))
print('Number of columns contain DATE/TIME type:', sum(b16))
print('Number of columns contain TEXT type:', sum(b17))
fonk2(b14, 'Histogram for INTEGER/LONG type', 'Number of columns with INTEGER(LONG) type', 'Count of datasets', 'integer.png')
fonk2(b14, 'Histogram for INTEGER/LONG type (under 100)', 'Number of columns with INTEGER(LONG) type (under 100)', 'Count of datasets', 'integer_under100.png', b4 = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])
fonk2(b15, 'Histogram for REAL type', 'Number of columns with REAL type', 'Count of datasets', 'real.png')
fonk2(b16, 'Histogram for DATE/TIME type', 'Number of columns with DATE/TIME type', 'Count of datasets', 'datetime.png')
fonk2(b17, 'Histogram for TEXT type', 'Number of columns with TEXT type', 'Count of datasets', 'text.png')
fonk2(b17, 'Histogram for TEXT type (under 100)', 'Number of columns with TEXT type (under 100)', 'Count of datasets', 'text_under100.png', b4 = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])
b23 = os.listdir(b10)
b24 = []
for file in b23:
    with open(os.path.join(b10, file)) as f:
        b3 = json.load(f)
    b24.append(len(b3['semantic_types']))
b25 = collections.Counter(b24)
b25 = dict(sorted(b25.items()))
plt.bar(b25.keys(), b25.values(), b6 = 'blue')
plt.title('Prevalence of heterogeneous columns')
plt.xlabel('Number of semantic types in the column')
plt.ylabel('Count of columns')
plt.grid(b5 = 'y', alpha=0.75)
plt.savefig('heterogeneous.png')