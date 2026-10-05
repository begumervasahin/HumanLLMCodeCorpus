import b5;
import sys;
def fonk1(b3):
   for i in range(1,len(b3)):
        b1 = b3[i]
        b2 = i
        while b2>0 and b3[b2-1]>b1:
           b3[b2]=b3[b2-1]
           b2 = b2-1
        b3[b2]=b1;
if len(sys.argv)!=3:
	print "Incorrect Format!! Enter [filename].py [input file name] [Output file name]"
	sys.exit();
with open(sys.argv[1],'r') as f:
	b3 = [int(x) for x in f.read().split(',')];
b4 = b5.b5();
fonk1(b3);
print "Running b5 = ",b5.b5()-b4," secs";
b6 = open(sys.argv[2],'w');
print >>b6, b3;
b6.close();