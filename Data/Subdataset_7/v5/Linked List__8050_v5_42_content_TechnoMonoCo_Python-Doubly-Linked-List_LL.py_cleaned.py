class class1:
    def fonk1(b5, b2, b1 = None, b3=None):
        b5.b2 = b2
        b5.b1 = b1
        b5.b3 = b3
    def fonk2(b5, b2):
        if b5.b2 = = b2:
            if b5.b3 is None:
                if b5.b1:
                    b5.b2 = b5.b1.b2
                    b5.b1 = b5.b1.b1
                else:
                    b5.b2 = None
                return 0
            elif b5.b1 is None:
                b5.b3.b1 = None
                return 0
            else:
                b5.b3.b1 = b5.b1
                return 0
        elif b5.b1:
            return b5.b1.fonk2(b2)
        else:
            return -1
    def fonk3(b5, b2):
        if b2 < b5.b2:
            b4 = class1(b2, b5, None)
            b5 = b4
        elif b5.b1 is None:
            b4 = class1(b2, None, b5)
            b5.b1 = b4
        else:
            b5.b1.fonk3(b2)
    def fonk4(b5):
        b6 = b5
        if b6.b2 is None:
            print("Empty.")
        else:
            while b6:
                print(b6.b2, b7 = ", ")
                b6 = b6.b1
            print()
def fonk5():
    b8 = class1(0)
    print("contains...")
    b8.fonk4()
    print()
    print("inserting 1...")
    b8.fonk3(1)
    print("contains:")
    b8.fonk4()
    print()
    print("inserting 5...")
    b8.fonk3(5)
    print("contains:")
    b8.fonk4()
    print()
    print("removing 1...")
    b8.fonk2(1)
    print("contains:")
    b8.fonk4()
    print()
    print("removing 5...")
    b8.fonk2(5)
    print("contains...")
    b8.fonk4()
    print()
    print("removing 0...")
    b8.fonk2(0)
    print("contains:")
    b8.fonk4()
    print()
fonk5()