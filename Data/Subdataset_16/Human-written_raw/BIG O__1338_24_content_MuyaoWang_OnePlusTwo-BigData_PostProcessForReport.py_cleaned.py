import os
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import collections
def fonk1(path,root_name,new_file_name):
    b1 = os.listdir(path)
    b2 = {}
    b3 = []
    for file in b1:
        with open(path + '/' + file) as b6:
            b4 = json.load(b6)
        b3.append(b4)
    b2[root_name] = b3
    b5 = json.dumps(b2)
    b6 = open(new_file_name, 'w')
    b6.write(b5)
    b6.close()
b7 = 'Result-Task1'
b8 = 'datasets'
b9 = 'task1.json'
fonk1(b7,b8,b9)
b10 = 'Result-Task2'
b11 = 'presicted_types'
b12 = 'task2.json'
fonk1(b10,b11,b12)
b1 = os.listdir(b7)
b13 = []
b14 = []
b15 = []
b16 = []
b17 = []
for file in b1:
    with open(b7 + '/' + file) as b6:
        b4 = json.load(b6)
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    b18 = b4['columns']
    for column in b18:
        b19 = set()
        b20 = column['data_types']
        if len(b20) == 0:
            print(b4['dataset_name'])
            print(column['column_name'])
            print('-------------')
        for dataType in b20:
            b21 = dataType['type']
            b19.add(b21)
            if b21 = = 'INTEGER(LONG)':
                a1 += 1
            elif b21 = = 'REAL':
                a2 += 1
            elif b21 = = 'DATE/TIME':
                a3 += 1
            else:
                a4 += 1
        b17.append(b19)
    b13.append(a1)
    b14.append(a2)
    b15.append(a3)
    b16.append(a4)
print('Number of columns contain INTEGER(LONG) type:', sum(b13))
print('Number of columns contain REAL type:', sum(b14))
print('Number of columns contain DATE/TIME type:', sum(b15))
print('Number of columns contain TEXT type:', sum(b16))
plt.clf()
plt.hist(b13, b22 = 50, b29='
plt.title('Histogram for INTEGER/LONG type')
plt.xlabel('Number of columns with INTEGER(LONG) type')
plt.ylabel('Count of datasets')
plt.grid(b23 = 'y', alpha=0.75)
plt.savefig('integer.png')
plt.clf()
plt.hist(b13, b22 = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100], b29='
plt.title('Histogram for INTEGER/LONG type (
plt.xlabel('Number of columns with INTEGER(LONG) type (under 100)')
plt.ylabel('Count of datasets')
plt.grid(b23 = 'y', alpha=0.75)
plt.savefig('integer_under100.png')
plt.clf()
plt.hist(b14, b22 = 50, b29='
plt.title('Histogram for REAL type')
plt.xlabel('Number of columns with REAL type')
plt.ylabel('Count of datasets')
plt.grid(b23 = 'y', alpha=0.75)
plt.savefig('real.png')
plt.clf()
plt.hist(b15, b22 = 50, b29='
plt.title('Histogram for DATE/TIME type')
plt.xlabel('Number of columns with DATE/TIME type')
plt.ylabel('Count of datasets')
plt.grid(b23 = 'y', alpha=0.75)
plt.savefig('datetime.png')
plt.clf()
plt.hist(b16, b22 = 50, b29='
plt.title('Histogram for TEXT type')
plt.xlabel('Number of columns with TEXT type')
plt.ylabel('Count of datasets')
plt.grid(b23 = 'y', alpha=0.75)
plt.savefig('text.png')
plt.clf()
plt.hist(b16, b22 = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100], b29='
plt.title('Histogram for TEXT type (
plt.xlabel('Number of columns with TEXT type (under 100)')
plt.ylabel('Count of datasets')
plt.grid(b23 = 'y', alpha=0.75)
plt.savefig('text_under100.png')
b24 = []
for b25 in b17:
    if b25 = = {'INTEGER(LONG)'}:
        b24.append('I')
    elif b25 = = {'REAL'}:
        b24.append('R')
    elif b25 = = {'DATE/TIME'}:
        b24.append('D')
    elif b25 = = {'TEXT'}:
        b24.append('T')
    elif b25 = = {'INTEGER(LONG)', 'REAL'}:
        b24.append('IR')
    elif b25 = = {'INTEGER(LONG)', 'DATE/TIME'}:
        b24.append('ID')
    elif b25 = = {'INTEGER(LONG)', 'TEXT'}:
        b24.append('IT')
    elif b25 = = {'REAL', 'DATE/TIME'}:
        b24.append('RD')
    elif b25 = = {'REAL', 'TEXT'}:
        b24.append('RT')
    elif b25 = = {'DATE/TIME', 'TEXT'}:
        b24.append('DT')
    elif b25 = = {'INTEGER(LONG)', 'REAL', 'DATE/TIME'}:
        b24.append('IRD')
    elif b25 = = {'INTEGER(LONG)', 'REAL', 'TEXT'}:
        b24.append('IRT')
    elif b25 = = {'INTEGER(LONG)', 'DATE/TIME', 'TEXT'}:
        b24.append('IDT')
    elif b25 = = {'REAL', 'DATE/TIME', 'TEXT'}:
        b24.append('RDT')
    elif b25 = = {'INTEGER(LONG)', 'REAL', 'DATE/TIME', 'TEXT'}:
        b24.append('IRDT')
    else:
        b24.append('Empty')
b26 = dict((x,b24.count(x)) for x in set(b24))
b27 = sorted(b26, key=len, reverse=False)
b28 = {}
for b25 in b27:
    b28[b25] = b26[b25]
plt.clf()
plt.bar(b28.keys(), b28.values(), b29 = '
plt.title('Frequent Itemsets')
plt.xlabel('Frequent Itemsets')
plt.ylabel('Count')
plt.grid(b23 = 'y', alpha=0.75)
plt.savefig('frequent.png')
b30 = [1.0, 1.0, 0.9166666666666666, 0.75, 1.0, 0.8846153846153846, 0.6363636363636364, 0.6666666666666666, 0.6666666666666666, 0.3333333333333333, 1.0, 0.5714285714285714, 0.6551724137931034, 0.9090909090909091, 0.5294117647058824, 1.0, 0.8, 0.7, 0.5, 1.0, 1.0, 1.0, 0.0, 0.4858490566037736]
b31 = [0.8387096774193549, 0.8888888888888888, 1.0, 1.0, 1.0, 1.0, 0.9333333333333333, 1.0, 1.0, 0.5, 0.7857142857142857, 0.7619047619047619, 0.9047619047619048, 0.8333333333333334, 1.0, 0.9, 0.8421052631578947, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.9363636363636364]
b32 = [1.0, 1.0, 0.9166666666666666, 1.0, 1.0, 1.0, 1.0, 1.0, 0.125, 0.7142857142857143, 1.0, 1.0, 0.8095238095238095, 0.9090909090909091, 0.0, 1.0, 0.8461538461538461, 0.7, 0.0, 1.0, 1.0, 1.0, 0.0, 0.584]
b33 = [0.8387096774193549, 0.8888888888888888, 1.0, 0.7142857142857143, 1.0, 0.43478260869565216, 0.8666666666666667, 0.5909090909090909, 1.0, 0.5, 0.7857142857142857, 0.38095238095238093, 0.8095238095238095, 0.8333333333333334, 0.0, 0.9, 0.5789473684210527, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.6636363636363637]
b34 = ['Person_name', 'Business_name', 'City_agency', 'Neighborhood', 'Building_Classification', 'Areas_of_study',
                 'School_Levels', 'Borough', 'Subjects_in_school', 'Parks_Playgrounds', 'Zip_code', 'Address', 'Street_name',
                 'Phone_Number', 'City', 'LAT_LON_coordinates', 'School_name', 'Car_make', 'Vehicle_Type', 'Type_of_location',
                 'Websites', 'Color', 'College_University_names', 'Other']
b35 = sum(b32)/len(b32)
b36 = sum(b33)/len(b33)
b37 = sum(b30)/len(b30)
b38 = sum(b31)/len(b31)
b39 = b37 - b35
b40 = b38 - b36
plt.clf()
plt.figure(b41 = (10,8))
plt.plot(b34, b32, b29 = 'b', label = 'Original')
plt.plot(b34, b30, b29 = 'r', label = 'Optimized')
plt.title('Original precision vs. Optimized precision')
plt.xlabel('Semantic Type')
plt.ylabel('Precision')
plt.xticks(b42 = -90, fontsize=5)
plt.legend()
plt.savefig('precision.png')
plt.clf()
plt.figure(b41 = (10,8))
plt.plot(b34, b33, b29 = 'b', label='Original')
plt.plot(b34, b31, b29 = 'r', label='Optimized')
plt.title('Original recall vs. Optimized recall')
plt.xlabel('Semantic Type')
plt.ylabel('Recall')
plt.xticks(b42 = -90, fontsize=5)
plt.legend()
plt.savefig('recall.png')
b1 = os.listdir(b10)
b43 = []
for file in b1:
    with open(b10 + '/' + file) as b6:
        b4 = json.load(b6)
    b44 = b4['semantic_types']
    b43.append(len(b44))
b45 = dict((x,b43.count(x)) for x in b43)
b45 = collections.OrderedDict(sorted(b45.items()))
plt.clf()
plt.bar(b45.keys(), b45.values(), b29 = '
plt.title('Prevalence of heterogeneous columns')
plt.xlabel('Number of semantic b19 in the column')
plt.ylabel('Count of columns')
plt.grid(b23 = 'y', alpha=0.75)
plt.savefig('heterogeneous.png')