import csv
import itertools
import sys
def read_extracted_csv(input_file):
    SIZE_OF_DISK = 250
    TOTAL_NO_BINS = int((SIZE_OF_DISK * 1024) / 128)
    lba_list = []
    xfrlen_list = []
    timestamp_list = []
    operation_list = []
    bin_list = []
    flag = False
    with open(input_file, 'r') as extracted_csv:
        for line in extracted_csv:
            if flag:
                parts = line.strip().split(',')
                try:
                    bin_list.append(int(parts[0]))
                    lba_list.append(int(parts[1]))
                    xfrlen_list.append(int(parts[2]))
                    operation_list.append(parts[3])
                    timestamp_list.append(float(parts[4]))
                except IndexError:
                    continue
            flag = True
    clustered_bins = [list(v) for k, v in itertools.groupby(bin_list)]
    bin_number = []
    bin_count = []
    end_time = []
    xfrlen_bin_sum = []
    operation_bin = []
    counter = 0
    flag_counter = 0
    for bins in clustered_bins:
        bin_number.append(bins[-1])
        bin_count.append(len(bins))
        counter += len(bins)
        end_time.append(timestamp_list[counter - 1])
        operation_bin.append(operation_list[counter - 1])
        xfrlen_bin_sum.append(sum(xfrlen_list[flag_counter:counter]) / (2 * 1024.0))
        flag_counter += len(bins)
    bin_info = zip(bin_number, bin_count, xfrlen_bin_sum, operation_bin, end_time)
    with open(input_file + '_bin_info.csv', 'w+') as bin_info_file:
        bin_info_file.write("bin_number,bin_count,xfrlen_bin_sum(MB),operation_bin,end_time\n")
        writer = csv.writer(bin_info_file, delimiter=',')
        writer.writerows(bin_info)
def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    read_extracted_csv(input_file)
if __name__ == "__main__":
    main()