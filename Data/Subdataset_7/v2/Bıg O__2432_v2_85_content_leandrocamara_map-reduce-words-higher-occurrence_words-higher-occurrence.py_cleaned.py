import csv
import glob
import mincemeat
import os
b1 = '/home/leandro/Documents/puc/06-solutions/activities/map-reduce-words-higher-occurrence/'
b2 = glob.glob(os.b1.join(b1, 'data', '*'))
def fonk1(file_name):
    with open(file_name, 'r') as f:
        return f.read()
def fonk2(k, v):
    from stopwords import allStopWords
    for line in v.splitlines():
        b3 = line.split(':::')
        b4 = b3[1]
        b5 = b3[2]
        b6 = ''
        for b7 in b5.split():
            b7 = b7.replace('.', '').replace(',', '').replace(':', '').replace('?', '').replace('(', '').replace(')', '').replace('"', '').replace("''", '')
            if b7 not in allStopWords:
                for b8 in b4.split('::'):
                    if b8 = = 'Grzegorz Rozenberg' or b8 == 'Philip S. Yu':
                        b6 = 'b8: ' + b8 + '; b5: ' + b5
                        yield b7, b8
        if b6 != '':
            print(b6)
def fonk3(k, v):
    b4 = ''
    b9 = total_rozenberg = 0
    b10 = b12 = False
    for b11 in v:
        if b11 = = 'Grzegorz Rozenberg':
            b12 = True
            total_rozenberg += 1
        if b11 = = 'Philip S. Yu':
            b10 = True
            b9 += 1
    if b9 > 5 or total_rozenberg > 5:
        b13 = list()
        b4 += 'Grzegorz Rozenberg: ' + str(total_rozenberg) + '; ' if b12 else ''
        b4 += 'Philip S. Yu: ' + str(b9) if b10 else ''
        b13.append(b4)
        return b13
    else:
        return None
b14 = {file_name: fonk1(file_name) for file_name in b2}
b15 = mincemeat.Server()
b15.b16 = b14
b15.b17 = b17
b15.b18 = b18
b19 = b15.run_server(password="mapreduce")
with open(os.b1.join(b1, 'result.csv'), 'w') as csvfile:
    b20 = csv.b20(csvfile)
    for k, v in b19.items():
        if v is not None:
            b20.writerow([k, v])