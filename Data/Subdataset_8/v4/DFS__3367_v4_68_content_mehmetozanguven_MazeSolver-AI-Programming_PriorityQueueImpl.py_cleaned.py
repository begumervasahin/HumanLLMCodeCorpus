class PriorityQueue:
    def __init__(self, use_heuristic=False):
        self.items = []
        self.use_heuristic = use_heuristic
    def is_empty(self):
        return len(self.items) == 0
    def sort_by_cost(self, item):
        return item.cost
    def sort_by_heuristic(self, item):
        return item.heuristic_function
    def enqueue(self, item):
        self.items.append(item)
        if self.use_heuristic:
            self.items.sort(key=self.sort_by_heuristic)
        else:
            self.items.sort(key=self.sort_by_cost)
    def dequeue(self):
        return self.items.pop(0)
    def to_string(self):
        return ' '.join(str(each_item) for each_item in self.items)
    def contains_element(self, element):
        for each_element in self.items:
            if each_element == element:
                return True
        return False
if __name__ == "__main__":
    class Item:
        def __init__(self, cost, heuristic_function):
            self.cost = cost
            self.heuristic_function = heuristic_function
        def __str__(self):
            return f"Item(cost={self.cost}, heuristic_function={self.heuristic_function})"
    priority_queue = PriorityQueue(use_heuristic=True)
    priority_queue.enqueue(Item(10, 5))
    priority_queue.enqueue(Item(8, 3))
    priority_queue.enqueue(Item(12, 7))
    print(priority_queue.to_string())
    dequeued_item = priority_queue.dequeue()
    print("Dequeued item:", dequeued_item)
    print("Queue contains element with cost 5:", priority_queue.contains_element(5))