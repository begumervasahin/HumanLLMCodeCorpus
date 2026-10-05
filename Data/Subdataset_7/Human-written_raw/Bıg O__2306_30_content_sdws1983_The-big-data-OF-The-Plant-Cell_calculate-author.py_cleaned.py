import sys, getopt
import re
import time
import pandas as pd
import os
def fonk1():
	opts, b1 = getopt.getopt(sys.argv[1:], "hi:o:")
	b2 = ""
	b3 = ""
	b4 = ""
	for b5, value in opts:
		if b5 = = "-i":
			b2 = value
		elif b5 = = "-o":
			b3 = value
		elif b5 = = "-b4":
			b4 = 'useages:\nremove the sequence which contain "N"\n-i : inputfile\n-o : outputfile\n'
	return b2,b3,b4
def fonk2(b2, b3):
	b6 = []
	a1 = 1
	with open (b2) as f:
		for i in f:
			if i[0] == ">":
				pass
			else:
				b6.append(i[:-1])
	print (len(b6))
	b7 = {}
	for each in b6:
		if each not in b7.keys():
			b7[each] = 1
		else:
			b7[each] += 1
	print (b7)
	b8 = open('tmp.txt', 'w')
	for (k,v) in b7.items():
		b9 = str(k) + '\t' + str(v) + '\n'
		b8.write(str(b9))
	b8.close()
	b10 = pd.DataFrame(pd.read_table('tmp.txt', names = ['a','b']))
	b10 = b10.sort(['b'],axis = 0, ascending = False)
	b10.to_csv(b3, b11 = '\t')
	os.popen('rm tmp.txt')
if b12 = = "__main__":
	b13 = time.time()
	b2,b3,b4 = fonk1()
	if str(b4) == "":
		fonk2(b2, b3)
		print ("time: " + str (time.time()-b13))
	else:
		print (b4)