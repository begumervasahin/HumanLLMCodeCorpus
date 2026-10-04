from linkedlist import LinkedList
from vartree import BinarySearchTree
from infixtotree import to_expr_tree
class VariableTree(BinarySearchTree):
    def assign(self, variable, value):
        self.insert(variable, value)
    def lookup(self, variable):
        node = self.search(variable)
        if node:
            return node.value
        raise ValueError(f"Variable '{variable}' not found in the tree")
varTree = VariableTree()
def eval_postfix(postfixExpr):
    stack = LinkedList()
    for token in postfixExpr:
        if token[0].isdigit() or token[0].isalpha():
            stack.push(token)
        elif token == '=':
            top = stack.pop()
            bottom = stack.pop()
            if top[0].isalpha():
                top = varTree.lookup(top)
            varTree.assign(bottom, top)
            stack.push(bottom)
        else:
            top = stack.pop()
            bottom = stack.pop()
            if top[0].isalpha():
                top = varTree.lookup(top)
            if bottom[0].isalpha():
                bottom = varTree.lookup(bottom)
            temp = eval(f"{bottom} {token} {top}")
            stack.push(str(temp))
    result = stack.top()
    if result[0].isdigit():
        return float(result)
    return varTree.lookup(result)
if __name__ == "__main__":
    postfix_expr = ['12', '3', '*', '5', '+', 'a', '=']
    result = eval_postfix(postfix_expr)
    print("Result:", result)