import csv
from collections import defaultdict
def loadCsv(input_filename, output_filename):
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        reader = csv.DictReader(input_file)
        writer = csv.writer(output_file)
        writer.writerow(['Lon', 'Lat', 'Text_General_Code'])
        for row in reader:
            lon = row['Lon']
            lat = row['Lat']
            code = row['Text_General_Code']
            writer.writerow([lon, lat, code])
def main():
    input_filename = 'input.csv'
    output_filename = 'output.csv'
    loadCsv(input_filename, output_filename)
if __name__ == "__main__":
    main()