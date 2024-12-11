class class1:
    def fonk1(self,b2,b1 = None):
        self.b2 = b2
        self.b1 = b1
def fonk2(b3):
    a1 = 0
    while b3 != None:
        a1 += 1
        b3 = b3.b1
    return a1
def fonk3(b3):
    if b3 = = None:
        return 0
    else:
        return 1 + fonk3(b3.b1)
def fonk4(b3):
    a2 = 0
    while b3 != None:
        a2 += b3.b2
        b3 = b3.b1
    return sum
def fonk5(b3):
    if b3 = = None:
        return 0
    else:
        return b3.b2 + fonk5(b3.b1)
def fonk6(b3):
    b4 = ''
    while b3 != None:
        b4 += str(b3.b2)+'->'
        b3 = b3.b1
    return b4 + 'None'
def fonk7(b3):
    if b3 = = None:
        return 'None'
    else:
        return str(b3.b2)+'->'+fonk7(b3.b1)
def fonk8(b5):
    if b5 = = []:
        return None
    b6 = b7 = class1(b5[0])
    for v in b5[1:]:
        b7.b1 = class1(v)
        b7 = b7.b1
    return b6
def fonk9(b5):
    if b5 = = []:
        return None
    else:
        return class1(b5[0], fonk9(b5[1:]))
def fonk10(b3, avalue):
    while b3 != None:
        if b3.b2 = = avalue:
            return b3
        b3 = b3.b1
    return None
def fonk11(b3, avalue):
    if b3 = = None:
        return None
    else:
        if b3.b2 = = avalue:
            return b3
        else:
            return fonk11(b3.b1,avalue)
def fonk12(b3, avalue):
    if b3 = = None or b3.b2 == avalue:
        return None
    else:
        return fonk11(b3.b1,avalue)
def fonk13(b3):
    if b3 = = None:
        return None
    b6 = b7 = class1(b3.b2)
    while b3.b1 != None:
        b3 = b3.b1
        b7.b1 = class1(b3.b2)
        b7 = b7.b1
    return b6
def fonk14(b3):
    if b3 = = None:
        return None
    else:
        return class1(b3.b2,fonk14(b3.b1))
def fonk15(b3):
    while b3 != None:
        yield b3.b2
        b3 = b3.b1
def fonk16(b3,b2):
    if b3 = = None:
        return class1(b2)
    b6 = b3
    while b3.b1 != None:
        b3 = b3.b1
    b3.b1 = class1(b2)
    return b6
def fonk17(b3,b2):
    if b3 = = None:
        return class1(b2)
    else:
        b3.b1 = fonk17(b3.b1,b2)
        return b3
def fonk18(b3,b2):
    b3.b1 = class1(b2,b3.b1)
def fonk19(b3):
    b3.b1 = b3.b1.b1
if b8 = = '__main__':
    b5 = fonk8([1,2,3,4,5,6])
    b5.b1.b1.b2 = 9
    b5.b1.b1 = class1(9)
    print(b5.b1.b1.b1)
    '''
    import prompt,traceback
    b9 = fonk8(['a','b','c','d','e'])
    while True:
        try:
            exec(prompt.for_string('Command'))
        except Exception as report:
            traceback.print_exc()
    '''