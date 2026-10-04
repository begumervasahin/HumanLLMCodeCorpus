import codecs
import re
pattern = r'vvid=[A-Z0-9-]{36}'
with codecs.open('app.log', 'r', 'utf-8', 'ignore') as log_file:
    log_lines = log_file.readlines()
reversed_log_lines = log_lines[::-1]
with codecs.open('app_convert.log', 'w+', 'utf-8', 'ignore') as result_log:
    result_log.writelines(reversed_log_lines)
total_lines = len(reversed_log_lines)
print("All logfile lines:", total_lines, '\n')
vvid_list = []
vvid_line_numbers = []
for i, line in enumerate(reversed_log_lines):
    match = re.search(pattern, line)
    if match:
        vvid_list.append(match.group())
        vvid_line_numbers.append(i)
total_vvids = len(vvid_line_numbers)
print("The number of all VVIDs:", total_vvids, '\n')
for line_number, vvid in zip(vvid_line_numbers, vvid_list):
    print(line_number)
    print(vvid)
cut_line_numbers = []
for i in range(1, total_vvids):
    if vvid_list[i] != vvid_list[i - 1]:
        cut_line_numbers.append(vvid_line_numbers[i - 1])
        print(cut_line_numbers)