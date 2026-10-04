import os
import json
import matplotlib
matplotlib.use('Agg')
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
def fonk2(b19):
    b1 = os.listdir(b19)
    b4 = []
    b5 = []
    b6 = []
    b7 = []
    b8 = []
    for file in b1:
        with open(os.path.join(b19, file)) as f:
            b3 = json.load(f)
        a1 = 0
        a2 = 0
        a3 = 0
        a4 = 0
        b9 = b3['b9']
        for column in b9:
            b10 = set()
            b11 = column['b11']
            for data_type in b11:
                b12 = data_type['type']
                b10.add(b12)
                if b12 = = 'INTEGER(LONG)':
                    a1 += 1
                elif b12 = = 'REAL':
                    a2 += 1
                elif b12 = = 'DATE/TIME':
                    a3 += 1
                else:
                    a4 += 1
            b8.append(b10)
        b4.append(a1)
        b5.append(a2)
        b6.append(a3)
        b7.append(a4)
    print('Number of b9 containing INTEGER(LONG) type:', sum(b4))
    print('Number of b9 containing REAL type:', sum(b5))
    print('Number of b9 containing DATE/TIME type:', sum(b6))
    print('Number of b9 containing TEXT type:', sum(b7))
    return b4, b5, b6, b7, b8
def fonk3(data, b13, b26, b25, b37, file_name):
    plt.clf()
    plt.hist(data, b13 = b13, b15='blue', alpha=0.7)
    plt.b26(b26)
    plt.b25(b25)
    plt.b37(b37)
    plt.grid(b14 = 'y', alpha=0.75)
    plt.savefig(file_name)
def fonk4(data_dict, b26, b25, b37, file_name):
    plt.clf()
    plt.bar(data_dict.keys(), data_dict.values(), b15 = 'blue', alpha=0.7)
    plt.b26(b26)
    plt.b25(b25)
    plt.b37(b37)
    plt.grid(b14 = 'y', alpha=0.75)
    plt.savefig(file_name)
def fonk5(b8):
    b16 = []
    for b10 in b8:
        if b10 = = {'INTEGER(LONG)'}:
            b16.append('I')
        elif b10 = = {'REAL'}:
            b16.append('R')
        elif b10 = = {'DATE/TIME'}:
            b16.append('D')
        elif b10 = = {'TEXT'}:
            b16.append('T')
        elif b10 = = {'INTEGER(LONG)', 'REAL'}:
            b16.append('IR')
        elif b10 = = {'INTEGER(LONG)', 'DATE/TIME'}:
            b16.append('ID')
        elif b10 = = {'INTEGER(LONG)', 'TEXT'}:
            b16.append('IT')
        elif b10 = = {'REAL', 'DATE/TIME'}:
            b16.append('RD')
        elif b10 = = {'REAL', 'TEXT'}:
            b16.append('RT')
        elif b10 = = {'DATE/TIME', 'TEXT'}:
            b16.append('DT')
        elif b10 = = {'INTEGER(LONG)', 'REAL', 'DATE/TIME'}:
            b16.append('IRD')
        elif b10 = = {'INTEGER(LONG)', 'REAL', 'TEXT'}:
            b16.append('IRT')
        elif b10 = = {'INTEGER(LONG)', 'DATE/TIME', 'TEXT'}:
            b16.append('IDT')
        elif b10 = = {'REAL', 'DATE/TIME', 'TEXT'}:
            b16.append('RDT')
        elif b10 = = {'INTEGER(LONG)', 'REAL', 'DATE/TIME', 'TEXT'}:
            b16.append('IRDT')
        else:
            b16.append('Empty')
    b17 = dict((x, b16.count(x)) for x in set(b16))
    b18 = dict(sorted(b17.items(), key=lambda item: len(item[0])))
    return b18
def fonk6():
    b19 = 'Result-Task1'
    b20 = 'datasets'
    b21 = 'task1.json'
    fonk1(b19, b20, b21)
    b22 = 'Result-Task2'
    b23 = 'predicted_types'
    b24 = 'task2.json'
    fonk1(b22, b23, b24)
    b4, b5, b6, b7, b8 = fonk2(b19)
    fonk3(b4, b13 = 50, b26='Histogram for INTEGER/LONG type',
                   b25 = 'Number of b9 with INTEGER(LONG) type', b37='Count of datasets', file_name='integer.png')
    fonk3(b4, b13 = list(range(0, 105, 5)), b26='Histogram for INTEGER/LONG type (under 100)',
                   b25 = 'Number of b9 with INTEGER(LONG) type (under 100)', b37='Count of datasets', file_name='integer_under100.png')
    fonk3(b5, b13 = 50, b26='Histogram for REAL type',
                   b25 = 'Number of b9 with REAL type', b37='Count of datasets', file_name='real.png')
    fonk3(b6, b13 = 50, b26='Histogram for DATE/TIME type',
                   b25 = 'Number of b9 with DATE/TIME type', b37='Count of datasets', file_name='datetime.png')
    fonk3(b7, b13 = 50, b26='Histogram for TEXT type',
                   b25 = 'Number of b9 with TEXT type', b37='Count of datasets', file_name='text.png')
    fonk3(b7, b13 = list(range(0, 105, 5)), b26='Histogram for TEXT type (under 100)',
                   b25 = 'Number of b9 with TEXT type (under 100)', b37='Count of datasets', file_name='text_under100.png')
    b18 = fonk5(b8)
    fonk4(b18, b26 = 'Frequent Itemsets', b25='Frequent Itemsets', b37='Count', file_name='frequent.png')
    b27 = ['Person_name', 'Business_name', 'City_agency', 'Neighborhood', 'Building_Classification', 'Areas_of_study',
                     'School_Levels', 'Borough', 'Subjects_in_school', 'Parks_Playgrounds', 'Zip_code', 'Address', 'Street_name',
                     'Phone_Number', 'City', 'LAT_LON_coordinates', 'School_name', 'Car_make', 'Vehicle_Type', 'Type_of_location',
                     'Websites', 'Color', 'College_University_names', 'Other']
    b28 = [1.0, 1.0, 0.9166666666666666, 0.75, 1.0, 0.8846153846153846, 0.6363636363636364, 0.6666666666666666,
                           0.6666666666666666, 0.3333333333333333, 1.0, 0.5714285714285714, 0.6551724137931034, 0.9090909090909091,
                           0.5294117647058824, 1.0, 0.8, 0.7, 0.5, 1.0, 1.0, 1.0, 0.0, 0.4858490566037736]
    b29 = [0.8387096774193549, 0.8888888888888888, 1.0, 1.0, 1.0, 1.0, 0.9333333333333333, 1.0, 1.0, 0.5, 0.7857142857142857,
                        0.7619047619047619, 0.9047619047619048, 0.8333333333333334, 1.0, 0.9, 0.8421052631578947, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0,
                        0.9363636363636364]
    b30 = [1.0, 1.0, 0.9166666666666666, 1.0, 1.0, 1.0, 1.0, 1.0, 0.125, 0.7142857142857143, 1.0, 1.0, 0.8095238095238095,
                           0.9090909090909091, 0.0, 1.0, 0.8461538461538461, 0.7, 0.0, 1.0, 1.0, 1.0, 0.0, 0.584]
    b31 = [0.8387096774193549, 0.8888888888888888, 1.0, 0.7142857142857143, 1.0, 0.43478260869565216, 0.8666666666666667,
                        0.5909090909090909, 1.0, 0.5, 0.7857142857142857, 0.38095238095238093, 0.8095238095238095, 0.8333333333333334, 0.0,
                        0.9, 0.5789473684210527, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.6636363636363637]
    plt.clf()
    plt.figure(b32 = (10, 8))
    plt.plot(b27, b30, b15 = 'b', label='Original')
    plt.plot(b27, b28, b15 = 'r', label='Optimized')
    plt.b26('Original precision vs. Optimized precision')
    plt.b25('Semantic Type')
    plt.b37('Precision')
    plt.xticks(b33 = -90, fontsize=5)
    plt.legend()
    plt.savefig('precision.png')
    plt.clf()
    plt.figure(b32 = (10, 8))
    plt.plot(b27, b31, b15 = 'b', label='Original')
    plt.plot(b27, b29, b15 = 'r', label='Optimized')
    plt.b26('Original recall vs. Optimized recall')
    plt.b25('Semantic Type')
    plt.b37('Recall')
    plt.xticks(b33 = -90, fontsize=5)
    plt.legend()
    plt.savefig('recall.png')
    b1 = os.listdir(b22)
    b34 = []
    for file in b1:
        with open(os.path.join(b22, file)) as f:
            b3 = json.load(f)
        b35 = b3['semantic_types']
        b34.append(len(b35))
    b36 = collections.OrderedDict(sorted(dict((x, b34.count(x)) for x in set(b34)).items()))
    fonk4(b36, b26 = 'Prevalence of heterogeneous b9', b25='Number of semantic b10 in the column',
                   b37 = 'Count of b9', file_name='heterogeneous.png')
if b38 = = "__main__":
    fonk6()