import os
import argparse
def fonk1(n):
	b1 = ""
	for i in range(0,n):
		b1 += unichr(65 + ord(os.urandom(1))%26)
	return b1
def fonk2(a, b):
	b2 = ""
	for i in range(0,len(a)):
		b2 += unichr(64 + (ord(a[i]) ^ ord(b[i])))
	return b2
def fonk3(a):
	return a.upper().replace(" ", "a").replace(".", "b").replace(",", "b2").replace("'", "d")
def fonk4(a):
	return a.replace("a", " ").replace("b", ".").replace("b2", ",").replace("d","'")
b3 = argparse.ArgumentParser(
        b4 = 'Encrypt or Decrypt data using One-Time Pad')
b3.add_argument('-d', '--decrypt', b5 = 'store_true',
        b6 = 'Decrypt data (default is to encrypt)')
b7 = b3.parse_args()
if b7.decrypt:
	b8 = raw_input("b8: ")
	b9 = raw_input("b9 stuff: ")
	print fonk4(fonk2(b8,b9))
else:
	b10 = fonk3(raw_input("message: "))
	b8 = fonk1(len(b10))
	print b8, fonk2(b10, b8)