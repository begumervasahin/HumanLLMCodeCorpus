from sage.all_cmdline import *
b1 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_4 = Integer(4); _sage_const_593439483948394349 = Integer(593439483948394349); _sage_const_2000000000 = Integer(2000000000); _sage_const_29579385439865947694694684968492467204765870577p = RealNumber('29579385439865947694694684968492467204765870577.'); _sage_const_32934893483948394 = Integer(32934893483948394); _sage_const_100000000 = Integer(100000000)
b2 = _sage_const_29579385439865947694694684968492467204765870577p
b3 = GF(b2)
b4 = EllipticCurve(GF(b2),[_sage_const_32934893483948394 ,_sage_const_593439483948394349 ])
b5 = '/home/landondare/EllipticCurveProject/data.txt'
b6 = open(b5).read().splitlines()
b7 = b6[len(b6) -_sage_const_1 ].split(' ')
b8 = int(b7[_sage_const_1 ])
b9 = b4.lift_x(b8)
b10 = int(b7[_sage_const_0 ])
b11 = b10 * b9
b12 = int(b7[_sage_const_2 ])
b13 = int(b7[b1 ])
b14 = int(b7[_sage_const_4 ])
print("all values read in as the following:")
print( "\b15 = " + b7[_sage_const_0 ])
print( "\b16 = " + b7[_sage_const_1 ])
print( "\b17 = " + b7[_sage_const_2 ])
print( "\b18 = " + b7[b1 ])
print( "\b19 = " + b7[_sage_const_4 ])
b20 = _sage_const_2000000000
b21 = _sage_const_100000000
while(b10 < b20):
	if(b11[_sage_const_1 ] < b13):
		b12 = b11[_sage_const_0 ]
		b13 = b11[_sage_const_1 ]
		b14 = b10
		print("!!!!!!!found new y2")
		print(str(b11))
		print(str(b10))
		with open(b5, "a") as dataFile:
		    dataFile.write("\n\n!!!!!!!!!!!!!!!!!! NEW LOWEST FOUND " + str(b10) + " !!!!!!!!!!!!!!!!!!\n")
		    dataFile.write(str(b10) + " ")
		    dataFile.write(str(b8) + " ")
		    dataFile.write(str(b12) + " ")
		    dataFile.write(str(b13) + " ")
		    dataFile.write(str(b14))
		    dataFile.close()
	if(b10 % b21 = = _sage_const_0 ):
		with open(b5, "a") as dataFile:
		    dataFile.write("\n\n
		    dataFile.write(str(b10) + " ")
		    dataFile.write(str(b8) + " ")
		    dataFile.write(str(b12) + " ")
		    dataFile.write(str(b13) + " ")
		    dataFile.write(str(b14))
		    dataFile.close()
	b10 = b10 + _sage_const_1
	b11 = b11 + b9