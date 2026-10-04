import random
import base64
import hashlib
import sys
a1 = 9
a2 = 1001
b1 = random.randint(5, 10)
b2 = random.randint(10,20)
b3 = (a1**b1) % a2
b4 = (a1**b2) % a2
print 'a1: ',a1,' (b1 shared value), a2: ',a2, ' (b1 prime number)'
print '\nAlice calculates:'
print 'b1 (Alice random): ',b1
print 'Alice value (b3): ',b3,' (a1^b1) mod a2'
print '\nBob calculates:'
print 'b2 (Bob random): ',b2
print 'Bob value (b4): ',b4,' (a1^b2) mod a2'
print '\nAlice calculates:'
b5 = (b4**b1) % a2
print 'Key: ',b5,' (b4^b1) mod a2'
print 'Key: ',hashlib.sha256(str(b5)).hexdigest()
print '\nBob calculates:'
b6 = (b3**b2) % a2
print 'Key: ',b6,' (b3^b2) mod a2'
print 'Key: ',hashlib.sha256(str(b6)).hexdigest()