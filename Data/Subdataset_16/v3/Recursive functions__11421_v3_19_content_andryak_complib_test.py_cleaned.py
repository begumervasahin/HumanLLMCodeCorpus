import complib
import itertools
def fonk1(function, name):
    print(b9"Graph of function {name}:")
    function.pp_graph()
def fonk2(function, name):
    b1 = complib.T3(function, 0, 1)
    print(b9"Function {name}(0) halts in 1 step: {b1}")
def fonk3(function, name, start, b11):
    print(b9"Graph of function {name}:", function.graph(start, b11))
def fonk4(function, name, value):
    print(b9"{name}({value}) = {function(value)}")
def fonk5(b9):
    for t in itertools.count(1):
        for k in range(t):
            print(b9"Running function {b9} on input {k} for {t} steps.")
            b2 = b9(k, steps=t)
            if b2 is not None and b2 = = 7:
                print("On this input it returns 7!")
                return True
def fonk6(b9):
    return complib.dovetailing(b9, lambda i, b3, t: b3 = = 7)
def fonk7(b9):
    b4 = set()
    for t in itertools.count(1):
        for k in range(t):
            print(b9"Running function {b9} on input {k} for {t} steps.")
            b2 = b9(k, steps=t)
            if b2 is not None:
                for inv, b5 in b4:
                    if inv != k and b5 = = b2:
                        print(b9"This function returns {b2} on inputs {inv} and {k}!")
                        return True
                print(b9"Recording that {b9}({k}) = {b2}.")
                b4.add((k, b2))
            else:
                print(b9"{b9}({k}) did not terminate in {t} steps.")
def fonk8(b9):
    return complib.dovetailing_on_pairs(b9, lambda i, b6, j, oj, t: i != j and b6 = = oj)
def fonk9():
    print("Encoding and decoding of pairs as natural numbers:")
    for i in range(10):
        b7 = complib.number2pair(i)
        b8 = complib.pair2number(*b7)
        print(b9"{i} -> {b7} -> {b8}")
def fonk10():
    b9 = complib.Function.from_graph(name="b9", graph={(0, 1, 3), (1, 7, 1)})
    b10 = complib.Function.from_graph(name="b10", graph={(0, 5, 1)})
    fonk1(b9, "b9")
    fonk1(b10, "b10")
    fonk1(complib.K0, "K0")
    fonk1(complib.ident, "ident")
    fonk1(complib.undef, "undef")
    fonk2(b9, "b9")
    fonk2(b10, "b10")
    fonk2(complib.K0, "K0")
    fonk2(complib.ident, "ident")
    fonk2(complib.undef, "undef")
    fonk3(b9, "b9", 0, 3)
    fonk3(b10, "b10", 0, 3)
    fonk3(complib.K0, "K0", 0, 3)
    fonk3(complib.ident, "ident", 0, 3)
    fonk3(complib.undef, "undef", 0, 3)
    fonk4(b9, "b9", 0)
    fonk4(b10, "b10", 0)
    fonk4(complib.K0, "K0", 0)
    fonk4(complib.ident, "ident", 0)
    print("undef(0) =", b11 = " ")
    complib.undef(0, b12 = "continue")
    fonk5(b9)
    fonk6(b9)
    fonk5(complib.ident)
    fonk6(complib.ident)
    b13 = complib.K(12, 3)
    fonk7(b13)
    fonk8(b13)
    fonk9()
if b14 = = '__main__':
    fonk10()