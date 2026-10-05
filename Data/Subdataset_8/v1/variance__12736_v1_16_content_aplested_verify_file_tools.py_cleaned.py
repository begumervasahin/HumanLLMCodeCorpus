import os
def file_read(file):
    print('Reading ' + file + '....')
    with open(file, 'r') as f:
        block_lines = f.readlines()
    lines_of_file = [line.strip() for line in block_lines[1:-1]]
    print(lines_of_file[0])
    return lines_of_file
def file_write(file, data):
    with open(file, "w") as f:
        for each_line in data:
            joined_line = '\t'.join(each_line)
            f.write(joined_line + '\n')
def addFilenamePrefix(path, prefix=""):
    directory, filename = os.path.split(path)
    filename = prefix + filename
    return os.path.join(directory, filename)
def lines_into_traces(lines):
    split_lines = [line.split('\t') for line in lines]
    traces = [[] for _ in range(len(split_lines[0]))]
    for line in split_lines:
        for i in range(len(traces)):
            traces[i].append(float(line[i]))
    return traces
def traces_into_lines(traces):
    lines_of_output = len(traces[0])
    lines = [[] for _ in range(lines_of_output)]
    for point in range(lines_of_output):
        for trace in traces:
            lines[point].append(str(trace[point]))
    return lines
if __name__ == "__main__":
    lines = file_read("example.txt")
    traces = lines_into_traces(lines)
    for i in range(len(traces)):
        traces[i] = [val + 1 for val in traces[i]]
    modified_lines = traces_into_lines(traces)
    file_write("modified_example.txt", modified_lines)