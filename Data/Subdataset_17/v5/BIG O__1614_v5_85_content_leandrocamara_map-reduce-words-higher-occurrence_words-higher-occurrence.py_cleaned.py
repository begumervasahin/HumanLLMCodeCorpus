import csv
import glob
import sys
import mincemeat
PATH = '/home/leandro/Documents/puc/06-solutions/activities/map-reduce-words-higher-occurrence/'
text_files = glob.glob(PATH + 'data/*')
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
            word = word.strip('.,:?!()""')
            if word not in allStopWords:
                for author in authors.split('::'):
                    if author in ['Grzegorz Rozenberg', 'Philip S. Yu']:
                        yield word, author
def reducefn(k, v):
    total_philip = v.count('Philip S. Yu')
    total_rozenberg = v.count('Grzegorz Rozenberg')
    if total_philip > 5 or total_rozenberg > 5:
        authors = []
        if total_rozenberg > 0:
            authors.append(f'Grzegorz Rozenberg: {total_rozenberg}')
        if total_philip > 0:
            authors.append(f'Philip S. Yu: {total_philip}')
        return authors
    return None
def write_results_to_csv(results, path):
    with open(path + 'result.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for k, v in results.items():
            if v is not None:
                writer.writerow([k, v])
def main():
    source = {file_name: file_contents(file_name) for file_name in text_files}
    s = mincemeat.Server()
    s.datasource = source
    s.mapfn = mapfn
    s.reducefn = reducefn
    results = s.run_server(password="mapreduce")
    write_results_to_csv(results, PATH)
if __name__ == "__main__":
    main()