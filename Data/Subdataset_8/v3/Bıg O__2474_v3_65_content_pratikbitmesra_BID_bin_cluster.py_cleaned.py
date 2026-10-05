import csv
import itertools
import sys
def read_extracted_csv(input_file):
    SIZE_OF_DISK = 250
    BYTES_PER_BLOCK = 128
    TOTAL_NO_BINS = int((SIZE_OF_DISK * 1024) / BYTES_PER_BLOCK)
    bin_info = []
    with open(input_file, 'r') as extracted_csv:
        reader = csv.reader(extracted_csv)
        next(reader)
        current_bin = None
        bin_count = 0
        xfrlen_sum = 0
        end_time = None
        operation = None
        for row in reader:
            try:
                bin_num, lba, xfrlen, operation, timestamp = map(int, row[:5])
            except ValueError:
                continue
            if bin_num != current_bin:
                if current_bin is not None:
                    xfrlen_sum_MB = xfrlen_sum / (2 * 1024.0)
                    bin_info.append((current_bin, bin_count, xfrlen_sum_MB, operation, end_time))
                current_bin = bin_num
                bin_count = 0
                xfrlen_sum = 0
            bin_count += 1
            xfrlen_sum += xfrlen
            end_time = timestamp
        if current_bin is not None:
            xfrlen_sum_MB = xfrlen_sum / (2 * 1024.0)
            bin_info.append((current_bin, bin_count, xfrlen_sum_MB, operation, end_time))
    output_file = input_file + '_bin_info.csv'
    with open(output_file, 'w', newline='') as bin_info_file:
        writer = csv.writer(bin_info_file)
        writer.writerow(["bin_number", "bin_count", "xfrlen_bin_sum(MB)", "operation_bin", "end_time"])
        writer.writerows(bin_info)
def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    read_extracted_csv(input_file)
if __name__ == "__main__":
    main()