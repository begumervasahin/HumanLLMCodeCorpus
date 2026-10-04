import os
def file_read(file_path):
    print(f'Reading {file_path}...')
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n')
    if lines:
        lines = lines[1:]
    if lines:
        lines = lines[:-1]
    if lines:
        print(lines[0])
    return lines
def file_write(file_path, data):
    with open(file_path, 'w') as file:
        for line in data:
            file.write(f"{line}\r")
def add_filename_prefix(path, prefix=""):
    directory, filename = os.path.split(path)
    new_filename = prefix + filename
    return os.path.join(directory, new_filename)
def lines_into_traces(lines):
    split_lines = [line.split('\t') for line in lines]
    num_of_traces = len(split_lines[0])
    traces = [[] for _ in range(num_of_traces)]
    for split_line in split_lines:
        for i in range(num_of_traces):
            traces[i].append(float(split_line[i]))
    return traces
def traces_into_lines(traces):
    lines_of_output = len(traces[0])
    lines = ['\t'.join(map(str, trace_point)) for trace_point in zip(*traces)]
    return lines
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