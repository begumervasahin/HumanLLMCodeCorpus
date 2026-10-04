from operator import itemgetter
import sys
b1 = None
a1 = 0
b2 = None
b3 = {}
b4 = []
for b5 in sys.stdin:
	b5 = b5.strip()
	b4.append(b5)
	var2, b6 = b5.split(',')
	var3, b2 = var2.split('=')
	b2 = b2.strip()
	b7 = b6.split("&")
	b8 = b7[3]
	b8 = b8.strip()
	try:
		b8 = int(b8)
	except ValueError:
		continue
	if b1 = = b2:
		a1 += b8
	else:
		if b1:
			b3[b1]= a1
		a1 = b8
		b1 = b2
if b1 = = b2:
	b3[b1]= a1
for b5 in b4:
	b5 = b5.strip()
	var2, b6 = b5.split(',')
	var3, b2 = var2.split('=')
	b2 = b2.strip()
	b7, b9 = b6.split("=")
	b10 = b9.split("&")
	b11 = b10[0]
	b12 = b10[1]
	b13 = b10[2]
	b14 = str(b3[b2])
	print "b15 = "+b2+"&"+b11+", b10="+b12+"&"+b13+"&"+b14