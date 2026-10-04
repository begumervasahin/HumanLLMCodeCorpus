import codecs
import re
def read_log_file(file_path):
    with codecs.open(file_path, 'r', 'utf-8', 'ignore') as log_file:
        return log_file.readlines()
def write_reversed_log_file(lines, file_path):
    with codecs.open(file_path, 'w+', 'utf-8', 'ignore') as result_log:
        result_log.writelines(lines[::-1])
def find_vvids(lines, pattern):
    vvid_list = []
    vvid_line_numbers = []
    for i, line in enumerate(lines):
        match = re.search(pattern, line)
        if match:
            vvid_list.append(match.group())
            vvid_line_numbers.append(i)
    return vvid_list, vvid_line_numbers
def find_cut_lines(vvid_list, vvid_line_numbers):
    cut_line_numbers = []
    for i in range(1, len(vvid_list)):
        if vvid_list[i] != vvid_list[i - 1]:
            cut_line_numbers.append(vvid_line_numbers[i - 1])
    return cut_line_numbers
def main():
    pattern = r'vvid=[A-Z0-9-]{36}'
    log_lines = read_log_file('app.log')
    write_reversed_log_file(log_lines, 'app_convert.log')
    reversed_log_lines = log_lines[::-1]
    print(f"All logfile lines: {len(reversed_log_lines)}\n")
    vvid_list, vvid_line_numbers = find_vvids(reversed_log_lines, pattern)
    print(f"The number of all VVIDs: {len(vvid_list)}\n")
    for line_number, vvid in zip(vvid_line_numbers, vvid_list):
        print(line_number)
        print(vvid)
    cut_line_numbers = find_cut_lines(vvid_list, vvid_line_numbers)
    print("Cut line numbers where VVID changes:")
    for cut_line in cut_line_numbers:
        print(cut_line)
if __name__ == "__main__":
    main()