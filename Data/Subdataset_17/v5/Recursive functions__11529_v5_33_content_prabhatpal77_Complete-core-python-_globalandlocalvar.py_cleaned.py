
a = 1000
b = 2000
def f1():
    p = 3000
    q = 4000
    print("f1 - Global 'a':", a)
    print("f1 - Global 'b':", b)
    print("f1 - Local 'p':", p)
    print("f1 - Local 'q':", q)
def f2():
    x = 5000
    y = 6000
    print("f2 - Global 'a':", a)
    print("f2 - Global 'b':", b)
    print("f2 - Local 'x':", x)
    print("f2 - Local 'y':", y)
    for var in ['p', 'q']:
        try:
            print(f"f2 - Local '{var}':", eval(var))
        except NameError as e:
            print(f"f2 - Local '{var}':", e)
f1()
f2()