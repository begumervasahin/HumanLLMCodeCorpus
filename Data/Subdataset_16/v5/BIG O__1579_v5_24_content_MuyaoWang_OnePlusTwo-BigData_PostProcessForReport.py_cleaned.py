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
def fonk2(b28, b29):
    fonk1(b28, 'datasets', 'task1.json')
    fonk1(b29, 'predicted_types', 'task2.json')
    integer_count_list, real_count_list, datetime_count_list, b5 = [], [], [], []
    b6 = []
    b1 = os.listdir(b28)
    for file in b1:
        with open(os.path.join(b28, file)) as f:
            b3 = json.load(f)
        integer_count, real_count, datetime_count, b7 = 0, 0, 0, 0
        for column in b3['columns']:
            b8 = set()
            for data_type in column['data_types']:
                b9 = data_type['type']
                b8.add(b9)
                if b9 = = 'INTEGER(LONG)':
                    integer_count += 1
                elif b9 = = 'REAL':
                    real_count += 1
                elif b9 = = 'DATE/TIME':
                    datetime_count += 1
                else:
                    b7 += 1
            b6.append(b8)
        integer_count_list.append(integer_count)
        real_count_list.append(real_count)
        datetime_count_list.append(datetime_count)
        b5.append(b7)
    print(f"Number of columns containing INTEGER(LONG) type: {sum(integer_count_list)}")
    print(f"Number of columns containing REAL type: {sum(real_count_list)}")
    print(f"Number of columns containing DATE/TIME type: {sum(datetime_count_list)}")
    print(f"Number of columns containing TEXT type: {sum(b5)}")
    def fonk3(data, title, xlabel, ylabel, filename, b10 = 50):
        plt.clf()
        plt.hist(data, b10 = b10, b16='blue')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(b11 = 'y', alpha=0.75)
        plt.savefig(filename)
    fonk3(integer_count_list, 'Histogram for INTEGER/LONG type', 'Number of columns with INTEGER(LONG) type', 'Count of datasets', 'integer.png')
    fonk3(integer_count_list, 'Histogram for INTEGER/LONG type (under 100)', 'Number of columns with INTEGER(LONG) type (under 100)', 'Count of datasets', 'integer_under100.png', b10 = range(0, 101, 5))
    fonk3(real_count_list, 'Histogram for REAL type', 'Number of columns with REAL type', 'Count of datasets', 'real.png')
    fonk3(datetime_count_list, 'Histogram for DATE/TIME type', 'Number of columns with DATE/TIME type', 'Count of datasets', 'datetime.png')
    fonk3(b5, 'Histogram for TEXT type', 'Number of columns with TEXT type', 'Count of datasets', 'text.png')
    fonk3(b5, 'Histogram for TEXT type (under 100)', 'Number of columns with TEXT type (under 100)', 'Count of datasets', 'text_under100.png', b10 = range(0, 101, 5))
    b12 = {
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
    b13 = [b12.get(frozenset(b8), 'Empty') for b8 in b6]
    b14 = dict(collections.Counter(b13))
    b15 = dict(sorted(b14.items(), key=lambda item: len(item[0])))
    plt.clf()
    plt.bar(b15.keys(), b15.values(), b16 = 'blue')
    plt.title('Frequent Itemsets')
    plt.xlabel('Frequent Itemsets')
    plt.ylabel('Count')
    plt.grid(b11 = 'y', alpha=0.75)
    plt.savefig('frequent.png')
    b17 = ['Person_name', 'Business_name', 'City_agency', 'Neighborhood', 'Building_Classification', 'Areas_of_study',
                     'School_Levels', 'Borough', 'Subjects_in_school', 'Parks_Playgrounds', 'Zip_code', 'Address', 'Street_name',
                     'Phone_Number', 'City', 'LAT_LON_coordinates', 'School_name', 'Car_make', 'Vehicle_Type', 'Type_of_location',
                     'Websites', 'Color', 'College_University_names', 'Other']
    b18 = [1.0, 1.0, 0.9166666666666666, 1.0, 1.0, 1.0, 1.0, 1.0, 0.125, 0.7142857142857143, 1.0, 1.0, 0.8095238095238095, 0.9090909090909091, 0.0, 1.0, 0.8461538461538461, 0.7, 0.0, 1.0, 1.0, 1.0, 0.0, 0.584]
    b19 = [0.8387096774193549, 0.8888888888888888, 1.0, 0.7142857142857143, 1.0, 0.43478260869565216, 0.8666666666666667, 0.5909090909090909, 1.0, 0.5, 0.7857142857142857, 0.38095238095238093, 0.8095238095238095, 0.8333333333333334, 0.0, 0.9, 0.5789473684210527, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.6636363636363637]
    b20 = [1.0, 1.0, 0.9166666666666666, 0.75, 1.0, 0.8846153846153846, 0.6363636363636364, 0.6666666666666666, 0.6666666666666666, 0.3333333333333333, 1.0, 0.5714285714285714, 0.6551724137931034, 0.9090909090909091, 0.5294117647058824, 1.0, 0.8, 0.7, 0.5, 1.0, 1.0, 1.0, 0.0, 0.4858490566037736]
    b21 = [0.8387096774193549, 0.8888888888888888, 1.0, 1.0, 1.0, 1.0, 0.9333333333333333, 1.0, 1.0, 0.5, 0.7857142857142857, 0.7619047619047619, 0.9047619047619048, 0.8333333333333334, 1.0, 0.9, 0.8421052631578947, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.9363636363636364]
    def fonk4(metric, original, optimized, title, ylabel, filename):
        plt.clf()
        plt.figure(b22 = (10, 8))
        plt.plot(b17, original, b16 = 'b', label='Original')
        plt.plot(b17, optimized, b16 = 'r', label='Optimized')
        plt.title(title)
        plt.xlabel('Semantic Type')
        plt.ylabel(ylabel)
        plt.xticks(b23 = -90, fontsize=5)
        plt.legend()
        plt.savefig(filename)
    fonk4('Precision', b18, b20, 'Original precision vs. Optimized precision', 'Precision', 'precision.png')
    fonk4('Recall', b19, b21, 'Original recall vs. Optimized recall', 'Recall', 'recall.png')
    b1 = os.listdir(b29)
    b24 = []
    for file in b1:
        with open(os.path.join(b29, file)) as f:
            b3 = json.load(f)
        b25 = b3['semantic_types']
        b24.append(len(b25))
    b26 = dict(collections.Counter(b24))
    b26 = collections.OrderedDict(sorted(b26.items()))
    plt.clf()
    plt.bar(b26.keys(), b26.values(), b16 = 'blue')
    plt.title('Prevalence of heterogeneous columns')
    plt.xlabel('Number of semantic b8 in the column')
    plt.ylabel('Count of columns')
    plt.grid(b11 = 'y', alpha=0.75)
    plt.savefig('heterogeneous.png')
if b27 = = "__main__":
    b28 = 'Result-Task1'
    b29 = 'Result-Task2'
    fonk2(b28, b29)