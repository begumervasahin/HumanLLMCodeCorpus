class Node:
    def __init__(self, val=None):
        self.val = val
        self.nextval = None
class LinkedList:
    def __init__(self):
        self.headval = None
    def add_end(self, end_data):
        new_node = Node(end_data)
        if self.headval is None:
            self.headval = new_node
            return
        last = self.headval
        while last.nextval:
            last = last.nextval
        last.nextval = new_node
    def remove_node(self, key):
        current = self.headval
        previous = None
        while current and current.val != key:
            previous = current
            current = current.nextval
        if current is None:
            return
        if previous is None:
            self.headval = current.nextval
        else:
            previous.nextval = current.nextval
        current = None
    def print_list(self):
        current = self.headval
        while current:
            print(current.val, end=' -> ')
            current = current.nextval
        print('None')
def node_gen(lst):
    if not isinstance(lst, list):
        print("Please pass a list to generate nodes from the list items.")
        return
    for i in range(1, len(lst)):
        print(f"d{i + 1} = Node('{lst[i]}')")
def next_gen(lst):
    if not isinstance(lst, list):
        print("Please pass a list to generate code for linking nodes.")
        return
    for i in range(1, len(lst)):
        print(f"d{i}.nextval = d{i + 1}")
if __name__ == "__main__":
    lst = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_list = LinkedList()
    day_list.headval = Node(lst[0])
    d2 = Node('Tuesday')
    d3 = Node('Wednesday')
    d4 = Node('Thursday')
    d5 = Node('Friday')
    d6 = Node('Saturday')
    d7 = Node('Sunday')
    day_list.headval.nextval = d2
    d2.nextval = d3
    d3.nextval = d4
    d4.nextval = d5
    d5.nextval = d6
    d6.nextval = d7
    print("Initial list:")
    day_list.print_list()
    print("*" * 40)
    day_list.add_end("Frargsday")
    print("List after adding 'Frargsday':")
    day_list.print_list()
    print("*" * 40)
    day_list.remove_node("Frargsday")
    print("List after removing 'Frargsday':")
    day_list.print_list()
    print("*" * 40)
    print("Generated node creation code:")
    node_gen(lst)
    print("*" * 40)
    print("Generated node linking code:")
    next_gen(lst)