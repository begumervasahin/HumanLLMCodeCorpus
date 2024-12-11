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
b1 = os.listdir(b7)
b13 = []
b14 = []
b15 = []
b16 = []
b17 = []
for file in b1:
    with open(os.path.join(b7, file)) as f:
        b3 = json.load(f)
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    b18 = b3['columns']
    for column in b18:
        b19 = column['data_types']
        if len(b19) == 0:
            print(b3['dataset_name'])
            print(column['column_name'])
            print('-------------')
        for dataType in b19:
            b20 = dataType['type']
            if b20 = = 'INTEGER(LONG)':
                a1 += 1
            elif b20 = = 'REAL':
                a2 += 1
            elif b20 = = 'DATE/TIME':
                a3 += 1
            else:
                a4 += 1
    b13.append(a1)
    b14.append(a2)
    b15.append(a3)
    b16.append(a4)
print('Number of columns contain INTEGER(LONG) type:', sum(b13))
print('Number of columns contain REAL type:', sum(b14))
print('Number of columns contain DATE/TIME type:', sum(b15))
print('Number of columns contain TEXT type:', sum(b16))
fonk2(b13, 'Histogram for INTEGER/LONG type', 'Number of columns with INTEGER(LONG) type', 'Count of datasets', 'integer.png')
fonk2(b13, 'Histogram for INTEGER/LONG type (under 100)', 'Number of columns with INTEGER(LONG) type (under 100)', 'Count of datasets', 'integer_under100.png', b4 = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])
fonk2(b14, 'Histogram for REAL type', 'Number of columns with REAL type', 'Count of datasets', 'real.png')
fonk2(b15, 'Histogram for DATE/TIME type', 'Number of columns with DATE/TIME type', 'Count of datasets', 'datetime.png')
fonk2(b16, 'Histogram for TEXT type', 'Number of columns with TEXT type', 'Count of datasets', 'text.png')
fonk2(b16, 'Histogram for TEXT type (under 100)', 'Number of columns with TEXT type (under 100)', 'Count of datasets', 'text_under100.png', b4 = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])
b21 = []
for b22 in b17:
    if b22 = = {'INTEGER(LONG)'}:
        b21.append('I')
    elif b22 = = {'REAL'}:
        b21.append('R')
    elif b22 = = {'DATE/TIME'}:
        b21.append('D')
    elif b22 = = {'TEXT'}:
        b21.append('T')
    elif b22 = = {'INTEGER(LONG)', 'REAL'}:
        b21.append('IR')
    elif b22 = = {'INTEGER(LONG)', 'DATE/TIME'}:
        b21.append('ID')
    elif b22 = = {'INTEGER(LONG)', 'TEXT'}:
        b21.append('IT')
    elif b22 = = {'REAL', 'DATE/TIME'}:
        b21.append('RD')
    elif b22 = = {'REAL', 'TEXT'}:
        b21.append('RT')
    elif b22 = = {'DATE/TIME', 'TEXT'}:
        b21.append('DT')
    elif b22 = = {'INTEGER(LONG)', 'REAL', 'DATE/TIME'}:
        b21.append('IRD')
    elif b22 = = {'INTEGER(LONG)', 'REAL', 'TEXT'}:
        b21.append('IRT')
    elif b22 = = {'INTEGER(LONG)', 'DATE/TIME', 'TEXT'}:
        b21.append('IDT')
    elif b22 = = {'REAL', 'DATE/TIME', 'TEXT'}:
        b21.append('RDT')
    elif b22 = = {'INTEGER(LONG)', 'REAL', 'DATE/TIME', 'TEXT'}:
        b21.append('IRDT')
    else:
        b21.append('Empty')
b23 = dict((x,b21.count(x)) for x in set(b21))
b24 = sorted(b23, key=len, reverse=False)
b25 = {}
for b22 in b24:
    b25[b22] = b23[b22]
fonk3(b25, 'Frequent Itemsets', 'Frequent Itemsets', 'Count', 'frequent.png')
b26 = [1.0, 1.0, 0.9166666666666666, 0.75, 1.0, 0.8846153846153846, 0.6363636363636364, 0.6666666666666666, 0.6666666666666666, 0.3333333333333333, 1.0, 0.5714285714285714, 0.6551724137931034, 0.9090909090909091, 0.5294117647058824, 1.0, 0.8, 0.7, 0.5, 1.0, 1.0, 1.0, 0.0, 0.4858490566037736]
b27 = [0.8387096774193549, 0.8888888888888888, 1.0, 1.0, 1.0, 1.0, 0.9333333333333333, 1.0, 1.0, 0.5, 0.7857142857142857, 0.7619047619047619, 0.9047619047619048, 0.8333333333333334, 1.0, 0.9, 0.8421052631578947, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.9363636363636364]
b28 = [1.0, 1.0, 0.9166666666666666, 1.0, 1.0, 1.0, 1.0, 1.0, 0.125, 0.7142857142857143, 1.0, 1.0, 0.8095238095238095, 0.9090909090909091, 0.0, 1.0, 0.8461538461538461, 0.7, 0.0, 1.0, 1.0, 1.0, 0.0, 0.584]
b29 = [0.8387096774193549, 0.8888888888888888, 1.0, 0.7142857142857143, 1.0, 0.43478260869565216, 0.8666666666666667, 0.5909090909090909, 1.0, 0.5, 0.7857142857142857, 0.38095238095238093, 0.8095238095238095, 0.8333333333333334, 0.0, 0.9, 0.5789473684210527, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.6636363636363637]
b30 = ['Person_name', 'Business_name', 'City_agency', 'Neighborhood', 'Building_Classification', 'Areas_of_study',
                 'School_Levels', 'Borough', 'Subjects_in_school', 'Parks_Playgrounds', 'Zip_code', 'Address', 'Street_name',
                 'Phone_Number', 'City', 'LAT_LON_coordinates', 'School_name', 'Car_make', 'Vehicle_Type', 'Type_of_location',
                 'Websites', 'Color', 'College_University_names', 'Other']
b31 = sum(b28)/len(b28)
b32 = sum(b29)/len(b29)
b33 = sum(b26)/len(b26)
b34 = sum(b27)/len(b27)
b35 = b33 - b31
b36 = b34 - b32
plt.clf()
plt.figure(b37 = (10,8))
plt.plot(b30, b28, b6 = 'blue', label = 'Original')
plt.plot(b30, b26, b6 = 'red', label = 'Optimized')
plt.title('Original precision vs. Optimized precision')
plt.xlabel('Semantic Type')
plt.ylabel('Precision')
plt.xticks(b38 = -90, fontsize=5)
plt.legend()
plt.savefig('precision.png')
plt.clf()
plt.figure(b37 = (10,8))
plt.plot(b30, b29, b6 = 'blue', label='Original')
plt.plot(b30, b27, b6 = 'red', label='Optimized')
plt.title('Original recall vs. Optimized recall')
plt.xlabel('Semantic Type')
plt.ylabel('Recall')
plt.xticks(b38 = -90, fontsize=5)
plt.legend()
plt.savefig('recall.png')
b1 = os.listdir(b10)
b39 = []
for file in b1:
    with open(os.path.join(b10, file)) as f:
        b3 = json.load(f)
    b40 = b3['semantic_types']
    b39.append(len(b40))
b41 = dict((x,b39.count(x)) for x in b39)
b41 = collections.OrderedDict(sorted(b41.items()))
plt.clf()
plt.bar(b41.keys(), b41.values(), b6 = 'blue')
plt.title('Prevalence of heterogeneous columns')
plt.xlabel('Number of semantic types in the column')
plt.ylabel('Count of columns')
plt.grid(b5 = 'y', alpha=0.75)
plt.savefig('heterogeneous.png')