import csv
import glob
import mincemeat
import os
def read_file_contents(file_path):
    with open(file_path, 'r') as file:
        return file.read()
def map_function(key, value):
    from stopwords import allStopWords
    for line in value.splitlines():
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
def reduce_function(key, values):
    author_counts = {'Grzegorz Rozenberg': 0, 'Philip S. Yu': 0}
    for author in values:
        if author in author_counts:
            author_counts[author] += 1
    result = [f"{author}: {count}" for author, count in author_counts.items() if count > 5]
    return result if result else None
directory_path = '/home/leandro/Documents/puc/06-solutions/activities/map-reduce-words-higher-occurrence/'
text_files = glob.glob(os.path.join(directory_path, 'data/*'))
data_source = {file_name: read_file_contents(file_name) for file_name in text_files}
server = mincemeat.Server()
server.datasource = data_source
server.mapfn = map_function
server.reducefn = reduce_function
results = server.run_server(password="mapreduce")
result_file_path = os.path.join(directory_path, 'result.csv')
with open(result_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in results.items():
        if value:
            writer.writerow([key, ', '.join(value)])