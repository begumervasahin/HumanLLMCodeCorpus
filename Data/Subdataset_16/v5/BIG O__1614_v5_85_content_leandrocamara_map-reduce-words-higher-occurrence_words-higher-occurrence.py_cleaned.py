import csv
import glob
import sys
import mincemeat
b1 = '/home/leandro/Documents/puc/06-solutions/activities/map-reduce-words-higher-occurrence/'
b2 = glob.glob(b1 + 'data/*')
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
            b6 = b6.strip('.,:?!()""')
            if b6 not in allStopWords:
                for author in b4.split('::'):
                    if author in ['Grzegorz Rozenberg', 'Philip S. Yu']:
                        yield b6, author
def fonk3(k, v):
    b7 = v.count('Philip S. Yu')
    b8 = v.count('Grzegorz Rozenberg')
    if b7 > 5 or b8 > 5:
        b4 = []
        if b8 > 0:
            b4.append(f'Grzegorz Rozenberg: {b8}')
        if b7 > 0:
            b4.append(f'Philip S. Yu: {b7}')
        return b4
    return None
def fonk4(b16, path):
    with open(path + 'result.csv', 'w', b9 = '') as csvfile:
        b10 = csv.b10(csvfile)
        for k, v in b16.items():
            if v is not None:
                b10.writerow([k, v])
def fonk5():
    b11 = {file_name: fonk1(file_name) for file_name in b2}
    b12 = mincemeat.Server()
    b12.b13 = b11
    b12.b14 = b14
    b12.b15 = b15
    b16 = b12.run_server(password="mapreduce")
    fonk4(b16, b1)
if b17 = = "__main__":
    fonk5()