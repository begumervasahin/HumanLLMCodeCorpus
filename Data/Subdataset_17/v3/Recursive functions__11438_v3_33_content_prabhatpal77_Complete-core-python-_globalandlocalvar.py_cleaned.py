
a = 1000
b = 2000
def f1():
    p = 3000
    q = 4000
    print("Inside f1()")
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"p: {p}")
    print(f"q: {q}")
def f2():
    x = 5000
    y = 6000
    print("Inside f2()")
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"x: {x}")
    print(f"y: {y}")
    try:
        print(f"p: {p}")
    except NameError as e:
        print(f"Error accessing p: {e}")
    try:
        print(f"q: {q}")
    except NameError as e:
        print(f"Error accessing q: {e}")
def main():
    f1()
    f2()
if __name__ == "__main__":
    main()