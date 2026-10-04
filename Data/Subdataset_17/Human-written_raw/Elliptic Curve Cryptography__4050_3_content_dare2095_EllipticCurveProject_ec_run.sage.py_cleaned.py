from sage.all_cmdline import *
_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_4 = Integer(4); _sage_const_593439483948394349 = Integer(593439483948394349); _sage_const_2000000000 = Integer(2000000000); _sage_const_29579385439865947694694684968492467204765870577p = RealNumber('29579385439865947694694684968492467204765870577.'); _sage_const_32934893483948394 = Integer(32934893483948394); _sage_const_100000000 = Integer(100000000)
p = _sage_const_29579385439865947694694684968492467204765870577p
field = GF(p)
curve = EllipticCurve(GF(p),[_sage_const_32934893483948394 ,_sage_const_593439483948394349 ])
path = '/home/landondare/EllipticCurveProject/data.txt'
lines = open(path).read().splitlines()
inputValues = lines[len(lines) -_sage_const_1 ].split(' ')
x1 = int(inputValues[_sage_const_1 ])
startPoint = curve.lift_x(x1)
e = int(inputValues[_sage_const_0 ])
testPoint = e * startPoint
lowest_x2 = int(inputValues[_sage_const_2 ])
lowest_y2 = int(inputValues[_sage_const_3 ])
lowest_e = int(inputValues[_sage_const_4 ])
print("all values read in as the following:")
print( "\te = " + inputValues[_sage_const_0 ])
print( "\tx1 = " + inputValues[_sage_const_1 ])
print( "\tlowest_x2 = " + inputValues[_sage_const_2 ])
print( "\tlowest_y2 = " + inputValues[_sage_const_3 ])
print( "\tlowest_e = " + inputValues[_sage_const_4 ])
runBlock = _sage_const_2000000000
writeBlock = _sage_const_100000000
while(e < runBlock):
	if(testPoint[_sage_const_1 ] < lowest_y2):
		lowest_x2 = testPoint[_sage_const_0 ]
		lowest_y2 = testPoint[_sage_const_1 ]
		lowest_e = e
		print("!!!!!!!found new y2")
		print(str(testPoint))
		print(str(e))
		with open(path, "a") as dataFile:
		    dataFile.write("\n\n!!!!!!!!!!!!!!!!!! NEW LOWEST FOUND " + str(e) + " !!!!!!!!!!!!!!!!!!\n")
		    dataFile.write(str(e) + " ")
		    dataFile.write(str(x1) + " ")
		    dataFile.write(str(lowest_x2) + " ")
		    dataFile.write(str(lowest_y2) + " ")
		    dataFile.write(str(lowest_e))
		    dataFile.close()
	if(e % writeBlock == _sage_const_0 ):
		with open(path, "a") as dataFile:
		    dataFile.write("\n\n
		    dataFile.write(str(e) + " ")
		    dataFile.write(str(x1) + " ")
		    dataFile.write(str(lowest_x2) + " ")
		    dataFile.write(str(lowest_y2) + " ")
		    dataFile.write(str(lowest_e))
		    dataFile.close()
	e = e + _sage_const_1
	testPoint = testPoint + startPoint