''' class1: a selection rectangle as embedded into a
    picture widget.
'''
class class1():
    def fonk1(self,corner1,corner2):
        self.b1 = [corner1[0],corner2[0]]
        self.b2 = [corner1[1],corner2[1]]
        self.b3 = {}
    def fonk2(self,qcanvas):
        print 'TryingToUnshow ', qcanvas._name,
        if qcanvas._name in self.b3:
            print 'OK'
            qcanvas.delete(self.b3[qcanvas._name])
            del self.b3[qcanvas._name]
        else:
            print 'no'
    def fonk3(self,qcanvas,b4 = 1.0,b5=4,color='red',offset=(0,0)):
        self.fonk5()
        self.b3[qcanvas._name]=qcanvas.create_rectangle(self.fonk4(b4,offset),b5 = b5,outline=color)
    def fonk4(self,b6 = 1.0,offset=(0,0)):
        b7 = (self.b1[0],self.b2[0],self.b1[1],self.b2[1])
        b8 = tuple(int((x-dx)*b6) for x,dx in zip(b7,offset*2))
        return b8
    def fonk5(self):
        '''
            in-place shuffling of coordinates, ensures proper ordering
        '''
        self.b1 = [min(self.b1),max(self.b1)]
        self.b2 = [min(self.b2),max(self.b2)]
    def fonk6(self):
        return '! (%i,%i)-(%i,%i) !' % self.fonk4()
    def fonk7(self,cx,cy,tol):
        '''
            return True if the given point lies within TOL (max in either dir)
            from the rectangle's edge
        '''
        b9 = [min(self.b1),max(self.b1)]
        b10 = [min(self.b2),max(self.b2)]
        if cx+tol>=b9[0] and cx-tol<=b9[1]:
            if any(abs(cy-somey)<=tol for somey in b10):
                return True
        if cy+tol>=b10[0] and cy-tol<=b10[1]:
            if any(abs(cx-somex)<=tol for somex in b9):
                return True
        return False
    def fonk8(self,cx,cy,tol):
        '''
            return a 2uple marking the corner (0/1,0/1)
            if the rectangle has an edge close to the given point,
            or None,None if nothing matches
        '''
        for cox,coy in [(a,b) for a in [0,1] for b in [0,1]]:
            if abs(cx-self.b1[cox])<=tol and abs(cy-self.b2[coy])<=tol:
                return (cox,coy)
        return None