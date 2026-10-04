
a1 = 1000
a2 = 2000
def fonk1():
    a3 = 3000
    a4 = 4000
    print("f1 - Global 'a1':", a1)
    print("f1 - Global 'a2':", a2)
    print("f1 - Local 'a3':", a3)
    print("f1 - Local 'a4':", a4)
def fonk2():
    a5 = 5000
    a6 = 6000
    print("f2 - Global 'a1':", a1)
    print("f2 - Global 'a2':", a2)
    print("f2 - Local 'a5':", a5)
    print("f2 - Local 'a6':", a6)
    try:
        print("f2 - Local 'a3':", a3)
    except NameError as e:
        print("f2 - Local 'a3':", e)
    try:
        print("f2 - Local 'a4':", a4)
    except NameError as e:
        print("f2 - Local 'a4':", e)
fonk1()
fonk2()