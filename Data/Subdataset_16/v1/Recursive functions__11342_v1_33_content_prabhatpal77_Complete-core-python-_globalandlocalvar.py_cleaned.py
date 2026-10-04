
a1 = 1000
a2 = 2000
def fonk1():
    a3 = 3000
    a4 = 4000
    print("Inside fonk1()")
    print(f"a1: {a1}")
    print(f"a2: {a2}")
    print(f"a3: {a3}")
    print(f"a4: {a4}")
def fonk2():
    a5 = 5000
    a6 = 6000
    print("Inside fonk2()")
    print(f"a1: {a1}")
    print(f"a2: {a2}")
    print(f"a5: {a5}")
    print(f"a6: {a6}")
    try:
        print(f"a3: {a3}")
    except NameError as e:
        print(e)
    try:
        print(f"a4: {a4}")
    except NameError as e:
        print(e)
fonk1()
fonk2()