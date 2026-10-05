import sys
import socket
import select
from time import time, sleep
from collections import defaultdict
import cPickle as pickle
import datetime
import copy
a1 = 1
b1 = a1
a2 = 4096
b2 = {}
b3 = {}
b4 = {}
b5 = {}
b6 = (0,0)
b7 = time()
b8 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
b8.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
b8.setblocking(0)
b9 = socket.gethostbyname(socket.gethostname())
if b9[:3] == '127':
	b9 = '127.0.0.1'
b10 = float("inf")
def fonk1(b22):
	b8.sendto('DOWN', b22)
def fonk2(b22, weight):
	b2[b22] = float(weight)
	b3[b22]= time()
	b4[b22] = 1
	b5[b6][b22] = [b22, float(weight)]
	b5[b22] = {}
	b5[b22][b22] = [b22, 0]
def fonk3(b22, vector):
	b5[b22] = vector
	b5[b6][b22] = [b22, b5[b22][b6][1]]
	b2[b22] = float(b5[b22][b6][1])
def fonk4():
	if a1:
		print b5[b6]
		print b4
	for b18, vector in b5.iteritems():
		if b18 is not b6:
			if b1:
				print b18
				print b4[b18]
			if b4[b18]==1:
				if b1:
					print "broadcast: sending to b22 " + str(b18)
				b11 = copy.deepcopy(b5[b6])
				for b12, b13 in b5[b6].iteritems():
					if b13[0] == b18 and b12 != b18:
						b11[b12][1] = b10
				if a1:
					print "poisoned b37 to neighbot %s : %s" % (b18, b11)
					print "actual b5[b6] " + str(b5[b6])
				b8.sendto(pickle.dumps(b11), b18)
	b7 = time()
def fonk5():
	print str(datetime.datetime.now()) + ", Current Distance Vector is:"
	for b12, b13 in b5[b6].iteritems():
		if b12 is not b6:
			if a1:
				print "b12 = " + str(b12)
				print "b13 = " + str(b13)
			print "b14 = %s:%d, Cost = %.1f, Link = (%s:%d)" % (b12[0], b12[1], float(b13[1]), b13[0][0], b13[0][1])
def fonk6():
	for b12,b15 in b5[b6].iteritems():
		b13 = b15[0]
		try:
			b5[b6][b12][1] = b5[b6][b13][1] + b5[b13][b12][1]
		except:
			b5[b6][b12][1] = b10
	b13 = ("UNREACHABLE", 0)
	a3 = 0
	for b12, b15 in b5[b6].iteritems():
		if b12 is not b6:
			if a1:
				print "----updating distance to b12 : " + str (b12)
				print "----old b15 = " + str(b15)
			try:
				if a1:
					print "^^^^^^^^^^^^^^ TRYING INITIAL CLEANUP"
					print "b12 = " + str(b12)
					print "b15[0] = " + str(b12)
					print "b5[b6][b12]" + str(b5[b6][b12])
					print "b5[b15[0]] = " + str(b5[b15[0]])
					print "b5[b15[0]][b6][1] = " + str(b5[b15[0]][b6][1])
					print "b5[b15[0]][b12][1] = " +  str(b5[b15[0]][b12][1])
					if b5[b15[0]][b6][1] + b5[b15[0]][b12][1] > b5[b6][b12][1]:
						b5[b6][b12] = [b12, b5[b15[0]][b6][1] + b5[b15[0]][b12][1]]
			except:
				pass
			b16 = b5[b6][b12][1]
			b17 = b10
			for b18, links in b5.iteritems():
				if b4[b18] and b18 != b6:
					if a1:
						print "-b18 is not b6, b18 = " + str(b18)
						print "-b6: " + str(b6)
					try:
						b19 = b5[b18][b12][1]
					except:
						b19 = b10
					if a1:
						print "-b5[b6] = " + str(b5[b6])
						print "-b5[b6][b18] = " + str(b5[b6][b18])
						print "-b5[b6][b18][1] = " + str(b5[b6][b18][1])
						print "-b5[b18][b12][1] = " + str(b19)
						print "-b16 = " + str(b16)
					if b18 != b12:
						b20 = b5[b6][b18][1]
					else:
						b20 = b2[b18]
					if b20 + b19 < b17:
						if a1:
							print "-route discovered, b5[%s][%s] + b5[%s][%s] = %s" % (b6, b18, b18, b12, b5[b6][b18][1]+ b19)
						b17 = b20 + b19
						b13 = b18
			if b16 != b17:
				if a1:
					print "====New route superior; CHANGE RECORDED"
					print "====b16 = " + str(b16)
					print "====b17 = " +str(b17)
					print "====b21 = " + str(b12)
					print "====via b13" + str(b13)
				a3 = 1
				b5[b6][b12] = [b13, b17]
			if a1:
				print "===================================================="
	return a3
def fonk7(client_input):
	b22 = client_input
	if b22[0] == 'localhost' or b22[0][:3] == '127':
		b22 = (b9, client_input[1])
	b4[b22] = 0
	b2[b22] = b5[b6][b22][1]
	'''
	b5[b6][b22] = [("DOWN", 0), b10]
	b5[b22][b6] = [("DOWN", 0), b10]
	'''
	b5[b6][b22][1] = b10
	try:
		b5[b22][b6][1] = b10
	except:
		if a1:
			print "dont have the DV for " + str(b22) + " yet."
	if b1:
		print b5[b6]
	for b12, b13 in b5[b6].iteritems():
		if a1:
			print "****killing intermediary... b12 = " + str(b12)
			print "b13[1] = " + str(b13[1])
		if b13[1] == b22:
			if a1:
				print "this b13 needs to be recalculated..."
			b5[b6][b12] = [("ALSO DOWN", 0), b10]
	fonk6()
	fonk1(b22)
	for b27 in range (5):
		fonk4()
		sleep(0.2)
def fonk8(client_input):
	b22 = client_input
	if b22[0] == 'localhost' or b22[0][:3] == '127':
		b22 = (b9, client_input[1])
	b4[b22] = 1
	b5[b6][b22] = [b22, b2[b22]]
	b5[b22][b6] = [b6, b2[b22]]
	fonk6()
	for b27 in range (5):
		fonk4()
		sleep(0.2)
def fonk9(packet):
	if packet[1][0][:3] == '127':
		b23 = (b9, packet[1][1])
	else:
		b23 = packet[1]
	if packet[0] == 'DOWN':
		b2[b23] = b5[b6][b23][1]
		b5[b6][b23][1] = b10
		try:
			b5[b23][b6][1] = b10
		except:
			pass
		b4[b23] = 0
		fonk6()
		fonk4()
	else:
		a3 = 0
		b24 = pickle.loads(packet[0])
		b3[b23] = time()
		if b23 not in b5.keys():
			fonk3(b23, b24)
			b4[b23] = 1
			for b12, b13 in b5[b23].iteritems():
				if b12 not in b5[b6].keys():
					b5[b6][b12] = [("UNKNOWN", 0), b10]
					a3 = 1
			b2[b23] = b5[b23][b6][1]
			b5[b6][b23] = [b23,  b2[b23]]
			if fonk6():
				a3 = 1
		else:
			b5[b23] = b24
			for b12, b13 in b5[b23].iteritems():
				if b12 not in b5[b6].keys():
					b5[b6][b12] = [("UNKNOWN", 0), b10]
			if not b4[b23]:
				b5[b6][b23] = [b23, b2[b23]]
			b4[b23] = 1
			if fonk6():
				a3 = 1
		if a3:
			fonk4()
		else:
			if a1:
				print "no changes to DV in this run"
def fonk10():
	for b18, vector in b5.iteritems():
		if b18 != b6:
			fonk1(b18)
	sys.exit()
def fonk11(b37):
	b25 = b37.split()
	if b25[0].upper() == 'SHOWRT':
		fonk5()
	elif b25[0].upper() == 'LINKDOWN' and len(b25) == 3:
		fonk7((b25[1], int(b25[2])))
	elif b25[0].upper() == 'LINKUP' and len(b25) == 3:
		fonk8((b25[1], int(b25[2])))
	elif b25[0].upper() == 'BROADCAST':
		fonk4()
	elif b25[0].upper() == 'CLOSE':
		fonk10()
	else:
		print "Syntax error. Refer to assignment for correct syntax."
		pass
def fonk12(argv):
	global b6;
	b26 = len(argv)
	if b26%3:
		print "Syntax error - b26 of argv is not divisible by 3"
		return 0
	b27 = 0;
	while b27 < b26-2:
		if argv[b27] == 'localhost' or argv[b27][:3] == '127':
			b28 = b9
			'''IMPORTANT
			ANYTHING LOCAL (127.x.x.x, localhost) is converted to actual IP address to ensure consistency
			'''
		else:
			b28 = argv[b27]
		fonk2((b28, int(argv[b27+1])), argv[b27+2])
		b27 = b27+3
	return 1
if b29 = = "__main__":
	b30 = int(sys.argv[1])
	b31 = int(sys.argv[2])
	b8.bind(("", b30))
	b6 = (b9, b30)
	b5[b6] = {}
	b5[b6][b6] = [(b9, b30), 0]
	b4[b6] = 1
	if a1:
		print "my b32 = %d, my timeout = %d, my address = %s" % (b30, b31, b9)
	if fonk12(sys.argv[3:]) != 1:
		print "Syntax error. b33 = localport timeout [ipaddress1 port1 weight1 ...]"
	fonk4()
	b7 = time()
	try:
		while True:
			b34 = [sys.stdin, b8]
			b35 = select.select(b34, [], [], 0.1)[0]
			if not b35:
				for b18, vector in b5.iteritems():
					if b4[b18] and b18 is not b6:
						if time()- b3[b18] > b31*3:
							if a1:
								print "
							fonk7(b18)
				if time() - b7 > b31:
					if a1:
						print "I am starting to broadcast to the neighbors..."
					fonk4()
					b7 = time()
			else:
				for b36 in b35:
					if b36 = = b8:
						if a1:
							print "see what the packet is... could be nothing"
						fonk9(b36.recvfrom(a2))
					elif b36 = = sys.stdin:
						b37 = sys.stdin.readline()
						fonk11(b37)
					else:
						print "DONT KNOW WHY IM HERE"
						pass
	except KeyboardInterrupt:
		fonk10()
		sys.exit()