import csv
import glob
import mincemeat
import os
path = '/home/leandro/Documents/puc/06-solutions/activities/map-reduce-words-higher-occurrence/'
text_files = glob.glob(os.path.join(path, 'data', '*'))
def file_contents(file_name):
    with open(file_name, 'r') as f:
        return f.read()
def mapfn(k, v):
    from stopwords import allStopWords
    for line in v.splitlines():
        fields = line.split(':::')
        authors = fields[1]
        title = fields[2]
        valid_book = ''
        for word in title.split():
            word = word.replace('.', '').replace(',', '').replace(':', '').replace('?', '').replace('(', '').replace(')', '').replace('"', '').replace("''", '')
            if word not in allStopWords:
                for author in authors.split('::'):
                    if author == 'Grzegorz Rozenberg' or author == 'Philip S. Yu':
                        valid_book = 'author: ' + author + '; title: ' + title
                        yield word, author
        if valid_book != '':
            print(valid_book)
def reducefn(k, v):
    authors = ''
    total_philip = total_rozenberg = 0
    has_philip = has_rozenberg = False
    for item in v:
        if item == 'Grzegorz Rozenberg':
            has_rozenberg = True
            total_rozenberg += 1
        if item == 'Philip S. Yu':
            has_philip = True
            total_philip += 1
    if total_philip > 5 or total_rozenberg > 5:
        L = list()
        authors += 'Grzegorz Rozenberg: ' + str(total_rozenberg) + '; ' if has_rozenberg else ''
        authors += 'Philip S. Yu: ' + str(total_philip) if has_philip else ''
        L.append(authors)
        return L
    else:
        return None
source = {file_name: file_contents(file_name) for file_name in text_files}
s = mincemeat.Server()
s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn
results = s.run_server(password="mapreduce")
with open(os.path.join(path, 'result.csv'), 'w') as csvfile:
    writer = csv.writer(csvfile)
    for k, v in results.items():
        if v is not None:
            writer.writerow([k, v])