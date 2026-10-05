class class1:
    def fonk1(self,b2):
        b1 = len(b2)
        b2 = sorted(b2)
        if b1%b3 = =0:
            return (b2[b1
        else:
            return b2[(b1
        print('Hello')
    def fonk2(self,b2):
        b4 = {}
        for i in set(b2):
            b4[i]=b2.count(i)
        b5 = b4[max(b4,key=b4.get)]
        if b5<=1:return [0]
        else:return [key for key,b6 in b4.items() if b6 = = b5]
    def fonk3(self,b2):
        return sum(b2)/len(b2)
    def fonk4(self,b2):
        b7 = self.fonk3(b2)
        return sum([(i-b7)**b3 for i in b2])/len(b2)
    def fonk5(self,b2):
        return (self.fonk4(b2))**.5
def fonk6():
    b8 = class1()
    b2 = [float(i) for i in open("b2.txt",'r')]
    print('Median is %.2f'%(b8.fonk3(b2)))
    print('Mean is %.2f'%(b8.fonk1(b2)))
    print('Mode is '+(', '.join(map(str,[i for i in b8.fonk2(b2)]))))
    print('Variance is %.2f'%(b8.fonk4(b2)))
    print('Standard Dev is %.2f'%(b8.fonk5(b2)))
if b9 = = "__main__":
    fonk6()