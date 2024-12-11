import csv
import glob
import sys
import mincemeat
b1 = '/home/leandro/Documents/puc/06-solutions/activities/map-reduce-words-higher-occurrence/'
b2 = glob.glob(b1 + 'data/*')
def file_contents (file_name):
    b3 = open(file_name)
    try:
        return b3.read()
    finally:
        b3.close()
def b18 (k, v):
    from stopwords import allStopWords
    for line in v.splitlines():
        b4 = line.split(':::')
        b5 = b4[1]
        b6 = b4[2]
        b7 = ''
        for b8 in b6.split():
            b8 = b8.replace('.', '').replace(',', '').replace(':', '').replace('?', '').replace('(', '').replace(')', '').replace('"', '').replace("''", '')
            if (b8 not in allStopWords):
                for b9 in b5.split('::'):
                    if b9 = = 'Grzegorz Rozenberg' or b9 == 'Philip S. Yu':
                        b7 = 'b9: ' + b9 + '; b6: ' + b6
                        yield b8, b9
        if b7 != '': print b7
def b19 (k, v):
    b5 = ''
    b10 = totalRozenberg = 0
    b11 = b13 = False
    for index, b12 in enumerate(v):
        if b12 = = 'Grzegorz Rozenberg':
            b13 = True
            totalRozenberg += 1
        if b12 = = 'Philip S. Yu':
            b11 = True
            b10 += 1
    if b10 > 5 or totalRozenberg > 5:
        b14 = list()
        b5 += 'Grzegorz Rozenberg: ' + str(totalRozenberg) + '; ' if b13 else ''
        b5 += 'Philip S. Yu: ' + str(b10) if b11 else ''
        b14.append(b5)
        return b14
    else:
        return None
b15 = dict( (file_name, file_contents(file_name)) for file_name in b2 )
b16 = mincemeat.Server()
b16.b17 = b15
b16.b18 = b18
b16.b19 = b19
b20 = b16.run_server(password="mapreduce")
b21 = csv.writer( open(b1 + 'result.csv', 'b21') )
for k, v in b20.items():
    if v != None:
        b21.writerow([k, v])