from vartree import binarySearchTree
from peekable import Peekable, peek
from newsplit import new_split_iter
from infixtotree import to_expr_tree, define_func
def fonk1(expr):
    """
    Define a new function or evaluate an expression.
    If the first word in the line is "deffn", it should appear as:
          deffn <function name> ( <parameters> ) = <function b2>
    A VarTree will associate the function name with:
            a list of parameters (at least one, maybe more)
            and a tree representing the function b2.
    Otherwise, the input line is evaluated in an expression tree.
    :param expr: Expression to evaluate or define as a function
    """
    b1 = Peekable(new_split_iter(expr))
    if peek(b1) == "deffn":
        name, params, b2 = define_func(b1)
        b4.assign(name, (params, b2))
    else:
        b3 = to_expr_tree(expr).fonk1(b5, b4)
        print(f"{expr} : {b3}")
b4 = binarySearchTree()
b5 = binarySearchTree()
if b6 = = "__main__":
    fonk1("deffn add (x, y) = x + y")
    fonk1("add(3, 4)")