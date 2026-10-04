import sys;
import subprocess;
from itertools import combinations;
from fractions import gcd;
from rsatool import rsatool;
b1 = []
b2 = 'authorized_keys'
b3 = []
b4 = [];
b5 = {};
b6 = {};
b7 = 0;
with open(b2) as f:
	b8 = f.readlines();
for b11 in b8:
	subprocess.call('echo "%s" > /tmp/rsa_; chmod 600 /tmp/rsa_' % b11, b9 = True);
	b5[b7] = subprocess.check_output("ssh-keygen -e -m PEM -f /tmp/rsa_ | openssl b16 -RSAPublicKey_in -in - -modulus -noout| cut -d '=' -f2", b9 = True);
	b5[b7] = int(b5[b7].rstrip("\n"), 16);
	b6[b7] = b11.split()[-1].split('@')[0];
	b3.append(str(b7))
	b7+=1;
b10 = {};
b10['b13'] = {};
b10['q1'] = {};
b10['q2'] = {};
b10['user1'] = {};
b10['user2'] = {};
b11 = 0;
for (b7, b12) in combinations(b3, 2):
	b7 = int(b7);
	b12 = int(b12);
	b11 = int(b11);
	b13 = gcd(b5[b7], b5[b12])
	if (b13 != 1):
		b1.append((b7, b12, b13, b5[b7]/b13, b5[b12]/b13))
		b4.append((b8[b7].rstrip(), b8[b12].rstrip()))
		b10['user1'][b11] = b6[b7];
		b10['user2'][b11] = b6[b12];
		b10['b13'][b11] = b13;
		b10['q1'][b11] = b5[b7]/b13;
		b10['q2'][b11] = b5[b12]/b13;
		b11+=1;
print b1
print "RSA Keys with common divisor: "
print b4[0]
print "b13, q1, q2:"
b14 = 0;
for b14 in range(b11):
	print "Generating keys for b6 %s and %s which share a common b13 \np: %s" %(b10['user1'][b14],b10['user2'][b14], b10['b13'][b14])
	print "User %s key:" % (b10['user1'][b14])
	print "(b15 = %d)" % b10['q1'][b14]
	b16 = rsatool.RSA(b13=b10['b13'][b14], b15=b10['q1'][b14], e=65537)
	b17 = b16.to_pem()
	print b17;
	print "User %s key :" % (b10['user2'][b14])
	print "(b15 = %d)" % b10['q2'][b14]
	b16 = rsatool.RSA(b13=b10['b13'][b14], b15=b10['q2'][b14], e=65537)
	b17 = b16.to_pem()
	print b17;