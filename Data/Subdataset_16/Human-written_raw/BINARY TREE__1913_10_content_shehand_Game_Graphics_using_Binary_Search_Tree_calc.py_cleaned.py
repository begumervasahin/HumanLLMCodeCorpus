class class1:
    def fonk1(self,indx):
        self.b1 = indx
        self.b2 = []
    def fonk2(self,x1,y1,x2,y2):
        if (x1-x2)!=0:
            b3 = (y1-y2)/(x1-x2)
            b4 = y1-(b3*x1)
            if abs(b3)==0:
                self.b2.insert(0,abs(b3))
            else:
                self.b2.insert(0,b3)
            self.b2.insert(1,b4)
        else:
            self.b2.insert[0,None]
            self.b2.insert[1,0]
            self.b2.insert[2,x1]
    def fonk3(self):
        return self.b1
class class2:
    def fonk4(self,b6,b7):
        self.b5 = None
        self.b6 = b6
        self.b7 = b7
    def fonk5(self,b3):
        if self.b6 = =b3:
            return True
        else:
            return False
    def fonk6(self,b4):
        if self.b7 = =b4:
            return True
        else:
            return False
    def fonk7(self,tmpc):
        if self.b6>0:
            if self.b7>tmpc:
                return 1
            else:
                return 0
        elif self.b6<0:
            if self.b7>tmpc:
                return 0
            else:
                return 1
        else:
            return
    def fonk8(self,b3,b4,dArray,tArray):
        b8 = float(tArray[1])
        b9 = float(tArray[3])
        b10 = max(b8,b9)
        b11 = min(b8,b9)
        if self.b6!=None and b3!=None:
            if self.b6*b3<0:
                if self.b7<b4:
                    b12 = max(float(dArray[1]),float(dArray[3]))
                    if b10>b12 and b11<b12:
                        return True
                    else:
                        return False
                elif self.b7>b4:
                    b12 = min(float(dArray[1]),float(dArray[3]))
                    if b10>b12 and b11<b12:
                        return True
                    else:
                        return False
                else:
                    return True
            elif self.b6!=b3 and self.b6*b3>0:
                b13 = (b4 - self.b7)/(self.b6-b3)
                b14 = b3*b13+b4
                if b14>b11 and b14<b10:
                    return True
                else:
                    return False
            else:
                return False
        elif self.b6 = =None:
            b13 = float(dArray[0])
            b15 = float(tArray[0])
            b16 = float(tArray[2])
            b17 = max(b15,b16)
            b18 = min(b15,b16)
            if b13>b18 and b13<b17:
                return True
            else:
                return False
        elif b3 = =None:
            b13 = float(tArray[0])
            b19 = float(dArray[0])
            b20 = float(dArray[2])
            b21 = max(b19,b20)
            b22 = min(b19,b20)
            if b13>b22 and b13<b21:
                return True
            else:
                return False
        else:
            return False