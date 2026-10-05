def fonk1(ch):
	b1 = ord(ch) + 100;
	return b1;
def fonk2(ascii_val):
	b2 = int(ascii_val) - 100;
	return b2;
b3 = ''
def fonk3(msg):
	b4 = ''
	for a1 in msg:
		b4+=str(fonk1(a1));
	return b4;
def fonk4(newascii_string):
	b5 = ''
	a1 = 0
	b6 = ''
	while (a1 < len(str(newascii_string))):
		b5 = newascii_string[a1:a1+3]
		b6+=chr(fonk2(b5))
		a1 = a1+3
	return b6;