
from __future__ import print_function
b1 = []
b2 = []
class class1:
    def fonk1(self, name):
	if name in b1:
	    print("A vertex with name", name, "already exists.")
	else:
	    b1.append(name)
    def fonk2(self, start, b3):
	if b3 not in b1:
	    b1.append(b3)
	if start not in b1:
	    b1.append(start)
	if start in b1:
	    if b3 in b1:
		b2.append(start)
		b2.append(b3)
    def fonk3(self, name):
	if name in b1:
	    b1.remove(name)
	pass
    def fonk4(self, start, b3):
	b2.remove(start)
	b2.remove(b3)
    def fonk5(self):
	return b1
    def fonk6(self):
	a1 = -1
	for i in range(len(b2)/2):
	    print (b2[a1], "->", b3 = " ")
	    a1 = a1 + 2
	    print (b2[a1])
    def fonk7(self, start, b3):
	for i in range(len(b2)):
	    if b2[i] == start:
		if b2[i+1] == b3:
		    return True
	return False
    def fonk8(self, start, b3):
	for j in range(len(b1)):
	    if b1[j] == start:
		try:
		    if b1[j+1] == b3:
		        print(b1[j], "->", b1[j+1])
		    if b1[j+2] == b3:
		        print(b1[j], "->", b1[j+1], "->", b1[j+2])
		    if b1[j+3] == b3:
		        print(b1[j], "->", b1[j+1], "->", b1[j+2], "->", b1[j+3])
		    if b1[j+4] == b3:
		        print(b1[j], "->", b1[j+1], "->", b1[j+2], "->", b1[j+3], "->", b1[j+4])
		    if b1[j+5] == b3:
		        print(b1[j], "->", b1[j+1], "->", b1[j+2], "->", b1[j+3], "->", b1[j+4], "->", b1[j+5])
		except IndexError:
		    pass
	pass
class class2(class1):
    def fonk9(self):
	b1[:] = []
        b2[:] = []
    def fonk10(self, start, b3):
	if b3 not in b1:
	    b1.append(b3)
	if start not in b1:
	    b1.append(start)
	if start in b1:
	    if b3 in b1:
		b2.append(start)
		b2.append(b3)
    pass
    def fonk11(self, start, b3):
	b2.remove(start)
	b2.remove(b3)
    def fonk12(self):
	a1 = -1
	for i in range(len(b2)/2):
	    print (b2[a1], "<->", b3 = " ")
	    a1 = a1 + 2
	    print (b2[a1])
    def fonk13(self, start, b3):
	for j in range(len(b1)):
	    if b1[j] == start:
		try:
		    if b1[j+1] == b3:
		        print(b1[j], "<->", b1[j+1])
		    if b1[j+2] == b3:
		        print(b1[j], "<->", b1[j+1], "<->", b1[j+2])
		    if b1[j+3] == b3:
		        print(b1[j], "<->", b1[j+1], "<->", b1[j+2], "<->", b1[j+3])
		    if b1[j+4] == b3:
		        print(b1[j], "<->", b1[j+1], "<->", b1[j+2], "<->", b1[j+3], "<->", b1[j+4])
		    if b1[j+5] == b3:
		        print(b1[j], "<->", b1[j+1], "<->", b1[j+2], "<->", b1[j+3], "<->", b1[j+4], "<->", b1[j+5])
		except IndexError:
		    pass
	pass