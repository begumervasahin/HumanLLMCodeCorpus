import socket
import sys
import json
import cPickle as pickle
b1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
b1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
b1.bind(("", int(sys.argv[1])))
b2 = b1.recvfrom(4096)
b3 = pickle.loads(b2[0])
print "b4 = " + str(b2[1])
print "b3 b5 = " + str(b3)