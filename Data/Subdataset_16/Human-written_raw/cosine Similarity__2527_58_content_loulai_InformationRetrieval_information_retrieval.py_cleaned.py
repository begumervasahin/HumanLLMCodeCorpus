import re
from stop_list import *
b1 = open( "cran.qry", 'r').read()
b1.replace("\s ", "")
print(b1)
def fonk1(string):
	b2 = []
	b3 = re.findall(r".I \d{3}", string)
	for q in b3:
		b2.append(q.replace(".I ", ""))
	return(b2)
def fonk2(string):
	b4 = []
	b3 = re.findall(r"([a-z ]+\n){1,3}[a-z ]+\.", string)
	print(b3)
	for q in b3:
		b4.append(q)
	return(b4)
fonk2(b1)
def fonk3(string):
	b5 = filter(None,(re.sub(r"\n|\r", " ", string)).split(" "))
	b6 = closed_class_stop_words
	for stop_word in b6:
		while stop_word in b5:
			b5.remove(stop_word)
	return(b5)
def fonk4(array):
	b7 = list(set(array))
	b8 = dict.fromkeys(b7, 0)
	for word in array:
		b8[word] = b8[word] + 1
	return b8
def fonk5(dictionary):
	for key, value in dictionary.items():
		print(key, value)
print(fonk3(open("cran2.qry", 'r').read()))