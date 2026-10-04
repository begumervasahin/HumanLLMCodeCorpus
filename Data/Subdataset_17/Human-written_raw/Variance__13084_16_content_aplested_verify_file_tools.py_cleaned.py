import sys,os
def file_read (file):
	print ('Reading '+file+'....')
	f=open(file, 'r')
	block_lines = f.read()
	f.close()
	eol = os.linesep
	lines_of_file = block_lines.split('\n')
	del lines_of_file [0]
	del lines_of_file [-1]
	print lines_of_file [0]
	return lines_of_file
def file_write (file,data):
	f=open(file, "w")
	for each_line in data:
		joined_line = '\t'.join(each_line)
		f.write(joined_line)
		f.write('\r')
	f.close()
	return
def addFilenamePrefix (path, prefix=""):
    directory, filename = os.path.split(path)
    filename = prefix + filename
    return os.path.join(directory,filename)
def lines_into_traces (lines):
	split_lines=[]
	for line in lines:
		values=line.split('\t')
		split_lines.append(values)
	traces = []
	num_of_traces = len(split_lines[0])
	for i in range(num_of_traces):
		traces.append([])
	for line in split_lines:
		for i in range (num_of_traces):
			traces[i].append (float(line[i]))
	return traces
def traces_into_lines (traces):
	lines_of_output=len(traces[0])
	lines = []
	for i in range(lines_of_output):
		lines.append([])
	for point in range(0,lines_of_output):
		for trace in traces:
			lines[point].append(str(trace[point]))
	return lines