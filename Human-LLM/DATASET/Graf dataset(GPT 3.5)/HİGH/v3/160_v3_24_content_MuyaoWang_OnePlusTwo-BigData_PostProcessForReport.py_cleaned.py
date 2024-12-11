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
def fonk2(b2, title, xlabel, ylabel, filename, b4 = 50):
    plt.clf()
    plt.hist(b2, b4 = b4, b18='blue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(b5 = 'y', alpha=0.75)
    plt.savefig(filename)
b6 = 'Result-Task1'
b7 = 'datasets'
b8 = 'task1.json'
fonk1(b6, b7, b8)
b9 = 'Result-Task2'
b10 = 'presicted_types'
b11 = 'task2.json'
fonk1(b9, b10, b11)
def fonk3(b1):
    integer_count, real_count, datetime_count, b12 = 0, 0, 0, 0
    for file in b1:
        with open(os.path.join(b6, file)) as f:
            b3 = json.load(f)
        for column in b3['columns']:
            b13 = column['b13']
            integer_count += sum(1 for dt in b13 if dt['type'] == 'INTEGER(LONG)')
            real_count += sum(1 for dt in b13 if dt['type'] == 'REAL')
            datetime_count += sum(1 for dt in b13 if dt['type'] == 'DATE/TIME')
            b12 += sum(1 for dt in b13 if dt['type'] == 'TEXT')
    return integer_count, real_count, datetime_count, b12
b14 = os.listdir(b6)
integer_count, real_count, datetime_count, b12 = fonk3(b14)
print('Number of columns contain INTEGER(LONG) type:', integer_count)
print('Number of columns contain REAL type:', real_count)
print('Number of columns contain DATE/TIME type:', datetime_count)
print('Number of columns contain TEXT type:', b12)
fonk2(integer_count, 'Histogram for INTEGER/LONG type', 'Number of columns with INTEGER(LONG) type', 'Count of datasets', 'integer.png')
fonk2(integer_count, 'Histogram for INTEGER/LONG type (under 100)', 'Number of columns with INTEGER(LONG) type (under 100)', 'Count of datasets', 'integer_under100.png', b4 = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])
fonk2(real_count, 'Histogram for REAL type', 'Number of columns with REAL type', 'Count of datasets', 'real.png')
fonk2(datetime_count, 'Histogram for DATE/TIME type', 'Number of columns with DATE/TIME type', 'Count of datasets', 'datetime.png')
fonk2(b12, 'Histogram for TEXT type', 'Number of columns with TEXT type', 'Count of datasets', 'text.png')
fonk2(b12, 'Histogram for TEXT type (under 100)', 'Number of columns with TEXT type (under 100)', 'Count of datasets', 'text_under100.png', b4 = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])
b15 = os.listdir(b9)
b16 = [len(json.load(open(os.path.join(b9, file)))['semantic_types']) for file in b15]
b17 = collections.Counter(b16)
b17 = dict(sorted(b17.items()))
plt.bar(b17.keys(), b17.values(), b18 = 'blue')
plt.title('Prevalence of heterogeneous columns')
plt.xlabel('Number of semantic types in the column')
plt.ylabel('Count of columns')
plt.grid(b5 = 'y', alpha=0.75)
plt.savefig('heterogeneous.png')