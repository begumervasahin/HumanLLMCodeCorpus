import sys
import os
def file_read(file_path):
    print('Reading ' + file_path + '...')
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    del lines[0]
    del lines[-1]
    print(lines[0])
    return lines
def file_write(file_path, data):
    with open(file_path, "w") as file:
        for line in data:
            joined_line = '\t'.join(line)
            file.write(joined_line + '\n')
def addFilenamePrefix(path, prefix=""):
    directory, filename = os.path.split(path)
    filename = prefix + filename
    return os.path.join(directory, filename)
def lines_into_traces(lines):
    split_lines = [line.split('\t') for line in lines]
    traces = [[] for _ in range(len(split_lines[0]))]
    for line in split_lines:
        for i, value in enumerate(line):
            traces[i].append(float(value))
    return traces
def traces_into_lines(traces):
    lines_of_output = len(traces[0])
    lines = [[] for _ in range(lines_of_output)]
    for point in range(lines_of_output):
        for trace in traces:
            lines[point].append(str(trace[point]))
    return lines