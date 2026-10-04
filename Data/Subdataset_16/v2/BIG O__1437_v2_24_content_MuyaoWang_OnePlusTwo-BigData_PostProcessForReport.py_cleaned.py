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
def fonk2(path):
    b1 = os.listdir(path)
    b4 = []
    b5 = []
    b6 = []
    b7 = []
    b8 = []
    for file in b1:
        with open(os.path.join(path, file)) as f:
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
def fonk3(data, b13, b27, b26, b38, file_name):
    plt.clf()
    plt.hist(data, b13 = b13, b15='blue', alpha=0.7)
    plt.b27(b27)
    plt.b26(b26)
    plt.b38(b38)
    plt.grid(b14 = 'y', alpha=0.75)
    plt.savefig(file_name)
def fonk4(data_dict, b27, b26, b38, file_name):
    plt.clf()
    plt.bar(data_dict.keys(), data_dict.values(), b15 = 'blue', alpha=0.7)
    plt.b27(b27)
    plt.b26(b26)
    plt.b38(b38)
    plt.grid(b14 = 'y', alpha=0.75)
    plt.savefig(file_name)
def fonk5(b8):
    b16 = []
    for b10 in b8:
        b17 = ''.join(sorted([t[0] for t in b10]))
        b16.append(b17)
    b18 = dict((x, b16.count(x)) for x in set(b16))
    b19 = dict(sorted(b18.items(), key=lambda item: len(item[0])))
    return b19
def fonk6():
    b20 = 'Result-Task1'
    b21 = 'datasets'
    b22 = 'task1.json'
    fonk1(b20, b21, b22)
    b23 = 'Result-Task2'
    b24 = 'predicted_types'
    b25 = 'task2.json'
    fonk1(b23, b24, b25)
    b4, b5, b6, b7, b8 = fonk2(b20)
    fonk3(b4, b13 = 50, b27='Histogram for INTEGER/LONG type',
                   b26 = 'Number of b9 with INTEGER(LONG) type', b38='Count of datasets', file_name='integer.png')
    fonk3(b4, b13 = list(range(0, 105, 5)), b27='Histogram for INTEGER/LONG type (under 100)',
                   b26 = 'Number of b9 with INTEGER(LONG) type (under 100)', b38='Count of datasets', file_name='integer_under100.png')
    fonk3(b5, b13 = 50, b27='Histogram for REAL type',
                   b26 = 'Number of b9 with REAL type', b38='Count of datasets', file_name='real.png')
    fonk3(b6, b13 = 50, b27='Histogram for DATE/TIME type',
                   b26 = 'Number of b9 with DATE/TIME type', b38='Count of datasets', file_name='datetime.png')
    fonk3(b7, b13 = 50, b27='Histogram for TEXT type',
                   b26 = 'Number of b9 with TEXT type', b38='Count of datasets', file_name='text.png')
    fonk3(b7, b13 = list(range(0, 105, 5)), b27='Histogram for TEXT type (under 100)',
                   b26 = 'Number of b9 with TEXT type (under 100)', b38='Count of datasets', file_name='text_under100.png')
    b19 = fonk5(b8)
    fonk4(b19, b27 = 'Frequent Itemsets', b26='Frequent Itemsets', b38='Count', file_name='frequent.png')
    b28 = ['Person_name', 'Business_name', 'City_agency', 'Neighborhood', 'Building_Classification', 'Areas_of_study',
                      'School_Levels', 'Borough', 'Subjects_in_school', 'Parks_Playgrounds', 'Zip_code', 'Address', 'Street_name',
                      'Phone_Number', 'City', 'LAT_LON_coordinates', 'School_name', 'Car_make', 'Vehicle_Type', 'Type_of_location',
                      'Websites', 'Color', 'College_University_names', 'Other']
    b29 = [1.0, 1.0, 0.9166666666666666, 0.75, 1.0, 0.8846153846153846, 0.6363636363636364, 0.6666666666666666,
                           0.6666666666666666, 0.3333333333333333, 1.0, 0.5714285714285714, 0.6551724137931034, 0.9090909090909091,
                           0.5294117647058824, 1.0, 0.8, 0.7, 0.5, 1.0, 1.0, 1.0, 0.0, 0.4858490566037736]
    b30 = [0.8387096774193549, 0.8888888888888888, 1.0, 1.0, 1.0, 1.0, 0.9333333333333333, 1.0, 1.0, 0.5, 0.7857142857142857,
                        0.7619047619047619, 0.9047619047619048, 0.8333333333333334, 1.0, 0.9, 0.8421052631578947, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0,
                        0.9363636363636364]
    b31 = [1.0, 1.0, 0.9166666666666666, 1.0, 1.0, 1.0, 1.0, 1.0, 0.125, 0.7142857142857143, 1.0, 1.0, 0.8095238095238095,
                          0.9090909090909091, 0.0, 1.0, 0.8461538461538461, 0.7, 0.0, 1.0, 1.0, 1.0, 0.0, 0.584]
    b32 = [0.8387096774193549, 0.8888888888888888, 1.0, 0.7142857142857143, 1.0, 0.43478260869565216, 0.8666666666666667,
                       0.5909090909090909, 1.0, 0.5, 0.7857142857142857, 0.38095238095238093, 0.8095238095238095, 0.8333333333333334, 0.0,
                       0.9, 0.5789473684210527, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.6636363636363637]
    plt.clf()
    plt.figure(b33 = (10, 8))
    plt.plot(b28, b31, b15 = 'b', label='Original')
    plt.plot(b28, b29, b15 = 'r', label='Optimized')
    plt.b27('Original precision vs. Optimized precision')
    plt.b26('Semantic Type')
    plt.b38('Precision')
    plt.xticks(b34 = -90, fontsize=5)
    plt.legend()
    plt.savefig('precision.png')
    plt.clf()
    plt.figure(b33 = (10, 8))
    plt.plot(b28, b32, b15 = 'b', label='Original')
    plt.plot(b28, b30, b15 = 'r', label='Optimized')
    plt.b27('Original recall vs. Optimized recall')
    plt.b26('Semantic Type')
    plt.b38('Recall')
    plt.xticks(b34 = -90, fontsize=5)
    plt.legend()
    plt.savefig('recall.png')
    b1 = os.listdir(b23)
    b35 = []
    for file in b1:
        with open(os.path.join(b23, file)) as f:
            b3 = json.load(f)
        b36 = b3['b28']
        b35.append(len(b36))
    b37 = collections.OrderedDict(sorted(dict((x, b35.count(x)) for x in set(b35)).items()))
    fonk4(b37, b27 = 'Prevalence of heterogeneous b9', b26='Number of semantic b10 in the column',
                   b38 = 'Count of b9', file_name='heterogeneous.png')
if b39 = = "__main__":
    fonk6()