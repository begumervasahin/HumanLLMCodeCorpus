
from vartree import binarySearchTree
from peekable import Peekable, peek
from newsplit import new_split_iter
from infixtotree import to_expr_tree, define_func
functions = binarySearchTree()
variables = binarySearchTree()
def evaluate(expr):
    expr_iter = Peekable(new_split_iter(expr))
    if peek(expr_iter) == "deffn":
        name, parameters, body = define_func(expr_iter)
        functions.assign(name, (parameters, body))
    else:
        result = to_expr_tree(expr).evaluate(variables, functions)
        print(f"{expr} : {result}")
evaluate("deffn f(x, y) = x * y")
evaluate("f(3, 4)")
evaluate("2 + 3 * 4")
