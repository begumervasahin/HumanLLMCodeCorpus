
from vartree import binarySearchTree
from peekable import Peekable, peek
from newsplit import new_split_iter
from infixtotree import to_expr_tree, define_func
functions = binarySearchTree()
variables = binarySearchTree()
def evaluate(expr):
    """
    Evaluate an expression or define a new function.
    If the expression begins with "deffn", it defines a new function.
    Otherwise, it evaluates the expression.
    Parameters:
        expr (str): The expression to evaluate or function definition.
    """
    iterator = Peekable(new_split_iter(expr))
    if peek(iterator) == "deffn":
        name, parms, body = define_func(iterator)
        functions.assign(name, (parms, body))
    else:
        print(expr, ':', to_expr_tree(expr).evaluate(variables, functions))
evaluate("deffn f(x, y) = x * y")
evaluate("f(3, 4)")
evaluate("2 + 3 * 4")
