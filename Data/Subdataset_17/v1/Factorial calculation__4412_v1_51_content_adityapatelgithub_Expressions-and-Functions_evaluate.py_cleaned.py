from vartree import binarySearchTree
from peekable import Peekable, peek
from newsplit import new_split_iter
from infixtotree import to_expr_tree, define_func
def evaluate(expr):
    """
    Define a new function or evaluate an expression.
    If the first word in the line is "deffn", it should appear as:
          deffn <function name> ( <parameters> ) = <function body>
    A VarTree will associate the function name with:
            a list of parameters (at least one, maybe more)
            and a tree representing the function body.
    Otherwise, the input line is evaluated in an expression tree.
    :param expr: Expression to evaluate or define as a function
    """
    iterator = Peekable(new_split_iter(expr))
    if peek(iterator) == "deffn":
        name, params, body = define_func(iterator)
        functions.assign(name, (params, body))
    else:
        result = to_expr_tree(expr).evaluate(variables, functions)
        print(f"{expr} : {result}")
functions = binarySearchTree()
variables = binarySearchTree()
if __name__ == "__main__":
    evaluate("deffn add (x, y) = x + y")
    evaluate("add(3, 4)")