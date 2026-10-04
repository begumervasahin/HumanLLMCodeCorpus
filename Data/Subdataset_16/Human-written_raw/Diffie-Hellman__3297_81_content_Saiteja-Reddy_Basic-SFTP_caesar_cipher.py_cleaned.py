def fonk1():
	b1 = {}
	b2 = {}
	b1[' '] = 00
	b2[0] = ' '
	for i in range(65, 65 + 26):
		b1[chr(i)] =  i-64
		b2[i-64] =  chr(i)
	b1[','] = 27
	b1['.'] = 28
	b1['?'] = 29
	b2[27] = ','
	b2[28] = '.'
	b2[29] = '?'
	for i in range(48, 48 + 10):
		b1[chr(i)] =  i-18
		b2[i-18] =  chr(i)
	for i in range(97, 97 + 26):
		b1[chr(i)] =  i-57
		b2[i-57] =  chr(i)
	b1['!'] = 66
	b2[66] = '!'
	return (b1, b2)
def fonk2(string, key):
	b1, b2 = fonk1()
	b3 = list(b1.b3())
	b4 = ""
	for char in string:
		if char not in b3:
			return -1
		else:
			b5 = b1[char]
			b6 = ((b5 + key) % 67)
			b4 += b2[b6]
	return b4
def fonk3(string, key):
	b1, b2 = fonk1()
	b3 = list(b1.b3())
	b4 = ""
	for char in string:
		if char not in b3:
			return -1
		else:
			b5 = b1[char]
			b6 = ((b5 - key) % 67)
			b4 += b2[b6%67]
	return b4