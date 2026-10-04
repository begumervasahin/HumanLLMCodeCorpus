import os
import sys
import csv
import itertools
from itertools import groupby
SIZE_OF_DISK = 250
TOTAL_NO_BINS = (SIZE_OF_DISK * 1024 / 128)
def read_extracted_csv(file_path):
    lba_list = []
    xfrlen_list = []
    timestamp_list = []
    operation_list = []
    bin_list = []
    clustered_bins = []
    with open(file_path, 'r') as extracted_csv:
        reader = csv.reader(extracted_csv)
        next(reader)
        for store_line in reader:
            bin_list.append(int(store_line[0]))
            lba_list.append(int(store_line[1]))
            xfrlen_list.append(int(store_line[2]))
            operation_list.append(store_line[3])
            timestamp_list.append(float(store_line[4]))
    clustered_bins = [list(v) for k, v in groupby(bin_list)]
    bin_number = []
    bin_count = []
    end_time = []
    xfrlen_bin_sum = []
    operation_bin = []
    counter = 0
    flag_counter = 0
    for y in clustered_bins:
        bin_number.append(y[-1])
        bin_count.append(len(y))
        counter += len(y)
        end_time.append(timestamp_list[counter-1])
        operation_bin.append(operation_list[counter-1])
        xfrlen_bin_sum.append(sum(xfrlen_list[flag_counter:counter]) / (2 * 1024.0))
        flag_counter += len(y)
    single_bin = list(zip(bin_number, bin_count, xfrlen_bin_sum, operation_bin, end_time))
    output_file = file_path + '_bin_info.csv'
    with open(output_file, 'w+', newline='') as bin_info_file:
        writer = csv.writer(bin_info_file, delimiter=',')
        writer.writerow(["bin_number", "bin_count", "xfrlen_bin_sum(MB)", "operation_bin", "end_time"])
        writer.writerows(single_bin)
def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_csv_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    read_extracted_csv(input_file)
if __name__ == "__main__":
    main()