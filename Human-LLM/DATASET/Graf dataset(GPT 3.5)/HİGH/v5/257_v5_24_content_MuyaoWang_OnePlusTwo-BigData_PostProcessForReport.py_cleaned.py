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
b4 = 'Result-Task1'
b5 = 'datasets'
b6 = 'task1.json'
fonk1(b4, b5, b6)
b7 = 'Result-Task2'
b8 = 'presicted_types'
b9 = 'task2.json'
fonk1(b7, b8, b9)
def fonk2(b1):
    integer_count, real_count, datetime_count, b10 = 0, 0, 0, 0
    for file in b1:
        with open(os.path.join(b4, file)) as f:
            b3 = json.load(f)
        for column in b3['columns']:
            b11 = column['b11']
            for data_type in b11:
                b12 = data_type['type']
                if b12 = = 'INTEGER(LONG)':
                    integer_count += 1
                elif b12 = = 'REAL':
                    real_count += 1
                elif b12 = = 'DATE/TIME':
                    datetime_count += 1
                elif b12 = = 'TEXT':
                    b10 += 1
    return integer_count, real_count, datetime_count, b10
b13 = os.listdir(b4)
integer_count, real_count, datetime_count, b10 = fonk2(b13)
print('Number of columns contain INTEGER(LONG) type:', integer_count)
print('Number of columns contain REAL type:', real_count)
print('Number of columns contain DATE/TIME type:', datetime_count)
print('Number of columns contain TEXT type:', b10)
plt.clf()
plt.hist(integer_count, b14 = 50, b19='blue')
plt.title('Histogram for INTEGER/LONG type')
plt.xlabel('Number of columns with INTEGER(LONG) type')
plt.ylabel('Count of datasets')
plt.grid(b15 = 'y', alpha=0.75)
plt.savefig('integer.png')
plt.clf()
plt.hist(integer_count, b14 = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100], b19='blue')
plt.title('Histogram for INTEGER/LONG type (under 100)')
plt.xlabel('Number of columns with INTEGER(LONG) type (under 100)')
plt.ylabel('Count of datasets')
plt.grid(b15 = 'y', alpha=0.75)
plt.savefig('integer_under100.png')
b16 = os.listdir(b7)
b17 = [len(json.load(open(os.path.join(b7, file)))['semantic_types']) for file in b16]
b18 = collections.Counter(b17)
b18 = dict(sorted(b18.items()))
plt.clf()
plt.bar(b18.keys(), b18.values(), b19 = 'blue')
plt.title('Prevalence of heterogeneous columns')
plt.xlabel('Number of semantic types in the column')
plt.ylabel('Count of columns')
plt.grid(b15 = 'y', alpha=0.75)
plt.savefig('heterogeneous.png')
