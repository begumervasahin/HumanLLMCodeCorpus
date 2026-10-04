import complib
import itertools
def display_graph(function, name):
    print(f"Graph of function {name}:")
    function.pp_graph()
def halt_in_one_step(function, name):
    result = complib.T3(function, 0, 1)
    print(f"Function {name}(0) halts in 1 step: {result}")
def display_function_graphs(function, name, start, end):
    print(f"Graph of function {name}:", function.graph(start, end))
def display_function_output(function, name, value):
    print(f"{name}({value}) = {function(value)}")
def sd1_1(f):
    for t in itertools.count(1):
        for k in range(t):
            print(f"Running function {f} on input {k} for {t} steps.")
            output = f(k, steps=t)
            if output is not None and output == 7:
                print("On this input it returns 7!")
                return True
def sd1_2(f):
    return complib.dovetailing(f, lambda i, o, t: o == 7)
def sd2_1(f):
    s = set()
    for t in itertools.count(1):
        for k in range(t):
            print(f"Running function {f} on input {k} for {t} steps.")
            output = f(k, steps=t)
            if output is not None:
                for inv, outv in s:
                    if inv != k and outv == output:
                        print(f"This function returns {output} on inputs {inv} and {k}!")
                        return True
                print(f"Recording that {f}({k}) = {output}.")
                s.add((k, output))
            else:
                print(f"{f}({k}) did not terminate in {t} steps.")
def sd2_2(f):
    return complib.dovetailing_on_pairs(f, lambda i, oi, j, oj, t: i != j and oi == oj)
def demonstrate_encoding_decoding():
    print("Encoding and decoding of pairs as natural numbers:")
    for i in range(10):
        p = complib.number2pair(i)
        n = complib.pair2number(*p)
        print(f"{i} -> {p} -> {n}")
def main():
    f = complib.Function.from_graph(name="f", graph={(0, 1, 3), (1, 7, 1)})
    g = complib.Function.from_graph(name="g", graph={(0, 5, 1)})
    display_graph(f, "f")
    display_graph(g, "g")
    display_graph(complib.K0, "K0")
    display_graph(complib.ident, "ident")
    display_graph(complib.undef, "undef")
    halt_in_one_step(f, "f")
    halt_in_one_step(g, "g")
    halt_in_one_step(complib.K0, "K0")
    halt_in_one_step(complib.ident, "ident")
    halt_in_one_step(complib.undef, "undef")
    display_function_graphs(f, "f", 0, 3)
    display_function_graphs(g, "g", 0, 3)
    display_function_graphs(complib.K0, "K0", 0, 3)
    display_function_graphs(complib.ident, "ident", 0, 3)
    display_function_graphs(complib.undef, "undef", 0, 3)
    display_function_output(f, "f", 0)
    display_function_output(g, "g", 0)
    display_function_output(complib.K0, "K0", 0)
    display_function_output(complib.ident, "ident", 0)
    print("undef(0) =", end=" ")
    complib.undef(0, on_undef="continue")
    sd1_1(f)
    sd1_2(f)
    sd1_1(complib.ident)
    sd1_2(complib.ident)
    k12_3_steps = complib.K(12, 3)
    sd2_1(k12_3_steps)
    sd2_2(k12_3_steps)
    demonstrate_encoding_decoding()
if __name__ == '__main__':
    main()