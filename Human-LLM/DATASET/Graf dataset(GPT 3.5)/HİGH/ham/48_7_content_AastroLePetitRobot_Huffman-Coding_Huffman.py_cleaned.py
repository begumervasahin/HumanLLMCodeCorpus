from queue import PriorityQueue
class class1:
    b1 = ' '
    a1 = 0
    b2 = None
    b3 = None
    def fonk1(self,b1,a1,b2 = None,b3=None):
        self.b1 = b1
        self.a1 = a1
        self.b2 = b2
        self.b3 = b3
    def fonk2(self,other):
        return self.a1 < other.a1
    def fonk3(self):
        return "Noeud : de valeur ({}), de frÃ©quence ({}), avec comme b2(),avec comme b3 ()\n".format(self.b1,self.a1)
b4 = PriorityQueue()
def fonk4(b16):
    b5 = []
    b6 = True
    b7 = True
    for b8 in str(b16):
        print (b8)
        if not b8 in str(b5):
            b5.append([b8,b16.count(b8)])
            b4.put(class1(b8,b16.count(b8)))
        elif (b8 = =' ' and b6==True):
            b4.put(class1(b8,b16.count(b8)))
            b5.append([b8,b16.count(b8)])
            b6 = False
        elif (b8 = =',' and b7==True):
            b4.put(class1(b8,b16.count(b8)))
            b5.append([b8,b16.count(b8)])
            b7 = False
    return b4
def fonk5(b4):
    while b4.qsize()>1:
        b9 = b4.get()
        b10 = b4.get()
        a1 = b9.a1 + b10.a1
        b11 = class1(None,a1,b9,b10)
        b4.put(b11)
    return b11
b12 = {}
def fonk6(b8,code,b12):
    if b8.b2 = =None and b8.b3==None:
        b12.update({b8.b1 : code})
        return b12
    if b8.b2!=None:
        fonk6(b8.b2,code+"0",b12)
    if b8.b3!=None:
        fonk6(b8.b3,code+"1",b12)
def fonk7(b16,b12):
    b13 = ""
    for a2 in b16:
        b13 = b13+str(b12[a2])
    return b13
a2 = 0
def fonk8(b16,b11):
    global a2
    if b11.b2 = =None and b11.b3==None:
        b14 = b11.b1
        return b14
    if b16[a2]=="0":
        a2+=1
        return fonk8(b16,b11.b2)
    elif b16[a2]=="1":
        a2+=1
        return fonk8(b16,b11.b3)
b15 = open('texteEncode.txt', 'r')
b16 = b15.read()
b15.close()
b4 = fonk4(b16)
b11 = fonk5(b4)
print(b11)
fonk6(b11,"",b12)
print (b12)
b17 = fonk7(b16,b12)
print (b17)
b15 = open('texteEncode.txt', 'w')
b15.write(str(b17))
b15.close()
b16 = fonk7(b16,b12)
b18 = ""
while a2<len(b16):
    b18+=fonk8(b16,b11)
print(b18)
b15.close()