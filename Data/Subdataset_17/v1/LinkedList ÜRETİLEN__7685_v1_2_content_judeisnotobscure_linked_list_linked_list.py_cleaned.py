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
        head_val = self.headval
        if head_val is not None:
            if head_val.val == key:
                self.headval = head_val.nextval
                head_val = None
                return
        while head_val is not None:
            if head_val.val == key:
                break
            prev = head_val
            head_val = head_val.nextval
        if head_val is None:
            return
        prev.nextval = head_val.nextval
        head_val = None
    def print_list(self):
        print_val = self.headval
        while print_val is not None:
            print(print_val.val)
            print_val = print_val.nextval
def node_gen(lst):
    try:
        for i in range(2, len(lst) + 1):
            print(f"d{i} = Node('{lst[i - 1]}')")
    except (TypeError, ValueError):
        print("Please pass a list to generate nodes from the list items.")
def next_gen(lst):
    dlist = []
    try:
        for i in range(2, len(lst) + 1):
            dlist.append(f"d{i}")
        for d in range(len(dlist) - 1):
            print(f"{dlist[d]}.nextval = {dlist[d + 1]}")
    except (TypeError, ValueError):
        print("Please pass a list to generate code for linking nodes.")
lst = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_list = LinkedList()
day_list.headval = Node("Monday")
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
day_list.add_end("frargsday")
print("List after adding 'frargsday':")
day_list.print_list()
print("*" * 40)
day_list.remove_node("frargsday")
print("List after removing 'frargsday':")
day_list.print_list()
print("*" * 40)
print("Generated node creation code:")
node_gen(lst)
print("*" * 40)
print("Generated node linking code:")
next_gen(lst)