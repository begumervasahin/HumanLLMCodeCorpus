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
            node = Node.all_nodes[value]
            cost = cost + father.accumulated_cost
            if cost < node.accumulated_cost:
                node.accumulated_cost = cost
                node.father = father
                self.binary_update(node)
            return
        self.binary_insert(Node(value, heuristic, father, cost))
    def binary_insert(self, elem):
        def added_cost(elem):
            return elem.heuristic_cost + elem.accumulated_cost
        total_cost = added_cost(elem)
        idx = len(self)
        while idx > 0 and added_cost(self[idx - 1]) > total_cost:
            idx -= 1
        self.insert(idx, elem)
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