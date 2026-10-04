import csv
from collections import defaultdict
def load_csv(input_filename, output_filename='output.csv'):
    with open(output_filename, 'w', newline='') as clusterfile:
        writer = csv.writer(clusterfile)
        with open(input_filename, 'r', newline='') as f:
            reader = csv.reader(f)
            headers = next(reader)
            required_columns = ["Lon", "Lat", "Text_General_Code"]
            writer.writerow([headers[12], headers[13], headers[9]])
            columns = defaultdict(list)
            reader = csv.DictReader(f, fieldnames=headers)
            for row in reader:
                for k, v in row.items():
                    columns[k].append(v)
            for i in range(len(columns["Lon"])):
                writer.writerow([columns["Lon"][i], columns["Lat"][i], columns["Text_General_Code"][i]])
def main():
    input_filename = 'input.csv'
    load_csv(input_filename)
if __name__ == "__main__":
    main()