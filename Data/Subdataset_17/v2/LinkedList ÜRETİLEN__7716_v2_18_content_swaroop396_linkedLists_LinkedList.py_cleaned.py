class Node:
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link
    def update_data(self, data):
        self.data = data
    def set_link(self, node):
        self.link = node
    def get_data(self):
        return self.data
    def get_next_node(self):
        return self.link
class LinkedList:
    def __init__(self):
        self.head = None
    def add_to_start(self, data):
        new_node = Node(data)
        new_node.set_link(self.head)
        self.head = new_node
    def add_to_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.get_next_node():
            current = current.get_next_node()
        current.set_link(new_node)
    def display(self):
        current = self.head
        if not current:
            print("Empty List!!!")
            return
        while current:
            print(current.get_data(), end=" ")
            current = current.get_next_node()
            if current:
                print("-->", end=" ")
        print()
    def length(self):
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.get_next_node()
        return size
    def index(self, data):
        current = self.head
        position = 0
        while current:
            if current.get_data() == data:
                return position
            current = current.get_next_node()
            position += 1
        return -1
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next_node()
        if found:
            if previous is None:
                self.head = current.get_next_node()
            else:
                previous.set_link(current.get_next_node())
        return found
    def get_max(self):
        if not self.head:
            return None
        current = self.head
        largest = current.get_data()
        while current:
            if current.get_data() > largest:
                largest = current.get_data()
            current = current.get_next_node()
        return largest
    def get_min(self):
        if not self.head:
            return None
        current = self.head
        smallest = current.get_data()
        while current:
            if current.get_data() < smallest:
                smallest = current.get_data()
            current = current.get_next_node()
        return smallest
    def push(self, data):
        self.add_to_end(data)
        return True
    def pop(self):
        if not self.head:
            return None
        current = self.head
        previous = None
        while current.get_next_node():
            previous = current
            current = current.get_next_node()
        if previous:
            previous.set_link(None)
        else:
            self.head = None
        return current.get_data()
    def at_index(self, position):
        if position < 0 or not self.head:
            return None
        current = self.head
        for _ in range(position):
            if not current.get_next_node():
                return None
            current = current.get_next_node()
        return current.get_data()
    def copy(self):
        new_list = LinkedList()
        current = self.head
        while current:
            new_list.add_to_end(current.get_data())
            current = current.get_next_node()
        return new_list
    def clear(self):
        self.head = None
        return True
    def remove_at_position(self, position):
        data = self.at_index(position)
        if data is not None:
            self.remove(data)
        return data
    def to_string(self, separator=""):
        current = self.head
        result = ""
        while current:
            result += str(current.get_data())
            current = current.get_next_node()
            if current:
                result += separator
        return result
    def count(self, element):
        current = self.head
        count = 0
        while current:
            if current.get_data() == element:
                count += 1
            current = current.get_next_node()
        return count
    def to_list(self):
        current = self.head
        result = []
        while current:
            result.append(current.get_data())
            current = current.get_next_node()
        return result
    def to_set(self):
        current = self.head
        result = set()
        while current:
            result.add(current.get_data())
            current = current.get_next_node()
        return result
    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.get_next_node()
            current.set_link(previous)
            previous = current
            current = next_node
        self.head = previous
    def sort(self):
        if not self.head or not self.head.get_next_node():
            return
        sorted_list = None
        current = self.head
        while current:
            next_node = current.get_next_node()
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list
    def sorted_insert(self, head, node):
        if not head or head.get_data() >= node.get_data():
            node.set_link(head)
            return node
        current = head
        while current.get_next_node() and current.get_next_node().get_data() < node.get_data():
            current = current.get_next_node()
        node.set_link(current.get_next_node())
        current.set_link(node)
        return head
    def sorted(self):
        new_list = self.copy()
        new_list.sort()
        return new_list
if __name__ == "__main__":
    my_list = LinkedList()
    my_list.add_to_start(5)
    my_list.add_to_start(4)
    my_list.add_to_start(3)
    my_list.add_to_start(2)
    my_list.add_to_start(1)
    my_list.display()
    my_list.add_to_end(12)
    my_list.add_to_end(13)
    my_list.add_to_end(3)
    my_list.display()
    print("Length:", my_list.length())
    print("Index of 3:", my_list.index(3))
    print("Element at index 5:", my_list.at_index(5))
    print("Removing 12:", my_list.remove(12))
    my_list.remove_at_position(2)
    my_list.display()
    print("Max:", my_list.get_max())
    print("Min:", my_list.get_min())
    print("Pushing 31:", my_list.push(31))
    my_list.display()
    print("Popping:", my_list.pop())
    my_list.display()
    my_list2 = my_list.copy()
    print("Copied list:")
    my_list2.display()
    my_list2.clear()
    print("Cleared copied list:")
    my_list2.display()
    print("List to string:", my_list.to_string(", "))
    print("Count of 3:", my_list.count(3))
    new_list = my_list.to_list()
    print("List:", new_list)
    new_set = my_list.to_set()
    print("Set:", new_set)
    my_list.reverse()
    print("Reversed list:")
    my_list.display()
    my_list3 = my_list.sorted()
    print("Sorted copy of list:")
    my_list3.display()
    my_list.sort()
    print("Sorted list:")
    my_list.display()