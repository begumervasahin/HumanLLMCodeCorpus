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
        if other and self.value == other:
            return True
        return False
    def __repr__(self):
        return str(self.value)
class Stack(list):
    def __init__(self, start, heuristic):
        super().__init__()
        self.append(Node(start, heuristic))
    def add_new(self, other, other_cost, other_father, heuristic):
        if other in Node.all_nodes:
            node = Node.all_nodes[other]
            other_cost = other_cost + other_father.accumulated_cost
            if other_cost < node.accumulated_cost:
                node.accumulated_cost = other_cost
                node.father = other_father
                self.binary_update(node)
            return
        self.binary_insert(Node(other, heuristic, other_father, other_cost))
    def binary_insert(self, elem):
        def added_cost(elem):
            return elem.heuristic_cost + elem.accumulated_cost
        if len(self):
            added_cost_val = added_cost(elem)
            begin, end = 0, len(self)
            split = (begin + end)
            while end - begin > 1:
                if added_cost_val >= added_cost(self[split]):
                    end = split
                else:
                    begin = split
                split = (begin + end)
            if added_cost_val > added_cost(self[begin]):
                self[begin:begin] = [elem]
            else:
                self[end:end] = [elem]
        else:
            self.append(elem)
    def binary_update(self, elem):
        if len(self):
            begin, end = 0, len(self)
            split = (begin + end)
            while end - begin > 1:
                if elem.value >= self[split].value:
                    end = split
                else:
                    begin = split
                split = (begin + end)
            if elem.value == self[begin].value:
                del self[begin]
                self.binary_insert(elem)
    def full_path(self, position, reverse):
        Node.all_nodes.clear()
        if reverse:
            return self.gen_full_path(position)
        return list(self.gen_full_path(position))[::-1]
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
        around = calc_possible(cur_position.value)
        for elem, cost in around:
            stack.add_new(elem, cost, cur_position, heuristic)
    raise TimeoutError("Time limit reached, you can manually change or remove it.")
def calc_possible(value):
    pass
def base_case(value):
    pass
def heuristic(value):
    pass
result = a(calc_possible, start='start_node', base_case=base_case, heuristic=heuristic, time_limit=10, reverse=False)
print(result)