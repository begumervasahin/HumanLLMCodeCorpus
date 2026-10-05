import csv
from collections import defaultdict
def load_csv(input_filename, output_filename='output.csv'):
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        csv_reader = csv.DictReader(input_file)
        csv_writer = csv.writer(output_file)
        headers = next(csv_reader)
        csv_writer.writerow([headers['Lon'], headers['Lat'], headers['Text_General_Code']])
        for row in csv_reader:
            csv_writer.writerow([row['Lon'], row['Lat'], row['Text_General_Code']])
def main():
    input_filename = 'input.csv'
    output_filename = 'output.csv'
    load_csv(input_filename, output_filename)
if __name__ == '__main__':
    main()