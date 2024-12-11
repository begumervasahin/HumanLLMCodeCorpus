
import texthelper as th
a1 = 31
a2 = 7
def fonk1():
	with open('./b1.txt') as fin:
		b1 = fin.readlines()
		b1 = [th.hex_to_nums(l.strip()) for l in b1]
		b2 = fonk2(b1)
		b3 = fonk3(b1,b2)
		b4 = fonk4(b3)
		for text in b4:
			print(text)
		b5 = b2.copy()
		b5[0] = b1[0][0] ^ ord('I')
		b5[6] = b1[0][6] ^ ord('l')
		b5[8] = b1[0][8] ^ ord('n')
		b5[10] = b1[0][10] ^ ord('i')
		b5[17] = b1[0][17] ^ ord('e')
		b5[20] = b1[0][20] ^ ord('e')
		b5[29] = b1[0][29] ^ ord('n')
		b5[30] = b1[0][30] ^ ord('.')
		b3 = fonk3(b1,b5)
		b4 = fonk4(b3)
		print()
		for text in b4:
			print(text)
def fonk2( b1 ):
	b6 = fonk5(b1)
	b2 = [None]*a1
	for i in range(a1):
		b7 = b6[i]
		if b7 = = -1:
			b8 = None
		else:
			b9 = b1[b7][i]
			b8 = b9 ^ ord(' ')
		b2[i] = b8
	return b2
def fonk3( b1, b5 ):
	b3 = []
	for ctext in b1:
		b10 = apply_key(ctext,b5)
		b3.append(b10)
	return b3
def fonk4( ptexts_ascii ):
	b3 = []
	for ptext_ascii in ptexts_ascii:
		b10 = clean_ptext(ptext_ascii)
		b3.append(b10)
	return b3
def fonk5( b1 ):
	 converts a list of ascii characters to   compares the ith character of all ciphertexts in the input list  outputs a list of scores indicating each chars liklihood of being a spcace  determines if this char is likely a space based on its b11 collision with """
	a3 = 0
	for b11 in list_xors:
		if (b11 > 64) or (b11 = = 0):
			a3 += 1
	return a3
fonk1()