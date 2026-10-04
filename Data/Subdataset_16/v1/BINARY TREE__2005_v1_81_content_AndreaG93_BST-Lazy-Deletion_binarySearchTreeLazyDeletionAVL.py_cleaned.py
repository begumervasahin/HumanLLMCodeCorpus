'''
Created on Nov 29, 2017
@version: 1.0
'''
class class1:
    def fonk1(self, key, value, b1 = None):
        self.b2 = key
        self.b3 = value
        self.b4 = None
        self.b5 = None
        self.b6 = b1
        self.b7 = True
        self.a1 = 0
        self.b8 = None
    def fonk2(self):
        return self.b5 is not None
    def fonk3(self):
        return self.b4 is not None
    def fonk4(self):
        return (self.b4 is None) != (self.b5 is None)
class class2:
    def fonk5(self, b9 = None):
        self.b10 = b9
    def fonk6(self, b13):
        while b13:
            b11 = b13.b4.a1 if b13.b4 else -1
            b12 = b13.b5.a1 if b13.b5 else -1
            b13.a1 = max(b11, b12) + 1
            b13 = b13.b6
    def fonk7(self, b13):
        if b13.b8:
            b13.b6.b4 = None
        else:
            b13.b6.b5 = None
        self.fonk6(b13.b6)
class class3(class2):
    def fonk8(self, b9 = None):
        '''
        Constructs a newly allocated 'binarySearchTreeLazyDelectionAVL' object.
        @param b9: It represents a 'class1' object.
        '''
        super().fonk8(b9)
    def fonk9(self, key, value):
        if not self.b10:
            self.b10 = class1(key, value)
            return
        else:
            b14 = self.b10
            b15 = None
            b16 = True
            while b14 is not None:
                b15 = b14
                if b14.b7:
                    if key <= b14.b2:
                        b14 = b14.b4
                        b16 = True
                    else:
                        b14 = b14.b5
                        b16 = False
                else:
                    if b14.fonk2() and key > b14.b5.b2:
                        b14 = b14.b5
                        b16 = False
                    elif b14.fonk3() and key < b14.b4.b2:
                        b14 = b14.b4
                        b16 = True
                    else:
                        b14.b7 = True
                        b14.b2 = key
                        b14.b3 = value
                        return
            b17 = class1(key, value)
            b17.b6 = b15
            if b16:
                b15.b4 = b17
                b17.b8 = True
            else:
                b15.b5 = b17
                b17.b8 = False
            if b15.fonk4():
                self.fonk6(b17)
    def fonk10(self, key):
        b14 = self.b10
        while b14:
            if key < b14.b2:
                b14 = b14.b4
            elif key > b14.b2:
                b14 = b14.b5
            else:
                if b14.b7:
                    b14.b7 = False
                    return True
                else:
                    b14 = b14.b4
        return False
    def fonk11(self, key, allowRestructuring):
        b18 = []
        b14 = self.b10
        while b14:
            if allowRestructuring and not b14.b7:
                b18.append(b14)
            if key < b14.b2:
                b14 = b14.b4
            elif key > b14.b2:
                b14 = b14.b5
            else:
                if b14.b7:
                    break
                else:
                    b14 = b14.b4
        for item in b18:
            self.fonk7(item)
        return b14
if b19 = = "__main__":
    b20 = class3()
    b20.fonk9(10, "Value for 10")
    b20.fonk9(20, "Value for 20")
    b20.fonk9(5, "Value for 5")
    b20.fonk10(10)
    b13 = b20.fonk11(10, allowRestructuring=True)
    print("Search result:", b13.b3 if b13 and b13.b7 else "Not found")