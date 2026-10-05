import csv
def convert_csv(input_filename, output_filename='output.csv'):
    with open(input_filename, 'r') as input_file, open(output_filename, 'w', newline='') as output_file:
        csv_reader = csv.DictReader(input_file)
        csv_writer = csv.writer(output_file)
        csv_writer.writerow(['Lon', 'Lat', 'Text_General_Code'])
        for row in csv_reader:
            csv_writer.writerow([row['Lon'], row['Lat'], row['Text_General_Code']])
def main():
    input_filename = 'input.csv'
    output_filename = 'output.csv'
    convert_csv(input_filename, output_filename)
if __name__ == '__main__':
    main()