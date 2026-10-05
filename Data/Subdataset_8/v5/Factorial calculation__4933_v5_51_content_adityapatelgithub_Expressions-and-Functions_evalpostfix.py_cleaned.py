from linkedlist import LinkedList
from vartree import BinarySearchTree
from infixtotree import to_expr_tree
variable_tree = BinarySearchTree()
def evaluate_postfix_expression(postfix_expression):
    stack = LinkedList()
    for token in postfix_expression:
        if token[0].isdigit() or token[0].isalpha():
            stack.push(token)
        elif token == '=':
            top = stack.pop()
            bottom = stack.pop()
            if top[0].isalpha():
                top = variable_tree.lookup(top)
            variable_tree.assign(bottom, top)
            stack.push(bottom)
        else:
            top = stack.pop()
            bottom = stack.pop()
            if top[0].isalpha():
                top = variable_tree.lookup(top)
            if bottom[0].isalpha():
                bottom = variable_tree.lookup(bottom)
            temp = eval(str(bottom) + token + str(top))
            stack.push(str(temp))
    if stack.top()[0].isdigit():
        return float(stack.top())
    return variable_tree.lookup(stack.top())