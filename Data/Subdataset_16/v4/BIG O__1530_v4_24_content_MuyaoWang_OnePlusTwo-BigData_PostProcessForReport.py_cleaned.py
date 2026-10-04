import os
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import collections
def fonk1(path, root_name, new_file_name):
    b1 = os.listdir(path)
    b2 = []
    for file in b1:
        with open(os.path.join(path, file)) as f:
            b3 = json.load(f)
        b2.append(b3)
    b4 = {root_name: b2}
    with open(new_file_name, 'w') as f:
        json.dump(b4, f)
def fonk2(b32, b33):
    fonk1(b32, 'datasets', 'task1.json')
    fonk1(b33, 'predicted_types', 'task2.json')
    b5 = []
    b6 = []
    b7 = []
    b8 = []
    b9 = []
    b1 = os.listdir(b32)
    for file in b1:
        with open(os.path.join(b32, file)) as f:
            b3 = json.load(f)
        a1 = 0
        a2 = 0
        a3 = 0
        a4 = 0
        b10 = b3['columns']
        for column in b10:
            b11 = set()
            b12 = column['data_types']
            if not b12:
                print(f"Dataset: {b3['dataset_name']}, Column: {column['column_name']}")
            for data_type in b12:
                b13 = data_type['type']
                b11.add(b13)
                if b13 = = 'INTEGER(LONG)':
                    a1 += 1
                elif b13 = = 'REAL':
                    a2 += 1
                elif b13 = = 'DATE/TIME':
                    a3 += 1
                else:
                    a4 += 1
            b9.append(b11)
        b5.append(a1)
        b6.append(a2)
        b7.append(a3)
        b8.append(a4)
    print('Number of columns containing INTEGER(LONG) type:', sum(b5))
    print('Number of columns containing REAL type:', sum(b6))
    print('Number of columns containing DATE/TIME type:', sum(b7))
    print('Number of columns containing TEXT type:', sum(b8))
    def fonk3(data, title, xlabel, ylabel, filename, b14 = 50):
        plt.clf()
        plt.hist(data, b14 = b14, b20='blue')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(b15 = 'y', alpha=0.75)
        plt.savefig(filename)
    fonk3(b5, 'Histogram for INTEGER/LONG type', 'Number of columns with INTEGER(LONG) type', 'Count of datasets', 'integer.png')
    fonk3(b5, 'Histogram for INTEGER/LONG type (under 100)', 'Number of columns with INTEGER(LONG) type (under 100)', 'Count of datasets', 'integer_under100.png', b14 = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])
    fonk3(b6, 'Histogram for REAL type', 'Number of columns with REAL type', 'Count of datasets', 'real.png')
    fonk3(b7, 'Histogram for DATE/TIME type', 'Number of columns with DATE/TIME type', 'Count of datasets', 'datetime.png')
    fonk3(b8, 'Histogram for TEXT type', 'Number of columns with TEXT type', 'Count of datasets', 'text.png')
    fonk3(b8, 'Histogram for TEXT type (under 100)', 'Number of columns with TEXT type (under 100)', 'Count of datasets', 'text_under100.png', b14 = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])
    b16 = []
    b17 = {
        frozenset({'INTEGER(LONG)'}): 'I',
        frozenset({'REAL'}): 'R',
        frozenset({'DATE/TIME'}): 'D',
        frozenset({'TEXT'}): 'T',
        frozenset({'INTEGER(LONG)', 'REAL'}): 'IR',
        frozenset({'INTEGER(LONG)', 'DATE/TIME'}): 'ID',
        frozenset({'INTEGER(LONG)', 'TEXT'}): 'IT',
        frozenset({'REAL', 'DATE/TIME'}): 'RD',
        frozenset({'REAL', 'TEXT'}): 'RT',
        frozenset({'DATE/TIME', 'TEXT'}): 'DT',
        frozenset({'INTEGER(LONG)', 'REAL', 'DATE/TIME'}): 'IRD',
        frozenset({'INTEGER(LONG)', 'REAL', 'TEXT'}): 'IRT',
        frozenset({'INTEGER(LONG)', 'DATE/TIME', 'TEXT'}): 'IDT',
        frozenset({'REAL', 'DATE/TIME', 'TEXT'}): 'RDT',
        frozenset({'INTEGER(LONG)', 'REAL', 'DATE/TIME', 'TEXT'}): 'IRDT'
    }
    for b11 in b9:
        b16.append(b17.get(frozenset(b11), 'Empty'))
    b18 = dict((x, b16.count(x)) for x in set(b16))
    b19 = dict(sorted(b18.items(), key=lambda item: len(item[0])))
    plt.clf()
    plt.bar(b19.keys(), b19.values(), b20 = 'blue')
    plt.title('Frequent Itemsets')
    plt.xlabel('Frequent Itemsets')
    plt.ylabel('Count')
    plt.grid(b15 = 'y', alpha=0.75)
    plt.savefig('frequent.png')
    b21 = ['Person_name', 'Business_name', 'City_agency', 'Neighborhood', 'Building_Classification', 'Areas_of_study',
                     'School_Levels', 'Borough', 'Subjects_in_school', 'Parks_Playgrounds', 'Zip_code', 'Address', 'Street_name',
                     'Phone_Number', 'City', 'LAT_LON_coordinates', 'School_name', 'Car_make', 'Vehicle_Type', 'Type_of_location',
                     'Websites', 'Color', 'College_University_names', 'Other']
    b22 = [1.0, 1.0, 0.9166666666666666, 1.0, 1.0, 1.0, 1.0, 1.0, 0.125, 0.7142857142857143, 1.0, 1.0, 0.8095238095238095, 0.9090909090909091, 0.0, 1.0, 0.8461538461538461, 0.7, 0.0, 1.0, 1.0, 1.0, 0.0, 0.584]
    b23 = [0.8387096774193549, 0.8888888888888888, 1.0, 0.7142857142857143, 1.0, 0.43478260869565216, 0.8666666666666667, 0.5909090909090909, 1.0, 0.5, 0.7857142857142857, 0.38095238095238093, 0.8095238095238095, 0.8333333333333334, 0.0, 0.9, 0.5789473684210527, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.6636363636363637]
    b24 = [1.0, 1.0, 0.9166666666666666, 0.75, 1.0, 0.8846153846153846, 0.6363636363636364, 0.6666666666666666, 0.6666666666666666, 0.3333333333333333, 1.0, 0.5714285714285714, 0.6551724137931034, 0.9090909090909091, 0.5294117647058824, 1.0, 0.8, 0.7, 0.5, 1.0, 1.0, 1.0, 0.0, 0.4858490566037736]
    b25 = [0.8387096774193549, 0.8888888888888888, 1.0, 1.0, 1.0, 1.0, 0.9333333333333333, 1.0, 1.0, 0.5, 0.7857142857142857, 0.7619047619047619, 0.9047619047619048, 0.8333333333333334, 1.0, 0.9, 0.8421052631578947, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.9363636363636364]
    def fonk4(metric, original, optimized, title, ylabel, filename):
        plt.clf()
        plt.figure(b26 = (10, 8))
        plt.plot(b21, original, b20 = 'b', label='Original')
        plt.plot(b21, optimized, b20 = 'r', label='Optimized')
        plt.title(title)
        plt.xlabel('Semantic Type')
        plt.ylabel(ylabel)
        plt.xticks(b27 = -90, fontsize=5)
        plt.legend()
        plt.savefig(filename)
    fonk4('Precision', b22, b24, 'Original precision vs. Optimized precision', 'Precision', 'precision.png')
    fonk4('Recall', b23, b25, 'Original recall vs. Optimized recall', 'Recall', 'recall.png')
    b1 = os.listdir(b33)
    b28 = []
    for file in b1:
        with open(os.path.join(b33, file)) as f:
            b3 = json.load(f)
        b29 = b3['semantic_types']
        b28.append(len(b29))
    b30 = dict(collections.Counter(b28))
    b30 = collections.OrderedDict(sorted(b30.items()))
    plt.clf()
    plt.bar(b30.keys(), b30.values(), b20 = 'blue')
    plt.title('Prevalence of heterogeneous columns')
    plt.xlabel('Number of semantic b11 in the column')
    plt.ylabel('Count of columns')
    plt.grid(b15 = 'y', alpha=0.75)
    plt.savefig('heterogeneous.png')
if b31 = = "__main__":
    b32 = 'Result-Task1'
    b33 = 'Result-Task2'
    fonk2(b32, b33)