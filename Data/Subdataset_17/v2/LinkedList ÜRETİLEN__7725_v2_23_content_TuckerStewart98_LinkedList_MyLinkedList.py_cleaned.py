class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next = next_node
    def get_data(self):
        return self.__data
    def get_next(self):
        return self.__next
    def set_next(self, next_node):
        self.__next = next_node
    def __str__(self):
        return str(self.__data)
class MyLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
    def size(self):
        return self.__size
    def add(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node
        self.__size += 1
    def get(self, index):
        if index >= self.__size or index < 0:
            raise IndexError('Index out of bounds')
        current_node = self.__head
        for _ in range(index):
            current_node = current_node.get_next()
        return current_node.get_data()
if __name__ == "__main__":
    linked_list = MyLinkedList()
    linked_list.add(1)
    linked_list.add(5)
    linked_list.add(-7)
    for i in range(linked_list.size()):
        print(linked_list.get(i))