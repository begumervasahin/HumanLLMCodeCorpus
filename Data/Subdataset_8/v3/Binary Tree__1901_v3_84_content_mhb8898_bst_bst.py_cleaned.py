import urllib.request
import re
from bs4 import BeautifulSoup
from collections import OrderedDict
import itertools as it
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
class Node:
    def __init__(self, value, left=None, right=None, parent=None, count=1):
        self.value = value
        self.count = count
        self.parent = parent
        self.left = left
        self.right = right
    def __len__(self):
        return self.count
    def __iter__(self):
        if self:
            if self.left:
                yield from self.left
            yield (self.value, self.count)
            if self.right:
                yield from self.right
    def replace(self, value, left_child, right_child):
        self.value = value
        self.left = left_child
        self.right = right_child
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self
    def find_successor(self):
        successor = None
        if self.right:
            successor = self.right.find_min()
        else:
            if self.parent:
                if self.left:
                    successor = self.parent
                else:
                    self.parent.right = None
                    successor = self.parent.find_successor()
                    self.parent.right = self
        return successor
    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current
    def splice_out(self):
        if not (self.right or self.left):
            if self.parent:
                if self.parent.left == self:
                    self.parent.left = None
                else:
                    self.parent.right = None
        elif self.right or self.left:
            if self.left:
                if self.parent:
                    if self.parent.left == self:
                        self.parent.left = self.left
                    else:
                        self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.parent:
                    if self.parent.left == self:
                        self.parent.left = self.right
                    else:
                        self.parent.right = self.right
                self.right.parent = self.parent
    def edge_list(self, counter=it.count().__next__):
        for child in (self.left, self.right):
            if child:
                yield (self.value, child.value)
        for child in (self.left, self.right):
            if child:
                yield from child.edge_list(counter)
    def in_order_traversal(self, func):
        if self.left:
            self.left.in_order_traversal(func)
        func(self)
        if self.right:
            self.right.in_order_traversal(func)
class BST:
    def __init__(self, url=None, file=None):
        self.root = None
        self.size = 0
        self.count_dict = dict()
        if url:
            self._build_tree_from_url(url)
        if file:
            self._build_tree_from_file(file)
    def __len__(self):
        return self.size
    def __iter__(self):
        return self.root.__iter__()
    def insert(self, value):
        node = self.search(value)
        if node:
            if self.count_dict[node.count] == 1:
                self.count_dict.pop(node.count)
            else:
                self.count_dict[node.count] -= 1
            node.count += 1
            self.count_dict[node.count] = self.count_dict.get(node.count, 0) + 1
        else:
            if self.root:
                self._insert(value, self.root)
            else:
                self.root = Node(value)
                self.count_dict[self.root.count] = self.count_dict.get(self.root.count, 0) + 1
            self.size += 1
    def search(self, value):
        if self.root:
            result = self._search(value, self.root)
            if result:
                return result
        return None
    def delete(self, value):
        if self.size > 1:
            node_to_delete = self._search(value, self.root)
            if node_to_delete:
                self._remove(node_to_delete)
                self.size -= 1
                self.count_dict[node_to_delete.count] = self.count_dict.get(node_to_delete.count, 0) - 1
            else:
                raise KeyError("Error, Word not in tree")
        elif self.size == 1 and self.root.value == value:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Error, Word not in tree")
    def sorted_by_count(self):
        result_list = [None] * self.size
        count_dict = OrderedDict(self.count_dict)
        temp_dict = OrderedDict()
        count_sum = -1
        for count in count_dict:
            temp_dict[count] = count_dict[count] + count_sum
            count_sum += count_dict[count]
        for value, count in self:
            result_list[temp_dict[count]] = (value, count)
            temp_dict[count] -= 1
        return result_list[::-1]
    def plot(self):
        labels = {}
        for value1, value2 in self.root.edge_list():
            labels[value1] = value1
            labels[value2] = value2
        graph = nx.Graph(self.root.edge_list())
        position = graphviz_layout(graph, prog='dot')
        nx.draw(graph, position)
        nx.draw_networkx_labels(graph, position, labels)
        plt.show()
    def _build_tree_from_url(self, url):
        text = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(text, 'html.parser')
        [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
        visible_text = soup.getText()
        word_list = re.sub("[^\w]", " ", visible_text).split()
        for word in word_list:
            self.insert(word)
    def _build_tree_from_file(self, file):
        with open(file, "r") as f:
            data = f.read()
            word_list = re.sub("[^\w]", " ", data).split()
            for word in word_list:
                self.insert(word)
    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left:
                self._insert(value, current_node.left)
            else:
                current_node.left = Node(value, parent=current_node)
                self.count_dict[current_node.left.count] = self.count_dict.get(current_node.left.count, 0) + 1
        else:
            if current_node.right:
                self._insert(value, current_node.right)
            else:
                current_node.right = Node(value, parent=current_node)
                self.count_dict[current_node.right.count] = self.count_dict.get(current_node.right.count, 0) + 1
    def _search(self, value, current_node):
        if not current_node:
            return None
        elif current_node.value == value:
            return current_node
        elif value < current_node.value:
            return self._search(value, current_node.left)
        else:
            return self._search(value, current_node.right)
    def _remove(self, node):
        if not node.right and not node.left:
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.right and node.left:
            successor = node.find_successor()
            successor.splice_out()
            node.value = successor.value
        else:
            if node.left:
                if node.parent:
                    if node.parent.left == node:
                        node.left.parent = node.parent
                        node.parent.left = node.left
                    elif node.parent.right == node:
                        node.left.parent = node.parent
                        node.parent.right = node.left
                node.replace(node.left.value, node.left.left, node.left.right)
            else:
                if node.parent:
                    if node.parent.left == node:
                        node.right.parent = node.parent
                        node.parent.left = node.right
                    elif node.parent.right == node:
                        node.right.parent = node.parent
                        node.parent.right = node.right
                node.replace(node.right.value, node.right.left, node.right.right)
if __name__ == "__main__":
    pass