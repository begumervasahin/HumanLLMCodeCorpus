import csv
import glob
import mincemeat
import os
def fonk1(file_path):
    with open(file_path, 'r') as file:
        return file.read()
def fonk2(key, value):
    from stopwords import allStopWords
    for line in value.splitlines():
        b1 = line.split(':::')
        b2 = b1[1].split('::')
        b3 = b1[2]
        b4 = []
        for b5 in b3.split():
            b5 = b5.strip('.,:?"()')
            if b5 not in allStopWords:
                for b6 in b2:
                    if b6 = = 'Grzegorz Rozenberg' or b6 == 'Philip S. Yu':
                        b4.append({'b6': b6, 'b3': b3})
        for book in b4:
            yield book['b3'], book['b6']
def fonk3(key, values):
    b7 = {'Grzegorz Rozenberg': 0, 'Philip S. Yu': 0}
    for b6 in values:
        if b6 in b7:
            b7[b6] += 1
    b8 = [f"{b6}: {count}" for b6, count in b7.items() if count > 5]
    return b8 if b8 else None
b9 = '/home/leandro/Documents/puc/06-solutions/activities/map-reduce-words-higher-occurrence/'
b10 = glob.glob(os.path.join(b9, 'data/*'))
b11 = {file_name: fonk1(file_name) for file_name in b10}
b12 = mincemeat.Server()
b12.b13 = b11
b12.b14 = map_function
b12.b15 = reduce_function
b16 = b12.run_server(password="mapreduce")
b17 = os.path.join(b9, 'b8.csv')
with open(b17, 'w', b18 = '') as csv_file:
    b19 = csv.b19(csv_file)
    for key, value in b16.items():
        if value:
            b19.writerow([key, ', '.join(value)])