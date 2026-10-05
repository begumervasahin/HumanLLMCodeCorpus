import os
from buildTree import firstRound
print(" ")
print(" ")
print("Andre Luiz LourenÃ§o de Andrade - 14/0016295")
print("Teoria da Informacao - Huffman Compressor")
print(" ")
b1 = []
def fonk1():
	fonk2()
def fonk2():
	b2 = input("Please enter a b4 or b3 to compress >>> ")
	if b2.find("-c") != -1:
		b3 = b2.split()[1]
		print("You choose", b3, "as b3 to be compressed...")
		fonk4(b3)
		return b3
	else:
		b4 = b2
		fonk3(b4)
		return b4
def fonk3(b4):
	print(" ")
	print("This function is not ready yet... Please choose a .txt b3 in your directory: " + os.getcwd())
	fonk2()
def fonk4(b3):
	b5 = open(b3, "rb")
	if b5.b6 = = 'rb':
		b7 = b5.read()
		fonk6(b7)
		return b7
def fonk5(contentFile):
	b8 = len(contentFile)
	return b8
def fonk6(contentFile):
	b9 = {}
	for i in contentFile:
		if i not in b9.keys():
			b9[i]=1
		else:
			b9[i]+=1
	fonk7(b9, contentFile)
	b1 = b9.keys()
	return b9
def fonk7(dictionary, contentFile):
	global b1
	b1 = dictionary.keys()
	for key in dictionary:
		dictionary[key] /= len(contentFile)
		b10 = sorted(dictionary.values(), reverse=True)
	firstRound(b10, b1)
	return b10
fonk1()