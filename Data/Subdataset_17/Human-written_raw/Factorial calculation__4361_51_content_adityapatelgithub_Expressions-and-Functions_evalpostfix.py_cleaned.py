from linkedlist import LinkedList
from vartree import binarySearchTree
from infixtotree import to_expr_tree
varTree = binarySearchTree()
def eval_postfix(postfixExpr):
    stack = LinkedList()
    for i in postfixExpr:
        if(i[0].isdigit() or i[0].isalpha()):
            stack.push(i)
        elif(i == '='):
            top = stack.pop()
            bottom = stack.pop()
            if(top[0].isalpha()):
                top = varTree.lookup(top)
            varTree.assign(bottom,top)
            stack.push(bottom)
        else:
            top = stack.pop()
            bottom = stack.pop()
            if(top[0].isalpha()):
                top = varTree.lookup(top)
            if(bottom[0].isalpha()):
                bottom = varTree.lookup(bottom)
            temp = eval(str(bottom) + i + str(top))
            stack.push(str(temp))
    if(stack.top()[0].isdigit()):
        return float(stack.top())
    return varTree.lookup(stack.top())