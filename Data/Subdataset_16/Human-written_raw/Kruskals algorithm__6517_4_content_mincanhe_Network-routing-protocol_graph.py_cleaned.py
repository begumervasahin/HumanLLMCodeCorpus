import random
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self, connection):
        self.b2.append(connection)
    def fonk3(self, connection):
        self.b2.remove(connection)
    def fonk4(self, t):
        for c in self.b2:
            if c[0]==t:
                return True
            return False
def fonk5(n, degree):
    b3 = []
    b4 = []
    b5 = []
    for i in range(n):
        b4.append(i)
        b3.append(class1(i, []))
    random.shuffle(b4)
    for i in range(n):
        b6 = i
        b7 = i
        for k in range(int(degree / 2)):
            b7 += 1
            if b7 >n-1:
                b7 = 0
            if b7 > i:
                b8 = random.randint(0,100)
                b3[b4[i]].fonk2([b4[b7], b8])
                b3[b4[b7]].fonk2([b4[i], b8])
            if b4[i]> b4[b7]:
                b5.append([b4[b7],b4[i],b8])
            else:
                b5.append([b4[i],b4[b7],b8])
            b6 -= 1
            if b6 <0:
                b6 = n-1
            if b6 > i:
                b8 = random.randint(0,100)
                b3[b4[i]].fonk2([b4[b6],b8])
                b3[b4[b6]].fonk2([b4[i],b8])
            if b4[i]> b4[b6]:
                b5.append([b4[b6],b4[i],b8])
            else:
                b5.append([b4[i],b4[b6],b8])
    b9 = open ('./b5.txt', 'a')
    for e in b5 :
        b9.write(str(e[0]) + '' + str(e[1]) + '' + str(e[2])+ '\n')
    b9.close ()
    return b3
fonk5(5000, 6);
fonk5(5000, 1000);