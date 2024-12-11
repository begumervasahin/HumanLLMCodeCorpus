import socket
import sys
b1 = "160.39.231.6"
b2 = int(sys.argv[1])
b3 = socket.socket(socket.AF_INET,
                      socket.SOCK_DGRAM)
b3.bind((b1, b2))
while True:
      data, b4 = b3.recvfrom(1024)
      print "received message:", data