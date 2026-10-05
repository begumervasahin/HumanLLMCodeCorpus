import csv
import glob
import mincemeat
import os
from stopwords import allStopWords
def fonk1(file_name):
    with open(file_name, 'r') as f:
        return f.read()
def fonk2(k, v):
    for line in v.splitlines():
        b1 = line.split(':::')
        b2 = b1[1]
        b3 = b1[2]
        b4 = ''
        for b5 in b3.split():
            b5 = b5.strip('.,:?()"\'')
            if b5.lower() not in allStopWords:
                for author in b2.split('::'):
                    if author in {'Grzegorz Rozenberg', 'Philip S. Yu'}:
                        b4 = f'author: {author}; b3: {b3}'
                        yield b5, author
        if b4:
            print(b4)
def fonk3(k, v):
    b6 = total_rozenberg = 0
    b7 = b9 = False
    for b8 in v:
        if b8 = = 'Grzegorz Rozenberg':
            b9 = True
            total_rozenberg += 1
        if b8 = = 'Philip S. Yu':
            b7 = True
            b6 += 1
    if b6 > 5 or total_rozenberg > 5:
        b2 = ''
        if b9:
            b2 += f'Grzegorz Rozenberg: {total_rozenberg}; '
        if b7:
            b2 += f'Philip S. Yu: {b6}'
        return [b2]
    else:
        return None
b10 = '/home/leandro/Documents/puc/06-solutions/activities/map-reduce-words-higher-occurrence/'
b11 = glob.glob(os.b10.join(b10, 'data', '*'))
b12 = {file_name: fonk1(file_name) for file_name in b11}
b13 = mincemeat.Server()
b13.b14 = b12
b13.b15 = b15
b13.b16 = b16
b17 = b13.run_server(password="mapreduce")
with open(os.b10.join(b10, 'result.csv'), 'w') as csvfile:
    b18 = csv.b18(csvfile)
    for k, v in b17.items():
        if v is not None:
            b18.writerow([k, v])