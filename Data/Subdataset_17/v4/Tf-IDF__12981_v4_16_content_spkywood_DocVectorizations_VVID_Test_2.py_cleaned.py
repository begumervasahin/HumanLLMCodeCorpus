import codecs
import re
vvid_pattern = r'vvid=[A-Z0-9-]{36}'
with codecs.open('app.log', 'r', 'utf-8', 'ignore') as log_file:
    log_lines = log_file.readlines()[::-1]
with codecs.open('app_convert.log', 'w+', 'utf-8', 'ignore') as result_log:
    result_log.writelines(log_lines)
total_lines = len(log_lines)
print("Total number of lines in the log file:", total_lines, '\n')
vvid_list = []
vvid_lines = []
for index, line in enumerate(log_lines):
    match = re.search(vvid_pattern, line)
    if match:
        vvid_list.append(match.group())
        vvid_lines.append(index)
num_vvids = len(vvid_lines)
print("Total number of VVIDs found:", num_vvids, '\n')
for line_number, vvid in zip(vvid_lines, vvid_list):
    print(line_number)
    print(vvid)
cut_line_numbers = []
for i in range(1, num_vvids):
    if vvid_list[i] != vvid_list[i - 1]:
        cut_line_numbers.append(vvid_lines[i - 1])
        print(cut_line_numbers)