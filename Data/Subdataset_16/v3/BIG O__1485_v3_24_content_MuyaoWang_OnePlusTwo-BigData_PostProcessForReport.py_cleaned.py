import os
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import collections
def fonk1(path, root_name, new_file_name):
    b1 = {root_name: []}
    for file in os.listdir(path):
        with open(os.path.join(path, file)) as f:
            b2 = json.load(f)
            b1[root_name].append(b2)
    with open(new_file_name, 'w') as f:
        json.dump(b1, f)
def fonk2(path):
    b3 = []
    b4 = []
    b5 = []
    b6 = []
    b7 = []
    for file in os.listdir(path):
        with open(os.path.join(path, file)) as f:
            b2 = json.load(f)
        integer_count, real_count, datetime_count, b8 = 0, 0, 0, 0
        for column in b2['columns']:
            b9 = set()
            for data_type in column['data_types']:
                b10 = data_type['type']
                b9.add(b10)
                if b10 = = 'INTEGER(LONG)':
                    integer_count += 1
                elif b10 = = 'REAL':
                    real_count += 1
                elif b10 = = 'DATE/TIME':
                    datetime_count += 1
                else:
                    b8 += 1
            b7.append(b9)
        b3.append(integer_count)
        b4.append(real_count)
        b5.append(datetime_count)
        b6.append(b8)
    print('Number of columns containing INTEGER(LONG) type:', sum(b3))
    print('Number of columns containing REAL type:', sum(b4))
    print('Number of columns containing DATE/TIME type:', sum(b5))
    print('Number of columns containing TEXT type:', sum(b6))
    return b3, b4, b5, b6, b7
def fonk3(data, b11, b27, b26, b37, file_name):
    plt.clf()
    plt.hist(data, b11 = b11, b13='blue', alpha=0.7)
    plt.b27(b27)
    plt.b26(b26)
    plt.b37(b37)
    plt.grid(b12 = 'y', alpha=0.75)
    plt.savefig(file_name)
def fonk4(data_dict, b27, b26, b37, file_name):
    plt.clf()
    plt.bar(data_dict.keys(), data_dict.values(), b13 = 'blue', alpha=0.7)
    plt.b27(b27)
    plt.b26(b26)
    plt.b37(b37)
    plt.grid(b12 = 'y', alpha=0.75)
    plt.savefig(file_name)
def fonk5(b7):
    b14 = []
    for b9 in b7:
        b15 = ''.join(sorted([t[0] for t in b9]))
        b14.append(b15)
    b16 = dict((x, b14.count(x)) for x in set(b14))
    b17 = dict(sorted(b16.items(), key=lambda item: len(item[0])))
    return b17
def fonk6(b28, b31, b29, b32, b30):
    plt.clf()
    plt.figure(b18 = (10, 8))
    plt.plot(b28, b31, b13 = 'b', label='Original')
    plt.plot(b28, b29, b13 = 'r', label='Optimized')
    plt.b27('Original precision vs. Optimized precision')
    plt.b26('Semantic Type')
    plt.b37('Precision')
    plt.xticks(b19 = -90, fontsize=5)
    plt.legend()
    plt.savefig('precision.png')
    plt.clf()
    plt.figure(b18 = (10, 8))
    plt.plot(b28, b32, b13 = 'b', label='Original')
    plt.plot(b28, b30, b13 = 'r', label='Optimized')
    plt.b27('Original recall vs. Optimized recall')
    plt.b26('Semantic Type')
    plt.b37('Recall')
    plt.xticks(b19 = -90, fontsize=5)
    plt.legend()
    plt.savefig('recall.png')
def fonk7():
    b20 = 'Result-Task1'
    b21 = 'datasets'
    b22 = 'task1.json'
    fonk1(b20, b21, b22)
    b23 = 'Result-Task2'
    b24 = 'predicted_types'
    b25 = 'task2.json'
    fonk1(b23, b24, b25)
    b3, b4, b5, b6, b7 = fonk2(b20)
    fonk3(b3, b11 = 50, b27='Histogram for INTEGER/LONG type',
                   b26 = 'Number of columns with INTEGER(LONG) type', b37='Count of datasets', file_name='integer.png')
    fonk3(b3, b11 = list(range(0, 105, 5)), b27='Histogram for INTEGER/LONG type (under 100)',
                   b26 = 'Number of columns with INTEGER(LONG) type (under 100)', b37='Count of datasets', file_name='integer_under100.png')
    fonk3(b4, b11 = 50, b27='Histogram for REAL type',
                   b26 = 'Number of columns with REAL type', b37='Count of datasets', file_name='real.png')
    fonk3(b5, b11 = 50, b27='Histogram for DATE/TIME type',
                   b26 = 'Number of columns with DATE/TIME type', b37='Count of datasets', file_name='datetime.png')
    fonk3(b6, b11 = 50, b27='Histogram for TEXT type',
                   b26 = 'Number of columns with TEXT type', b37='Count of datasets', file_name='text.png')
    fonk3(b6, b11 = list(range(0, 105, 5)), b27='Histogram for TEXT type (under 100)',
                   b26 = 'Number of columns with TEXT type (under 100)', b37='Count of datasets', file_name='text_under100.png')
    b17 = fonk5(b7)
    fonk4(b17, b27 = 'Frequent Itemsets', b26='Frequent Itemsets', b37='Count', file_name='frequent.png')
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
    fonk6(b28, b31, b29, b32, b30)
    b33 = os.listdir(b23)
    b34 = []
    for file in b33:
        with open(os.path.join(b23, file)) as f:
            b2 = json.load(f)
        b35 = b2['b28']
        b34.append(len(b35))
    b36 = collections.OrderedDict(sorted(dict((x, b34.count(x)) for x in set(b34)).items()))
    fonk4(b36, b27 = 'Prevalence of heterogeneous columns', b26='Number of semantic b9 in the column',
                   b37 = 'Count of columns', file_name='heterogeneous.png')
if b38 = = "__main__":
    fonk7()