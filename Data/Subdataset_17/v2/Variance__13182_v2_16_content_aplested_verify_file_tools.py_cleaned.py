import os
def file_read(file):
    print(f'Reading {file}...')
    with open(file, 'r') as f:
        block_lines = f.read()
    lines_of_file = block_lines.split('\n')
    if lines_of_file:
        del lines_of_file[0]
    if lines_of_file:
        del lines_of_file[-1]
    if lines_of_file:
        print(lines_of_file[0])
    return lines_of_file
def file_write(file, data):
    with open(file, 'w') as f:
        for each_line in data:
            joined_line = '\t'.join(each_line)
            f.write(f'{joined_line}\r')
def add_filename_prefix(path, prefix=""):
    directory, filename = os.path.split(path)
    filename = prefix + filename
    return os.path.join(directory, filename)
def lines_into_traces(lines):
    split_lines = [line.split('\t') for line in lines]
    num_of_traces = len(split_lines[0])
    traces = [[] for _ in range(num_of_traces)]
    for line in split_lines:
        for i in range(num_of_traces):
            traces[i].append(float(line[i]))
    return traces
def traces_into_lines(traces):
    lines_of_output = len(traces[0])
    lines = [[''] * len(traces) for _ in range(lines_of_output)]
    for point in range(lines_of_output):
        for i, trace in enumerate(traces):
            lines[point][i] = str(trace[point])
    return ['\t'.join(line) for line in lines]
if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    prefix = "new_"
    lines = file_read(input_file)
    traces = lines_into_traces(lines)
    new_lines = traces_into_lines(traces)
    file_write(output_file, new_lines)
    new_filename = add_filename_prefix(output_file, prefix)
    print(f'New filename: {new_filename}')