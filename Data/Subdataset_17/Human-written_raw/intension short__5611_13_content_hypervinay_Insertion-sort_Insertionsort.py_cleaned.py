import time;
import sys;
def insertionSortList(inputList):
   for i in range(1,len(inputList)):
        item = inputList[i]
        pointer = i
        while pointer>0 and inputList[pointer-1]>item:
           inputList[pointer]=inputList[pointer-1]
           pointer = pointer-1
        inputList[pointer]=item;
if len(sys.argv)!=3:
	print "Incorrect Format!! Enter [filename].py [input file name] [Output file name]"
	sys.exit();
with open(sys.argv[1],'r') as f:
	inputList = [int(x) for x in f.read().split(',')];
startTime = time.time();
insertionSortList(inputList);
print "Running time = ",time.time()-startTime," secs";
fout = open(sys.argv[2],'w');
print >>fout, inputList;
fout.close();