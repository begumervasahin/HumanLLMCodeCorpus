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
if b9 = = "__main__":
    b10 = {file_name: fonk1(file_name) for file_name in b2}
    b11 = mincemeat.Server()
    b11.b12 = b10
    b11.b13 = b13
    b11.b14 = b14
    b15 = b11.run_server(password="mapreduce")
    with open(b1 + 'result.csv', 'w', b16 = '') as csvfile:
        b17 = csv.b17(csvfile)
        for k, v in b15.items():
            if v is not None:
                b17.writerow([k, v])