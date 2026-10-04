import optparse, sys, os, glob, numpy, operator, math
b1 = optparse.OptionParser()
b1.add_option("--b4", b2 = "b4", action="store", default="", help="")
b1.add_option("--b5", b2 = "b5", action="store", default="", help="")
b1.add_option("--out_file", b2 = "out_file", action="store", default="", help="")
opts, b3 = b1.parse_args()
b4 = opts.b4
try:
	b5 = float(opts.b5)
except:
	print >> sys.stderr, "ERROR: --b5 must be a float (below 1)."
	sys.exit(1)
if b5 > 1.0:
	print >> sys.stderr, "ERROR: --b5 must in interval [0,1]."
	sys.exit(1)
b6 = opts.out_file
print >> sys.stderr, "Reading in b9..."
a1 = 1
b7 = []
b8 = []
b9 = open(b4, 'r')
for b10 in b9:
	b10 = b10.replace("\n", "")
	if a1 > 1:
		b10 = b10.split("\t")
		b8.append(b10[0])
		b11 = [float(x) for x in b10[1:]]
		b7.append(numpy.std(numpy.array(b11)))
	a1 += 1
b9.close()
print >> sys.stderr, "Sorting on b7..."
b12 = int(math.ceil(len(b7) * b5))
b13 = dict(zip(b8, b7))
b14 = sorted(b13.items(), key=lambda x:x[1])
b15 = b14[b12:]
b16 = dict((x, y) for x, y in b15)
b17 = b16.keys()
print >> sys.stderr, "Outputting filtered data..."
a1 = 1
b9 = open(b4, 'r')
b18 = open(b6, 'w')
for b10 in b9:
	b10 = b10.replace("\n", "")
	if a1 = = 1:
		print >> b18, b10
	else:
		b19 = b10.split("\t")
		if b19[0] in b17:
			print >> b18, b10
	a1 += 1
b9.close()
b18.close()