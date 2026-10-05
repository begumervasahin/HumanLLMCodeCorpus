from linkedlist import LinkedList
from vartree import BinarySearchTree
from infixtotree import to_expr_tree
var_tree = BinarySearchTree()
def eval_postfix(postfix_expr):
    stack = LinkedList()
    for token in postfix_expr:
        if token[0].isdigit() or token[0].isalpha():
            stack.push(token)
        elif token == '=':
            top = stack.pop()
            bottom = stack.pop()
            if top[0].isalpha():
                top = var_tree.lookup(top)
            var_tree.assign(bottom, top)
            stack.push(bottom)
        else:
            top = stack.pop()
            bottom = stack.pop()
            if top[0].isalpha():
                top = var_tree.lookup(top)
            if bottom[0].isalpha():
                bottom = var_tree.lookup(bottom)
            temp = eval(str(bottom) + token + str(top))
            stack.push(str(temp))
    if stack.top()[0].isdigit():
        return float(stack.top())
    return var_tree.lookup(stack.top())