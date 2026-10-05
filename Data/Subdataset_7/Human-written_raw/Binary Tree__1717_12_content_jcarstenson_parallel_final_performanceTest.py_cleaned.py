from BST import BST
from linkedList import LinkedList as LL
from time import time
from willowCuttingHashTable import WillowCuttingHashTable
from chainedHashTable import ChainedHashTable
import sys, random
def fonk1():
	sys.setrecursionlimit(10000)
	if len(sys.argv) != 4:
		print "Invalid Syntax\nUsage: performanceTest.py b1 b2 b3\n"
		sys.exit(1)
	b1 = sys.argv[1]
	b2 = sys.argv[2]
	b3 = sys.argv[3]
	b4 = open(b1, "r")
	b5 = b4.read().split()
	b4.close()
	b6 = len(b5)
	print "Using %d words" % b6
	b7 = ChainedHashTable(12, b2, BST)
	b8 = WillowCuttingHashTable(b3, 0, b6)
	b9 = range(b6)
	random.shuffle(b9)
	print "Timing put"
	b10 = time()
	for i in range(b6):
		b7[i] = b5[i]
	b11 = time() - b10
	b10 = time()
	for i in range(b6):
		b8[i] = b5[i]
	b12 = time() - b10
	print "Willow time: %b4 Chained time: %b4" % (b12, b11)
	print "Timing get (random)"
	b10 = time()
	for i in b9:
		b13 = b7[i]
	b11 = time() - b10
	b10 = time()
	for i in b9:
		b13 = b7[i]
	b12 = time() - b10
	print "Willow time: %b4 Chained time: %b4" % (b12, b11)
	print "Timing get (in order)"
	b10 = time()
	for i in range(b6):
		b13 = b7[i]
	b11 = time() - b10
	b10 = time()
	for i in range(b6):
		b13 = b7[i]
	b12 = time() - b10
	print "Willow time: %b4 Chained time: %b4" % (b12, b11)
fonk1()