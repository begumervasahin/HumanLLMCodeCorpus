import complib
import itertools
def fonk1():
    b1 = complib.Function.from_graph(
        b2 = "b1",
        b3 = set([
            (0, 1, 3),
            (1, 7, 1)
        ])
    )
    b4 = complib.Function.from_graph(
        b2 = "b4",
        b3 = set([
            (0, 5, 1)
        ])
    )
    print("Graph of function b1:")
    b1.pp_graph()
    print("Graph of function b4:")
    b4.pp_graph()
    print("Graph of function K0:")
    complib.K0.pp_graph()
    print("Graph of function ident:")
    complib.ident.pp_graph()
    print("Graph of function undef:")
    complib.undef.pp_graph()
    print("Function b1(0) halts in 1 step:", complib.T3(b1, 0, 1))
    print("Function b4(0) halts in 1 step:", complib.T3(b4, 0, 1))
    print("Function K0(0) halts in 1 step:", complib.T3(complib.K0, 0, 1))
    print("Function ident(0) halts in 1 step:", complib.T3(complib.ident, 0, 1))
    print("Function undef(0) halts in 1 step:", complib.T3(complib.undef, 0, 1))
    print("Graph of function b1:", b1.b3(0, 3))
    print("Graph of function b4:", b4.b3(0, 3))
    print("Graph of function K0:", complib.K0.b3(0, 3))
    print("Graph of function ident:", complib.ident.b3(0, 3))
    print("Graph of function undef:", complib.undef.b3(0, 3))
    print("b1(0) =", b1(0))
    print("b4(0) =", b4(0))
    print("K0(0) =", complib.K0(0))
    print("ident(0) =", complib.ident(0))
    print("undef(0) =", complib.undef(0, b5 = "continue"))
    fonk2(b1)
    fonk3(b1)
    fonk2(complib.ident)
    fonk3(complib.ident)
    b6 = complib.K(12, 3)
    fonk4(b6)
    fonk5(b6)
    print("Encoding and decoding of pairs as natural numbers:")
    for i in range(10):
        b7 = complib.number2pair(i)
        b8 = complib.pair2number(*b7)
        print(i, "->", b7, "->", b8)
def fonk2(b1):
    for t in itertools.count(1):
        for k in range(0, t):
            print("Running function {} on input {} for {} steps.".format(b1, k, t))
            b9 = b1(k, steps=t)
            if b9 is not None and b9 = = 7:
                print("On this input it returns 7!")
                return True
def fonk3(b1):
    return complib.dovetailing(b1, lambda i, b10, t: b10 = = 7)
def fonk4(b1):
    b11 = set()
    for t in itertools.count(1):
        for k in range(0, t):
            print("Running function {} on input {} for {} steps.".format(b1, k, t))
            b9 = b1(k, steps=t)
            if b9 is not None:
                for inv, b12 in b11:
                    if inv != k and b12 = = b9:
                        print("This function returns {} on inputs {} and {}!".format(b9, inv, k))
                        return True
                print("Recording that {}({}) = {}.".format(b1, k, b9))
                b11.add((k, b9))
            else:
                print("{}({}) did not terminate in {} steps.".format(b1, k, t))
def fonk5(b1):
    return complib.dovetailing_on_pairs(b1, lambda i, b13, j, oj, t: i != j and b13 = = oj)
if b14 = = '__main__':
    fonk1()