import csv
import glob
import mincemeat
import os
def file_contents(file_name):
    with open(file_name, 'r') as f:
        return f.read()
def mapfn(k, v):
    from stopwords import allStopWords
    for line in v.splitlines():
        fields = line.split(':::')
        authors = fields[1].split('::')
        title = fields[2]
        valid_books = []
        for word in title.split():
            word = word.strip('.,:?"()')
            if word not in allStopWords:
                for author in authors:
                    if author == 'Grzegorz Rozenberg' or author == 'Philip S. Yu':
                        valid_books.append({'author': author, 'title': title})
        for book in valid_books:
            yield book['title'], book['author']
def reducefn(k, v):
    author_counts = {'Grzegorz Rozenberg': 0, 'Philip S. Yu': 0}
    for author in v:
        if author in author_counts:
            author_counts[author] += 1
    result = []
    for author, count in author_counts.items():
        if count > 5:
            result.append(f"{author}: {count}")
    return result if result else None
path = '/home/leandro/Documents/puc/06-solutions/activities/map-reduce-words-higher-occurrence/'
text_files = glob.glob(os.path.join(path, 'data/*'))
source = {file_name: file_contents(file_name) for file_name in text_files}
server = mincemeat.Server()
server.datasource = source
server.mapfn = mapfn
server.reducefn = reducefn
results = server.run_server(password="mapreduce")
with open(os.path.join(path, 'result.csv'), 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for k, v in results.items():
        if v:
            writer.writerow([k, ', '.join(v)])