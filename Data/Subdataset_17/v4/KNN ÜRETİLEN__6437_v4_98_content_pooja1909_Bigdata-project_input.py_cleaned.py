import csv
from collections import defaultdict
def loadCsv(filename):
    output_filename = 'output.csv'
    with open(output_filename, 'w', newline='') as clusterfile:
        writer = csv.writer(clusterfile)
        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            headers = next(reader)
            writer.writerow([headers[12], headers[13], headers[9]])
            columns = defaultdict(list)
            reader = csv.DictReader(f, fieldnames=headers)
            for row in reader:
                for k, v in row.items():
                    columns[k].append(v)
            for i in range(len(columns["Lon"])):
                writer.writerow([columns["Lon"][i], columns["Lat"][i], columns["Text_General_Code"][i]])
def main():
    filename = 'input.csv'
    loadCsv(filename)
if __name__ == "__main__":
    main()