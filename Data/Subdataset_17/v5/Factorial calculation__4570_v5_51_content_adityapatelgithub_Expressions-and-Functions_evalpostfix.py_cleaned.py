from linkedlist import LinkedList
from vartree import binarySearchTree
from infixtotree import to_expr_tree
var_tree = binarySearchTree()
def eval_postfix(postfix_expr):
    stack = LinkedList()
    for token in postfix_expr:
        if token[0].isdigit() or token[0].isalpha():
            stack.push(token)
        elif token == '=':
            handle_assignment(stack)
        else:
            handle_operator(stack, token)
    return get_final_result(stack)
def handle_assignment(stack):
    top = stack.pop()
    bottom = stack.pop()
    if top[0].isalpha():
        top = var_tree.lookup(top)
    var_tree.assign(bottom, top)
    stack.push(bottom)
def handle_operator(stack, operator):
    top = stack.pop()
    bottom = stack.pop()
    if top[0].isalpha():
        top = var_tree.lookup(top)
    if bottom[0].isalpha():
        bottom = var_tree.lookup(bottom)
    result = eval(f"{bottom} {operator} {top}")
    stack.push(str(result))
def get_final_result(stack):
    final_result = stack.top()
    if final_result[0].isdigit():
        return float(final_result)
    return var_tree.lookup(final_result)
if __name__ == "__main__":
    postfix_expr = ['12', '3', '*', '5', '+', 'a', '=']
    result = eval_postfix(postfix_expr)
    print("Result:", result)