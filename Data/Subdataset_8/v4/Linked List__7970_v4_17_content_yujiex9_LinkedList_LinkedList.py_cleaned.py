class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
    def __eq__(self, other):
        return self.value == other.value
class LinkedList:
    def __init__(self):
        self.head = None
    def __contains__(self, node):
        found = False
        if self.head:
            cursor = self.head
            while cursor:
                if cursor == node:
                    found = True
                    break
                cursor = cursor.next_node
        return found
    def __len__(self):
        count = 0
        if self.head:
            cursor = self.head
            while cursor:
                count += 1
                cursor = cursor.next_node
        return count
    def append(self, node):
        if not self.head:
            self.head = node
            return
        cursor = self.head
        while cursor.next_node:
            cursor = cursor.next_node
        cursor.next_node = node
    def insert(self, flag_node, node):
        if self.head == flag_node:
            node.next_node = self.head
            self.head = node
        else:
            prev_node = self.head
            while prev_node.next_node:
                if prev_node.next_node == flag_node:
                    break
                prev_node = prev_node.next_node
            node.next_node = prev_node.next_node
            prev_node.next_node = node
    def delete(self, node):
        if self.head:
            if self.head.value == node.value:
                self.head = self.head.next_node
                return
            prev_node = self.head
            while prev_node.next_node:
                if prev_node.next_node == node:
                    prev_node.next_node = node.next_node
                    break
                prev_node = prev_node.next_node
    def remove_duplicates(self):
        outer_cursor = self.head
        while outer_cursor:
            inner_cursor, prev_cursor = outer_cursor.next_node, outer_cursor
            while inner_cursor:
                if inner_cursor == outer_cursor:
                    prev_cursor.next_node = inner_cursor.next_node
                else:
                    prev_cursor = prev_cursor.next_node
                inner_cursor = inner_cursor.next_node
            outer_cursor = outer_cursor.next_node
    def reverse(self):
        if not self.head or not self.head.next_node:
            return
        prev_node, cursor = None, self.head
        while cursor:
            next_node = cursor.next_node
            cursor.next_node = prev_node
            prev_node = cursor
            cursor = next_node
        self.head = prev_node
    def print_list(self):
        cursor = self.head
        while cursor:
            print(cursor.value)
            cursor = cursor.next_node