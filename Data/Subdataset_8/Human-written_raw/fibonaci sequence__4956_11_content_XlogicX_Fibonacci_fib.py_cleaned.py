import re
import math
import time
import sys
def errchk(hwmny,int1,int2,int3,int4,errcnt):
	expression = re.compile(r"^[^6]{1,3}", re.I | re.S)
	if expression.match(str(int3)):
		return
	else:
		if (hwmny > 12):
			return
		zints.err()
	return None
def nofloats():
	return math.floor(zints.int3)
class zeroints:
	int3=int4 = 0
	errcnt = 0
	def err(self):
		print "Errors"
		return
hwmny =15
int1 =int2 =1
zints = zeroints()
print "0\n1\n1"
def loop(hwmny,int1,int2,int3,int4,errcnt):
	while((zints.int4<hwmny)or not(zints.int4>0)and not(zints.int4==0)):
		zints.int3 =int1+ int2
		int1 =int2
		string = 'The Values Are'
		int2= zints.int3
		errchk(hwmny,int1,int2,zints.int3,zints.int4,zints.errcnt)
		print zints.int3
		zints.int4= zints.int4+1
		loop(hwmny,int1,int2,zints.int3,zints.int4,zints.errcnt)
		continue
loop(hwmny,int1,int2,zints.int3,zints.int4,zints.errcnt)