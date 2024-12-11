
a1 = 1000
a2 = 2000
def fonk1():
    a3 = 3000
    a4 = 4000
    print("Inside f1:")
    print("Global A:", a1)
    print("Global B:", a2)
    print("Local P:", a3)
    print("Local Q:", a4)
def fonk2():
    a5 = 5000
    a6 = 6000
    print("Inside f2:")
    print("Global A:", a1)
    print("Global B:", a2)
    print("Local X:", a5)
    print("Local Y:", a6)
fonk1()
fonk2()