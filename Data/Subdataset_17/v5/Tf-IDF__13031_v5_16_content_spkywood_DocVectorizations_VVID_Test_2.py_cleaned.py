import codecs
import re
def read_log_file(file_path):
    with codecs.open(file_path, 'r', 'utf-8', 'ignore') as file:
        return file.readlines()[::-1]
def write_log_file(file_path, lines):
    with codecs.open(file_path, 'w+', 'utf-8', 'ignore') as file:
        file.writelines(lines)
def extract_vvids(log_lines, pattern):
    vvids = []
    vvid_line_numbers = []
    for index, line in enumerate(log_lines):
        match = re.search(pattern, line)
        if match:
            vvids.append(match.group())
            vvid_line_numbers.append(index)
    return vvids, vvid_line_numbers
def identify_cut_points(vvids, vvid_line_numbers):
    cut_points = []
    for i in range(1, len(vvids)):
        if vvids[i] != vvids[i - 1]:
            cut_points.append(vvid_line_numbers[i - 1])
    return cut_points
def main():
    log_file_path = 'app.log'
    converted_log_file_path = 'app_convert.log'
    vvid_pattern = r'vvid=[A-Z0-9-]{36}'
    log_lines = read_log_file(log_file_path)
    write_log_file(converted_log_file_path, log_lines)
    total_lines = len(log_lines)
    print(f"Total number of lines in the log file: {total_lines}\n")
    vvids, vvid_line_numbers = extract_vvids(log_lines, vvid_pattern)
    num_vvids = len(vvid_line_numbers)
    print(f"Total number of VVIDs found: {num_vvids}\n")
    for line_number, vvid in zip(vvid_line_numbers, vvids):
        print(line_number)
        print(vvid)
    cut_points = identify_cut_points(vvids, vvid_line_numbers)
    print("Cut points where VVID changes:", cut_points)
if __name__ == "__main__":
    main()