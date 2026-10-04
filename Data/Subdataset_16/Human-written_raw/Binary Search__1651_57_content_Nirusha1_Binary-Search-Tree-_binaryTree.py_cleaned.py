class class1:
    def fonk1(self):
        self.a1 = 0
        self.b1 = None
    class class2:
        def fonk2(self,b2,b3):
            self.b2 = b2
            self.b3 = b3
            self.b4 = None
            self.b5 = None
    def fonk3(self,b2,b3):
        b6 = self.class2(b2,b3)
        b7 = None
        b8 = self.b1
        while(b8!=None):
            b7 = b8
            if(b2<b8.b2):
                b8 = b8.b4
            else:
                b8 = b8.b5
        if(b7 = =None):
            self.b1 = b6
        elif (b6.b2<b7.b2):
            b7.b4 = b6
        else:
            b7.b5 = b6
        self.a1 +=1
    def fonk4(self):
        if self.b1 is not None:
            b9 = self.b1
            while b9.b4 is not None:
                b9 = b9.b4
            return b9.b2
    def fonk5(self):
        if self.b1 is not None:
            b9 = self.b1
            while b9.b5 is not None:
                b9 = b9.b5
            return b9.b2
    def fonk6(self, b2):
        b10 = []
        self._searchForNode(self.b1, b2, b10)
	    return b10
    def fonk7(self, subtree, b2, b10):
	if(subtree):
            if(b2 = = subtree.b2):
                b10.append(1)
	    elif(b2 < subtree.b2):
		self._searchForNode(subtree.b4, b2, b10)
	    elif(b2 > subtree.b2):
		self._searchForNode(subtree.b5, b2, b10)
    def fonk8(self):
        return self.a1 = =0
    def fonk9(self):
        return self.a1
    def fonk10(self):
        b11 = []
        self.fonk11(self.b1, b11)
        return b11
    def fonk11(self, subtree, b11):
        if subtree:
            self.fonk11(subtree.b4,b11)
            b11.append(subtree.b2)
            self.fonk11(subtree.b5, b11)
    def fonk12(self):
        b11 = []
        self.fonk13(self.b1, b11)
        return b11
    def fonk13(self, subtree, b11):
        if subtree:
            b11.append(subtree.b2)
            self.fonk13(subtree.b4,b11)
            self.fonk13(subtree.b5, b11)
    def fonk14(self):
        b11 = []
        self.fonk15(self.b1, b11)
        return b11
    def fonk15(self, subtree, b11):
        if subtree:
            self.fonk15(subtree.b4,b11)
            self.fonk15(subtree.b5, b11)
            b11.append(subtree.b2)