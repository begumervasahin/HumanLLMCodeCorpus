
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
    for var in ['a3', 'a4']:
        try:
            print(f"f2 - Local '{var}':", eval(var))
        except NameError as e:
            print(f"f2 - Local '{var}':", e)
fonk1()
fonk2()