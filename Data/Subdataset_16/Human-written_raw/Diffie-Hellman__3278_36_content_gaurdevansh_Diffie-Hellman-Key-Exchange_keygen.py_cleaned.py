import random
a1 = 26994308385016394749558484505346578147056894665639
a2 = 2
def fonk1(filename):
	b1 = str(random.randint(1000,10000))
	with open(filename,'w') as outfile:
		outfile.write(b1)
def fonk2(privatefilename,publicfilename):
	with open(privatefilename,'r') as infile:
		b2 = infile.read()
	b2 = int(b2)
	b3 = (a2**b2)%a1
	b3 = str(b3)
	with open(publicfilename,'w') as outfile:
		outfile.write(b3)
def fonk3(privatefile,publicfile):
	with open(privatefile,'r') as infile:
		b4 = int(infile.read())
	with open(publicfile,'r') as infile:
		b5 = int(infile.read())
	b6 = (b5**b4)%a1
	return b6