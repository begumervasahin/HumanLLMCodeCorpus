from vartree import binarySearchTree
from peekable import Peekable, peek
from newsplit import new_split_iter
from infixtotree import to_expr_tree, define_func
def fonk1(expr):
    """Define a new function, or evaluate an expression
    If the first word in the line "deffn", it should appear as
          deffn <function name> ( <parameters> ) = <function b2>
          a VarTree will associate the function name with
            a list of parameters (at least one, maybe more)
            and a tree representing the function b2
    otherwise the input line is evaluated in an expression tree
    """
    b1 = Peekable(new_split_iter(expr))
    if peek(b1) == "deffn":
        name, parms, b2 = define_func(b1)
        b3.assign(name, (parms, b2))
    else:
        print(expr,':',to_expr_tree(expr).fonk1(b4, b3))
b3 = binarySearchTree()
b4 = binarySearchTree()