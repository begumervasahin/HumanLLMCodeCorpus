a1 = 785963102379428822376694789446897396207498568951
a2 = 317689081251325503476317476413827693272746955927
a3 = 79052896607878758718120572025718535432100651934
a4 = 771507216262649826170648268565579889907769254176
a5 = 390157510246556628525279459266514995562533196655
import random
def fonk1(b3, b4):
    if not b4:
        return (b3, 1, 0)
    d1, b9, b1 = fonk1(b4, b3%b4)
    return (d1, b1, b9-(b3
class class1:
    def fonk2(self, b2, b3, b4):
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = None
    def fonk3(self, n):
        return (fonk1(n, self.b2)[1])%self.b2
    def fonk4(self, b6):
        if b6 = = (-1, -1):
            return True
        x, b7 = b6
        if not ((b7*b7)%self.b2-(x*x+self.b3)%self.b2*x-self.b4)%self.b2:
            return True
        return False
    def fonk5(self, point1, point2):
        b9, b1 = point1
        b13, b8 = point2
        if b9 = = b13:
            return (-1, -1)
        elif b9 < 0:
            return p2
        elif b13 < 0:
            return p1
        b10 = ((b8-b1)*self.fonk3((b13-b9)%self.b2))%self.b2
        b11 = ((b10*b10)%self.b2-b9-b13)%self.b2
        b12 = (b10*(b9-b11)-b1)%self.b2
        return (b11, b12)
    def fonk6(self, b6):
        b9, b1 = b6
        if b9 < 0 or b1 = = 0:
            return (-1, -1)
        b10 = (((3*b9*b9)%self.b2+self.b3)%self.b2*self.fonk3((2*b1)%self.b2))%self.b2
        b13 = ((b10*b10)%self.b2-2*b9)%self.b2
        b8 = ((b10*(b9-b13))%self.b2-b1)%self.b2
        return (b13, b8)
    def fonk7(self, n, b6):
        if n:
            b14 = b6
            b15 = []
            a6 = 1
            while a6 <= n:
                b15.append(bool(a6&n))
                a6 <<= 1
            b15.reverse()
            for a6 in b15[1:]:
                b14 = self.fonk6(b14)
                if a6:
                    b14 = self.fonk5(b14, b6)
            return b14
        else:
            return (-1, -1)
    def fonk8(self, b16 = None, b6 = None):
        if not b6:
            b6 = self.b5
        if not b16:
            b16 = random.randint(3, self.b2-1)
        return self.fonk7(b16, b6)
b17 = class1(a1, a2, a3)
b18 = (a4, a5)