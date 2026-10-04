import csv
import glob
import os
import mincemeat
DATA_PATH = '/home/leandro/Documents/puc/06-solutions/activities/map-reduce-words-higher-occurrence/data'
text_files = glob.glob(os.path.join(DATA_PATH, '*'))
def file_contents(file_name):
    with open(file_name, 'r') as f:
        return f.read()
def mapfn(k, v):
    from stopwords import allStopWords
    for line in v.splitlines():
        fields = line.split(':::')
        authors = fields[1]
        title = fields[2]
        for word in title.split():
            word = word.strip('.,:?"()')
            if word.lower() not in allStopWords:
                for author in authors.split('::'):
                    if author in ['Grzegorz Rozenberg', 'Philip S. Yu']:
                        yield word, author
def reducefn(k, v):
    author_counts = {'Grzegorz Rozenberg': 0, 'Philip S. Yu': 0}
    for author in v:
        if author in author_counts:
            author_counts[author] += 1
    result = [f'{author}: {count}' for author, count in author_counts.items() if count > 5]
    return result if result else None
def main():
    source = {file_name: file_contents(file_name) for file_name in text_files}
    server = mincemeat.Server()
    server.datasource = source
    server.mapfn = mapfn
    server.reducefn = reducefn
    results = server.run_server(password="mapreduce")
    output_file = os.path.join(DATA_PATH, 'result.csv')
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for word, authors in results.items():
            if authors:
                writer.writerow([word, ', '.join(authors)])
if __name__ == "__main__":
    main()