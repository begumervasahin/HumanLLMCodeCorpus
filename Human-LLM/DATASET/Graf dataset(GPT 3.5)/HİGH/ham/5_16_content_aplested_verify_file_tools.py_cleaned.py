import sys,os
def file_read (file):
	print ('Reading '+file+'....')
	b1 = open(file, 'r')
	b2 = b1.read()
	b1.close()
	b3 = os.linesep
	b4 = b2.split('\n')
	del b4 [0]
	del b4 [-1]
	print b4 [0]
	return b4
def file_write (file,data):
	b1 = open(file, "w")
	for each_line in data:
		b5 = '\t'.join(each_line)
		b1.write(b5)
		b1.write('\r')
	b1.close()
	return
def addFilenamePrefix (path, b6 = ""):
    directory, b7 = os.path.split(path)
    b7 = b6 + b7
    return os.path.join(directory,b7)
def lines_into_traces (b13):
	b8 = []
	for line in b13:
		b9 = line.split('\t')
		b8.append(b9)
	b10 = []
	b11 = len(b8[0])
	for i in range(b11):
		b10.append([])
	for line in b8:
		for i in range (b11):
			b10[i].append (float(line[i]))
	return b10
def traces_into_lines (b10):
	b12 = len(b10[0])
	b13 = []
	for i in range(b12):
		b13.append([])
	for point in range(0,b12):
		for trace in b10:
			b13[point].append(str(trace[point]))
	return b13