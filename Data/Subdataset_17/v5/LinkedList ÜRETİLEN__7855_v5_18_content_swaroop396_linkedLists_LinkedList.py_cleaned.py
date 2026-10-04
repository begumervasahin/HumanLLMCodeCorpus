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
        temp_node = Node(data)
        temp_node.set_link(self.head)
        self.head = temp_node
    def add_to_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        current = self.head
        while current.get_next_node():
            current = current.get_next_node()
        current.set_link(Node(data))
    def display(self):
        if self.head is None:
            print("Empty List!!!")
            return
        current = self.head
        while current:
            print(str(current.get_data()), end=" --> " if current.get_next_node() else "")
            current = current.get_next_node()
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
            position += 1
            current = current.get_next_node()
        return -1
    def remove(self, data):
        current = self.head
        previous = None
        while current:
            if current.get_data() == data:
                if previous is None:
                    self.head = current.get_next_node()
                else:
                    previous.set_link(current.get_next_node())
                return True
            previous = current
            current = current.get_next_node()
        return False
    def get_max(self):
        if self.head is None:
            return None
        current = self.head
        max_data = current.get_data()
        while current:
            if current.get_data() > max_data:
                max_data = current.get_data()
            current = current.get_next_node()
        return max_data
    def get_min(self):
        if self.head is None:
            return None
        current = self.head
        min_data = current.get_data()
        while current:
            if current.get_data() < min_data:
                min_data = current.get_data()
            current = current.get_next_node()
        return min_data
    def push(self, data):
        self.add_to_end(data)
    def pop(self):
        if self.head is None:
            return None
        current = self.head
        previous = None
        while current.get_next_node():
            previous = current
            current = current.get_next_node()
        if previous is None:
            self.head = None
        else:
            previous.set_link(None)
        return current.get_data()
    def at_index(self, position):
        current = self.head
        pos = 0
        while current and pos < position:
            current = current.get_next_node()
            pos += 1
        if current is None:
            raise IndexError("Index out of range")
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
    def remove_position(self, position):
        data = self.at_index(position)
        self.remove(data)
        return data
    def to_string(self, separator=""):
        current = self.head
        result = []
        while current:
            result.append(str(current.get_data()))
            current = current.get_next_node()
        return separator.join(result)
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
        current = self.head
        previous = None
        while current:
            next_node = current.get_next_node()
            current.set_link(previous)
            previous = current
            current = next_node
        self.head = previous
    def sort(self):
        if self.head is None:
            return
        current = self.head
        while current:
            smallest = current
            next_node = current.get_next_node()
            while next_node:
                if next_node.get_data() < smallest.get_data():
                    smallest = next_node
                next_node = next_node.get_next_node()
            current_data = current.get_data()
            current.update_data(smallest.get_data())
            smallest.update_data(current_data)
            current = current.get_next_node()
    def sorted(self):
        temp_list = self.to_list()
        temp_list.sort()
        sorted_list = LinkedList()
        for data in temp_list:
            sorted_list.add_to_end(data)
        return sorted_list
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
    print("Remove 12:", my_list.remove(12))
    my_list.remove_position(2)
    my_list.display()
    print("Max:", my_list.get_max())
    print("Min:", my_list.get_min())
    my_list.push(31)
    my_list.display()
    print("Pop:", my_list.pop())
    my_list.display()
    my_list2 = my_list.copy()
    my_list2.display()
    my_list2.clear()
    my_list2.display()
    print("To string:", my_list.to_string(","))
    print("Count of 3:", my_list.count(3))
    new_list = my_list.to_list()
    print("To list:", new_list)
    new_set = my_list.to_set()
    print("To set:", new_set)
    my_list.reverse()
    my_list.display()
    my_list3 = my_list.sorted()
    my_list3.display()
    my_list.sort()
    my_list.display()