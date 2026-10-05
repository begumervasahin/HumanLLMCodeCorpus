import complib
import itertools
def main():
    f = complib.Function.from_graph(
        name="f",
        graph=set([(0, 1, 3), (1, 7, 1)])
    )
    g = complib.Function.from_graph(
        name="g",
        graph=set([(0, 5, 1)])
    )
    print_function_graphs(f, g)
    evaluate_and_check_termination(f, g)
    search_for_properties(f)
def print_function_graphs(*functions):
    for function in functions:
        print(f"Graph of function {function.name}:")
        function.pp_graph()
def evaluate_and_check_termination(*functions):
    for function in functions:
        print(f"Function {function.name}(0) halts in 1 step:", complib.T3(function, 0, 1))
def search_for_properties(*functions):
    for function in functions:
        print(f"Searching for properties in function {function.name}:")
        sd1_1_result = sd1_1(function)
        print(f"Property found by sd1_1: {sd1_1_result}")
        sd1_2_result = sd1_2(function)
        print(f"Property found by sd1_2: {sd1_2_result}")
        if isinstance(function, complib.Function):
            k12_3_steps = complib.K(12, 3)
            sd2_1_result = sd2_1(k12_3_steps)
            print(f"Property found by sd2_1: {sd2_1_result}")
            sd2_2_result = sd2_2(k12_3_steps)
            print(f"Property found by sd2_2: {sd2_2_result}")
def sd1_1(f):
    for t in itertools.count(1):
        for k in range(0, t):
            output = f(k, steps=t)
            if output is not None and output == 7:
                return True
def sd1_2(f):
    return complib.dovetailing(f, lambda i, o, t: o == 7)
def sd2_1(f):
    s = set()
    for t in itertools.count(1):
        for k in range(0, t):
            output = f(k, steps=t)
            if output is not None:
                for inv, outv in s:
                    if inv != k and outv == output:
                        return True
                s.add((k, output))
def sd2_2(f):
    return complib.dovetailing_on_pairs(f, lambda i, oi, j, oj, t: i != j and oi == oj)
if __name__ == '__main__':
    main()