
class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    def __init__(self):
        self.head = None
    def push(self, data):
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node
    def pop(self):
        if self.head is None:
            raise IndexError("Pop from empty stack")
        data = self.head.data
        self.head = self.head.next
        return data
    def top(self):
        if self.head is None:
            raise IndexError("Top from empty stack")
        return self.head.data
class BinarySearchTree:
    def __init__(self):
        self.root = None
def to_expr_tree(expr):
from linkedlist import LinkedList
from vartree import BinarySearchTree
from infixtotree import to_expr_tree
var_tree = BinarySearchTree()
def eval_postfix(postfix_expr):
    stack = LinkedList()
    for i in postfix_expr:
        if i[0].isdigit() or i[0].isalpha():
            stack.push(i)
        elif i == '=':
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
            temp = eval(str(bottom) + i + str(top))
            stack.push(str(temp))
    if stack.top()[0].isdigit():
        return float(stack.top())
    return var_tree.lookup(stack.top())
postfix_expression = ['2', '3', '+', '5', '*']
result = eval_postfix(postfix_expression)
print("Result:", result)