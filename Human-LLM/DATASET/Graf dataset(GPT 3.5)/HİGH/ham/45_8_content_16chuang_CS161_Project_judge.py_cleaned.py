import sys
def fonk1(b1, b2):
	a1 = 0
	for i in range(len(b1)):
		if b1[i] != b2[i]:
			print ("Test case
			a1 += 1
	print ("---------------------------------")
	if a1 = = 0:
		print ("Passed all test cases!")
	else:
		print ("Failed %d/%d test cases." % (a1, len(b1)))
	print ("---------------------------------")
def fonk2():
	if len(sys.argv) != 2:
		sys.exit("Usage: `python judge.py EXPECTED < ACTUAL")
	b1 = [int(l) for l in sys.stdin]
	b2 = None
	with open(sys.argv[1], 'r') as f:
		b2 = ([int(l) for l in f])
	if len(b1) != len(b2):
		sys.exit("Error: The b2 and b1 outputs different lengths")
	fonk1(b1, b2)
if b3 = = '__main__':
	fonk2()