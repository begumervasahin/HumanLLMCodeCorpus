import csv
import glob
import os
import mincemeat
b1 = '/home/leandro/Documents/puc/06-solutions/activities/map-reduce-words-higher-occurrence/data'
b2 = glob.glob(os.path.join(b1, '*'))
def fonk1(file_name):
    with open(file_name, 'r') as f:
        return f.read()
def fonk2(k, v):
    from stopwords import allStopWords
    for line in v.splitlines():
        b3 = line.split(':::')
        b4 = b3[1]
        b5 = b3[2]
        for b6 in b5.split():
            b6 = b6.strip('.,:?"()')
            if b6.lower() not in allStopWords:
                for author in b4.split('::'):
                    if author in ['Grzegorz Rozenberg', 'Philip S. Yu']:
                        yield b6, author
def fonk3(k, v):
    b7 = {'Grzegorz Rozenberg': 0, 'Philip S. Yu': 0}
    for author in v:
        if author in b7:
            b7[author] += 1
    b8 = [f'{author}: {count}' for author, count in b7.items() if count > 5]
    return b8 if b8 else None
def fonk4():
    b9 = {file_name: fonk1(file_name) for file_name in b2}
    b10 = mincemeat.Server()
    b10.b11 = b9
    b10.b12 = b12
    b10.b13 = b13
    b14 = b10.run_server(password="mapreduce")
    b15 = os.path.join(b1, 'b8.csv')
    with open(b15, 'w', b16 = '') as csvfile:
        b17 = csv.b17(csvfile)
        for b6, b4 in b14.items():
            if b4:
                b17.writerow([b6, ', '.join(b4)])
if b18 = = "__main__":
    fonk4()