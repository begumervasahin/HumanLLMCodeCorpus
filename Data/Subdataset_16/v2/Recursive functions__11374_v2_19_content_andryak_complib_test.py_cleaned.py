import complib
import itertools
def fonk1():
    b1 = complib.Function.from_graph(
        b2 = "b1",
        b3 = {(0, 1, 3), (1, 7, 1)}
    )
    b4 = complib.Function.from_graph(
        b2 = "b4",
        b3 = {(0, 5, 1)}
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
    print(b1"b1(0) = {b1(0)}")
    print(b1"b4(0) = {b4(0)}")
    print(b1"K0(0) = {complib.K0(0)}")
    print(b1"ident(0) = {complib.ident(0)}")
    print("undef(0) =", b5 = " ")
    complib.undef(0, b6 = "continue")
    def fonk2(b1):
        for t in itertools.count(1):
            for k in range(t):
                print(b1"Running function {b1} on input {k} for {t} steps.")
                b7 = b1(k, steps=t)
                if b7 is not None and b7 = = 7:
                    print("On this input it returns 7!")
                    return True
    def fonk3(b1):
        return complib.dovetailing(b1, lambda i, b8, t: b8 = = 7)
    def fonk4(b1):
        b9 = set()
        for t in itertools.count(1):
            for k in range(t):
                print(b1"Running function {b1} on input {k} for {t} steps.")
                b7 = b1(k, steps=t)
                if b7 is not None:
                    for inv, b10 in b9:
                        if inv != k and b10 = = b7:
                            print(b1"This function returns {b7} on inputs {inv} and {k}!")
                            return True
                    print(b1"Recording that {b1}({k}) = {b7}.")
                    b9.add((k, b7))
                else:
                    print(b1"{b1}({k}) did not terminate in {t} steps.")
    def fonk5(b1):
        return complib.dovetailing_on_pairs(b1, lambda i, b11, j, oj, t: i != j and b11 = = oj)
    fonk2(b1)
    fonk3(b1)
    fonk2(complib.ident)
    fonk3(complib.ident)
    b12 = complib.K(12, 3)
    fonk4(b12)
    fonk5(b12)
    print("Encoding and decoding of pairs as natural numbers:")
    for i in range(10):
        b13 = complib.number2pair(i)
        b14 = complib.pair2number(*b13)
        print(b1"{i} -> {b13} -> {b14}")
if b15 = = '__main__':
    fonk1()