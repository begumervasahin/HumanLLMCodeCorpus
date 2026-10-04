import csv
from collections import defaultdict
def loadCsv(filename):
    with open('output.csv', 'w', newline='') as clusterfile:
        writer = csv.writer(clusterfile)
        columns = defaultdict(list)
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            headers = next(reader)
            writer.writerow([headers[12], headers[13], headers[9]])
            f.seek(0)
            reader = csv.DictReader(f)
            for row in reader:
                for (k, v) in row.items():
                    columns[k].append(v)
            for i in range(len(columns["Lon"])):
                writer.writerow([columns["Lon"][i], columns["Lat"][i], columns["Text_General_Code"][i]])
def main():
    filename = 'input.csv'
    loadCsv(filename)
if __name__ == "__main__":
    main()