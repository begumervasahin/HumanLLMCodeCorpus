import os
def read_lines(file_path):
    print('Reading file:', file_path)
    with open(file_path, 'r') as file:
        lines = file.readlines()
    stripped_lines = [line.strip() for line in lines[1:-1]]
    print("First line of content:", stripped_lines[0])
    return stripped_lines
def write_lines(file_path, lines):
    with open(file_path, "w") as file:
        for line in lines:
            joined_line = '\t'.join(line)
            file.write(joined_line + '\n')
def add_prefix_to_filename(file_path, prefix=""):
    directory, filename = os.path.split(file_path)
    prefixed_filename = prefix + filename
    return os.path.join(directory, prefixed_filename)
def lines_to_traces(lines):
    split_lines = [line.split('\t') for line in lines]
    num_of_traces = len(split_lines[0])
    traces = [[] for _ in range(num_of_traces)]
    for line in split_lines:
        for i in range(num_of_traces):
            traces[i].append(float(line[i]))
    return traces
def traces_to_lines(traces):
    num_of_points = len(traces[0])
    lines = [[] for _ in range(num_of_points)]
    for point in range(num_of_points):
        for trace in traces:
            lines[point].append(str(trace[point]))
    return lines
if __name__ == "__main__":
    lines = read_lines("example.txt")
    traces = lines_to_traces(lines)
    for trace in traces:
        for i in range(len(trace)):
            trace[i] += 1
    modified_lines = traces_to_lines(traces)
    write_lines("modified_example.txt", modified_lines)