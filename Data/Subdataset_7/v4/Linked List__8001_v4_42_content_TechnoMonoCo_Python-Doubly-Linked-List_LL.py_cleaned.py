class class1:
    def fonk1(b6, b2, b1 = None, b3=None):
        b6.b2 = b2
        b6.b1 = b1
        b6.b3 = b3
    def fonk2(b6, b2):
        if b6.b3 is None:
            if b6.b2 = = b2:
                if b6.b1 is None:
                    b6.b2 = None
                    return 0
                b4 = b6.b1
                b6.b2 = b6.b1.b2
                b6.b1 = b6.b1.b1
                del b4
                return 0
            elif b6.b1 is None:
                return -1
            else:
                return b6.b1.fonk2(b2)
        else:
            if b6.b1 is None:
                if b6.b2 = = b2:
                    b4 = b6
                    b5 = b6.b3
                    b5.b1 = None
                    del b4
                    return 0
                else:
                    return -1
            else:
                if b6.b2 = = b2:
                    b4 = b6
                    b5 = b6.b3
                    b5.b1 = b6.b1
                    del b4
                    return 0
                else:
                    return b6.b1.fonk2(b2)
    def fonk3(b6, b2):
        if b2 < b6.b2:
            b4 = class1(b2, b6, None)
            b6 = b4
        elif b6.b1 is None:
            b4 = class1(b2, None, b6)
            b6.b1 = b4
        else:
            b6.b1.fonk3(b2)
    def fonk4(b6, b7):
        if b6.b2 is None:
            print(b7)
        else:
            b7 = b7 + ", " + str(b6.b2)
            if b6.b1 is None:
                print(b7)
            else:
                b6.b1.fonk4(b7)
    def fonk5(b6):
        if b6.b1 is None:
            if b6.b2 is None:
                print("Empty.")
            else:
                print(b6.b2)
        else:
            b6.b1.fonk4(str(b6.b2))
def fonk6():
    b8 = class1(0)
    print("contains...")
    b8.fonk5()
    print()
    print("inserting 1...")
    b8.fonk3(1)
    print("contains:")
    b8.fonk5()
    print()
    print("inserting 5...")
    b8.fonk3(5)
    print("contains:")
    b8.fonk5()
    print()
    print("removing 1...")
    b8.fonk2(1)
    print("contains:")
    b8.fonk5()
    print()
    print("removing 5...")
    b8.fonk2(5)
    print("contains...")
    b8.fonk5()
    print()
    print("removing 0...")
    b8.fonk2(0)
    print("contains:")
    b8.fonk5()
    print()
fonk6()