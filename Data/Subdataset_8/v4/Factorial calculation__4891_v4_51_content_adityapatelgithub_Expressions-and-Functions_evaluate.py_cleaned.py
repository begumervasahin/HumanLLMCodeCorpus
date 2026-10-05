
from vartree import binarySearchTree
from peekable import Peekable, peek
from newsplit import new_split_iter
from infixtotree import to_expr_tree, define_func
functions = binarySearchTree()
variables = binarySearchTree()
def evaluate(expr):
    """
    Define a new function or evaluate an expression.
    If the first word in the line is "deffn", it defines a new function in the format:
        deffn <function name> ( <parameters> ) = <function body>
    Otherwise, the input line is evaluated in an expression tree.
    Parameters:
        expr (str): The expression to evaluate or function definition.
    """
    iterator = Peekable(new_split_iter(expr))
    if peek(iterator) == "deffn":
        name, parameters, body = define_func(iterator)
        functions.assign(name, (parameters, body))
    else:
        result = to_expr_tree(expr).evaluate(variables, functions)
        print(expr, ':', result)
evaluate("deffn f(x, y) = x * y")
evaluate("f(3, 4)")
evaluate("2 + 3 * 4")
