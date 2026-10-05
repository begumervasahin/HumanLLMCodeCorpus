import socket
print("")
print ("***********************")
print ("*    Diffie Hellman   *")
print ("*     Key Exchange    *")
print ("***********************")
b1 = input("Input prime number: ")
b2 = input("Input base number : ")
b3 = input("Enter Alice Secret here:")
b4 = input("Enter Bob Secret here:")
print "-----------------------------------------"
print "Publicly Shared Variables:"
print "    Publicly Shared b1: " , b1
print "    Publicly Shared b2:  " , b2
print "-----------------------------------------"
b5 = b2**b3 % b1
print "\n  Alice Sends Over Public Chanel: " , b5
b6 = (b2 ** b4) % b1
print  "\n  Bob Sends Over Public Chanel: " ,b6
print "------------------------------------------"
print "Privately Calculated Shared Secret:"
b7 = b6 ** b3 % b1
print "    Alice Shared Secret: ", b7
b8 = (b5**b4) % b1
print "    Bob Shared Secret: ", b8
print "------------------------------------------"
if b8 = = b7 :
    print "Connection established"
print "******************************************"
b9 = socket.socket()
b10 = socket.gethostname()
a1 = 51125
b9.bind((b10, a1))
b9.listen(5)
while True:
   c, b11 = b9.accept()
   print 'Got connection from', b11
   c.send(str(b7)+str(b8))
   c.close()
print  "    Alice Shared Secret: ", b7