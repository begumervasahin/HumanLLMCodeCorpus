import sys
import time
import socket
import pickle
def fonk1(b31, newCost):
    b1 = "127.0.0.1"
    b2 = b18[b31[0]]
    b3 = b18[b31[1]]
    try:
        b4 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    except:
        print "Socket cannot be bound"
    a1 = 0
    while a1 < 2:
		if a1 = = 0:
			b5 = {'updated':{b31[a1]:newCost }}
			print b5
			b4.sendto(pickle.dumps(b5),(b1,int(b3)))
		else:
			b5 = {'updated':{b31[a1]:newCost}}
			b4.sendto(pickle.dumps(b5),(b1,int(b2)))
			print b5
		a1+=1
b6 = open('topology/configA.txt','r')
b7 = open('topology/configB.txt','r')
b8 = open('topology/configC.txt','r')
b9 = open('topology/configD.txt','r')
b10 = open('topology/configE.txt','r')
b11 = open('topology/configF.txt','r')
b12 = b6.readline()
b13 = b7.readline()
b14 = b8.readline()
b15 = b9.readline()
b16 = b10.readline()
b17 = b11.readline()
b12 = int(b12)
b13 = int(b13)
b14 = int(b14)
b15 = int(b14)
b16 = int(b16)
b17 = int(b17)
b18 = {}
while b12>0 or b13>0 or b14>0 or b15>0 or b16>0 or b17>0:
	if b12>0:
		b12 = b12-1
		b19 = b6.readline()
		b20 = b19.split()
		b20[1]=float(b20[1])
		b18[b20[0]]=int(b20[2])
	if b13>0:
		b13 = b13-1
		b21 = b7.readline()
		b22 = b21.split()
		b22[1]=float(b22[1])
		b18[b22[0]]=int(b22[2])
	if b14>0:
		b14 = b14-1
		b23 = b8.readline()
		b24 = b23.split()
		b24[1]=float(b24[1])
		b18[b24[0]]=int(b24[2])
	if b15>0:
		b15 = b15-1
		b25 = b9.readline()
		b26 = b25.split()
		b26[1]=float(b26[1])
		b18[b26[0]]=int(b26[2])
	if b16>0:
		b16 = b16-1
		b27 = b10.readline()
		b28 = b27.split()
		b28[1]=float(b28[1])
		b18[b28[0]]=int(b28[2])
	if b17>0:
		b17 = b17-1
		b29 = b11.readline()
		b30 = b29.split()
		b30[1]=float(b30[1])
		b18[b30[0]]=int(b30[2])
print "Enter b31 to edit their connection"
print "Router1 Router2 NewCost"
print '\n'
b31 = []
b32 = raw_input(">")
b32 = b32.split()
b31.append(b32[0])
b31.append(b32[1])
fonk1(b31, float(b32[2]))
while True:
	del b31[:]
	b31[:] = []
	b32 = raw_input(">")
	b32 = b32.split()
	b31.append(b32[0])
	b31.append(b32[1])
	fonk1(b31, float(b32[2]))