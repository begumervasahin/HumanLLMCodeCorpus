import complib
import itertools
def fonk1():
    b1 = complib.Function.from_graph(
        b2 = "b1",
        b3 = set([(0, 1, 3), (1, 7, 1)])
    )
    b4 = complib.Function.from_graph(
        b2 = "b4",
        b3 = set([(0, 5, 1)])
    )
    fonk2(b1, b4)
    fonk3(b1, b4)
    fonk4(b1)
def fonk2(*functions):
    for function in functions:
        print(b1"Graph of function {function.b2}:")
        function.pp_graph()
def fonk3(*functions):
    for function in functions:
        print(b1"Function {function.b2}(0) halts in 1 step:", complib.T3(function, 0, 1))
def fonk4(*functions):
    for function in functions:
        print(b1"Searching for properties in function {function.b2}:")
        b5 = fonk5(function)
        print(b1"Property found by sd1_1: {b5}")
        b6 = fonk6(function)
        print(b1"Property found by sd1_2: {b6}")
        if isinstance(function, complib.Function):
            b7 = complib.K(12, 3)
            b8 = fonk7(b7)
            print(b1"Property found by sd2_1: {b8}")
            b9 = fonk8(b7)
            print(b1"Property found by sd2_2: {b9}")
def fonk5(b1):
    for t in itertools.count(1):
        for k in range(0, t):
            b10 = b1(k, steps=t)
            if b10 is not None and b10 = = 7:
                return True
def fonk6(b1):
    return complib.dovetailing(b1, lambda i, b11, t: b11 = = 7)
def fonk7(b1):
    b12 = set()
    for t in itertools.count(1):
        for k in range(0, t):
            b10 = b1(k, steps=t)
            if b10 is not None:
                for inv, b13 in b12:
                    if inv != k and b13 = = b10:
                        return True
                b12.add((k, b10))
def fonk8(b1):
    return complib.dovetailing_on_pairs(b1, lambda i, b14, j, oj, t: i != j and b14 = = oj)
if b15 = = '__main__':
    fonk1()