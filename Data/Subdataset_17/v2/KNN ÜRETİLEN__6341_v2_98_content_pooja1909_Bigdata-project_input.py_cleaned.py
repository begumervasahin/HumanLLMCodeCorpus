import csv
from collections import defaultdict
def load_csv(input_filename, output_filename='output.csv'):
    columns = defaultdict(list)
    with open(input_filename, 'r') as infile:
        reader = csv.reader(infile)
        headers = next(reader)
        infile.seek(0)
        dict_reader = csv.DictReader(infile)
        for row in dict_reader:
            for (k, v) in row.items():
                columns[k].append(v)
    with open(output_filename, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow([headers[12], headers[13], headers[9]])
        for i in range(len(columns["Lon"])):
            writer.writerow([columns["Lon"][i], columns["Lat"][i], columns["Text_General_Code"][i]])
def main():
    input_filename = 'input.csv'
    load_csv(input_filename)
if __name__ == "__main__":
    main()