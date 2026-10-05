from time import time
class Node:
    all_nodes = {}
    def __init__(self, value, heuristic_func, father=None, path_cost=1):
        self.value = value
        self.heuristic_cost = 0 if not heuristic_func else heuristic_func(self.value)
        self.accumulated_cost = father.accumulated_cost + path_cost if father else 0
        self.father = father
        Node.all_nodes[self.value] = self
    def __eq__(self, other):
        return isinstance(other, Node) and self.value == other.value
    def __repr__(self):
        return str(self.value)
class Stack(list):
    def __init__(self, start, heuristic):
        super().__init__([Node(start, heuristic)])
    def add_new(self, value, cost, father, heuristic):
        if value in Node.all_nodes:
            self.update_existing_node(value, cost, father)
            return
        self.insert_new_node(value, cost, father, heuristic)
    def update_existing_node(self, value, cost, father):
        node = Node.all_nodes[value]
        cost = cost + father.accumulated_cost
        if cost < node.accumulated_cost:
            node.accumulated_cost = cost
            node.father = father
            self.binary_update(node)
    def insert_new_node(self, value, cost, father, heuristic):
        self.binary_insert(Node(value, heuristic, father, cost))
    def binary_insert(self, elem):
        total_cost = elem.heuristic_cost + elem.accumulated_cost
        idx = len(self)
        while idx > 0 and self.is_bigger_than_total_cost(idx, total_cost):
            idx -= 1
        self.insert(idx, elem)
    def is_bigger_than_total_cost(self, idx, total_cost):
        return self.added_cost(self[idx - 1]) > total_cost
    def added_cost(self, elem):
        return elem.heuristic_cost + elem.accumulated_cost
    def binary_update(self, elem):
        idx = self.index(elem)
        while idx > 0 and elem.value < self[idx - 1].value:
            idx -= 1
        if idx != self.index(elem):
            self.pop(self.index(elem))
            self.binary_insert(elem)
    def full_path(self, position, reverse):
        Node.all_nodes.clear()
        return list(self.gen_full_path(position))[::-1] if reverse else list(self.gen_full_path(position))
    def gen_full_path(self, position):
        while position is not None:
            yield position.value
            position = position.father
def a(calc_possible, start, base_case, heuristic=None, time_limit=0, reverse=False):
    time_limit = float('inf') if time_limit == 0 else time_limit
    start_time = time()
    stack = Stack(start, heuristic)
    while time() < start_time + time_limit:
        if not stack:
            return False
        cur_position = stack.pop()
        if base_case(cur_position.value):
            return stack.full_path(cur_position, reverse)
        for elem, cost in calc_possible(cur_position.value):
            stack.add_new(elem, cost, cur_position, heuristic)
    raise TimeoutError("Time limit reached, you can manually change or remove it.")