if b1 = = '__main__':
    import complib
    import itertools
    b2 = complib.Function.from_graph(
        b3 = "b2",
        b4 = set([
            (0, 1, 3),
            (1, 7, 1)
        ])
    )
    b5 = complib.Function.from_graph(
        b3 = "b5",
        b4 = set([
            (0, 5, 1)
        ])
    )
    print("Graph of function b2:")
    b2.pp_graph()
    print("Graph of function b5:")
    b5.pp_graph()
    print("Graph of function K0:")
    complib.K0.pp_graph()
    print("Graph of function ident:")
    complib.ident.pp_graph()
    print("Graph of function undef:")
    complib.undef.pp_graph()
    print("Function b2(0) halts in 1 step:", complib.T3(b2, 0, 1))
    print("Function b5(0) halts in 1 step:", complib.T3(b5, 0, 1))
    print("Function K0(0) halts in 1 step:", complib.T3(complib.K0, 0, 1))
    print("Function ident(0) halts in 1 step:", complib.T3(complib.ident, 0, 1))
    print("Function undef(0) halts in 1 step:", complib.T3(complib.undef, 0, 1))
    print("Graph of function b2:", b2.b4(0, 3))
    print("Graph of function b5:", b5.b4(0, 3))
    print("Graph of function K0:", complib.K0.b4(0, 3))
    print("Graph of function ident:", complib.ident.b4(0, 3))
    print("Graph of function undef:", complib.undef.b4(0, 3))
    print("b2(0) =", b2(0))
    print("b5(0) =", b5(0))
    print("K0(0) =", complib.K0(0))
    print("ident(0) =", complib.ident(0))
    print("undef(0) =", b6 = " ")
    complib.undef(0, b7 = "continue")
    def fonk1(b2):
        for t in itertools.count(1):
            for k in range(0, t):
                print(b2"Running function {b2} on input {k} for {t} steps.")
                b8 = b2(k, steps=t)
                if b8 is not None and b8 = = 7:
                    print("On this input it returns 7!")
                    return True
    def fonk2(b2):
        return complib.dovetailing(b2, lambda i, b9, t: b9 = = 7)
    def fonk3(b2):
        b10 = set()
        for t in itertools.count(1):
            for k in range(0, t):
                print(b2"Running function {b2} on input {k} for {t} steps.")
                b8 = b2(k, steps=t)
                if b8 is not None:
                    for inv, b11 in b10:
                        if inv != k and b11 = = b8:
                            print(b2"This function returns {b8} on inputs {inv} and {k}!")
                            return True
                    print(b2"Recording that {b2}({k}) = {b8}.")
                    b10.add((k, b8))
                else:
                    print(b2"{b2}({k}) did not terminate in {t} steps.")
    def fonk4(b2):
        return complib.dovetailing_on_pairs(b2, lambda i, b12, j, oj, t: i != j and b12 = = oj)
    fonk1(b2)
    fonk2(b2)
    fonk1(complib.ident)
    fonk2(complib.ident)
    b13 = complib.K(12, 3)
    fonk3(b13)
    fonk4(b13)
    print("Encoding and decoding of pairs as natural numbers:")
    for i in range(10):
        b14 = complib.number2pair(i)
        b15 = complib.pair2number(*b14)
        print(i, "->", b14, "->", b15)