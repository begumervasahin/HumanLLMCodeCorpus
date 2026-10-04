
import urllib.request
import re
from collections import OrderedDict
from bs4 import BeautifulSoup
import networkx as nx
import itertools as IT
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
class Node:
    def __init__(self, val, left=None, right=None, parent=None, count=1):
        self.value = val
        self.left = left
        self.right = right
        self.parent = parent
        self.count = count
    def __len__(self):
        return self.count
    def __iter__(self):
        if self.left:
            for elem in self.left:
                yield elem
        yield (self.value, self.count)
        if self.right:
            for elem in self.right:
                yield elem
    def replace(self, val, left_child, right_child):
        self.value = val
        self.left = left_child
        self.right = right_child
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self
    def find_successor(self):
        if self.right:
            return self.right.find_min()
        elif self.parent:
            if self == self.parent.left:
                return self.parent
            self.parent.right = None
            successor = self.parent.find_successor()
            self.parent.right = self
            return successor
        return None
    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current
    def splice_out(self):
        if not (self.right or self.left):
            if self.parent:
                if self == self.parent.left:
                    self.parent.left = None
                else:
                    self.parent.right = None
        elif self.left:
            if self.parent:
                if self == self.parent.left:
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
            self.left.parent = self.parent
        else:
            if self.parent:
                if self == self.parent.left:
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
            self.right.parent = self.parent
    def edge_list(self, counter=IT.count().__next__):
        for node in (self.left, self.right):
            if node:
                yield (self.value, node.value)
        for node in (self.left, self.right):
            if node:
                yield from node.edge_list(counter)
    def in_order(self, func):
        if self.left:
            self.left.in_order(func)
        func(self)
        if self.right:
            self.right.in_order(func)
class BST:
    def __init__(self, url=None, file=None):
        self.root = None
        self.size = 0
        self.cd = dict()
        if url:
            self._build_tree_from_url(url)
        if file:
            self._build_tree_from_file(file)
    def _build_tree_from_url(self, url):
        text = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(text, 'html.parser')
        [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
        visible_text = soup.getText()
        word_list = re.sub("[^\w]", " ", visible_text).split()
        for word in word_list:
            self.put(word)
    def _build_tree_from_file(self, file):
        with open(file, "r") as f:
            data = f.read()
            word_list = re.sub("[^\w]", " ", data).split()
            for word in word_list:
                self.put(word)
    def __len__(self):
        return self.size
    def __iter__(self):
        return iter(self.root)
    def put(self, val):
        node = self.get(val)
        if node:
            self._update_count(node)
        else:
            self._insert_new_node(val)
    def _update_count(self, node):
        if self.cd[node.count] == 1:
            self.cd.pop(node.count)
        else:
            self.cd[node.count] -= 1
        node.count += 1
        self.cd[node.count] = self.cd.get(node.count, 0) + 1
    def _insert_new_node(self, val):
        if self.root:
            self._put(val, self.root)
        else:
            self.root = Node(val)
            self.cd[self.root.count] = self.cd.get(self.root.count, 0) + 1
        self.size += 1
    def _put(self, val, current_node):
        if val < current_node.value:
            if current_node.left:
                self._put(val, current_node.left)
            else:
                current_node.left = Node(val, parent=current_node)
                self.cd[current_node.left.count] = self.cd.get(current_node.left.count, 0) + 1
        else:
            if current_node.right:
                self._put(val, current_node.right)
            else:
                current_node.right = Node(val, parent=current_node)
                self.cd[current_node.right.count] = self.cd.get(current_node.right.count, 0) + 1
    def get(self, val):
        if self.root:
            return self._get(val, self.root)
        return None
    def _get(self, val, current_node):
        if not current_node:
            return None
        elif current_node.value == val:
            return current_node
        elif val < current_node.value:
            return self._get(val, current_node.left)
        else:
            return self._get(val, current_node.right)
    def __contains__(self, val):
        return self.get(val) is not None
    def delete(self, val):
        if self.size > 1:
            node_to_remove = self.get(val)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
                self.cd[node_to_remove.count] -= 1
            else:
                raise KeyError("Error, Word not in tree")
        elif self.size == 1 and self.root.value == val:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Error, Word not in tree")
    def remove(self, current_node):
        if not (current_node.left or current_node.right):
            if current_node == current_node.parent.left:
                current_node.parent.left = None
            else:
                current_node.parent.right = None
        elif current_node.left and current_node.right:
            successor = current_node.find_successor()
            successor.splice_out()
            current_node.value = successor.value
        else:
            child = current_node.left if current_node.left else current_node.right
            if current_node == current_node.parent.left:
                current_node.parent.left = child
            else:
                current_node.parent.right = child
            child.parent = current_node.parent
    def sorted_by_count(self):
        sorted_list = [None] * self.size
        count_dict = OrderedDict(self.cd)
        index_dict = OrderedDict()
        cumulative_index = -1
        for count, freq in count_dict.items():
            index_dict[count] = freq + cumulative_index
            cumulative_index += freq
        for value, count in self:
            sorted_list[index_dict[count]] = (value, count)
            index_dict[count] -= 1
        return sorted_list[::-1]
    def plot(self):
        labels = {node.value: node.value for node in self.root.edge_list()}
        graph = nx.Graph(self.root.edge_list())
        pos = graphviz_layout(graph, prog='dot')
        nx.draw(graph, pos)
        nx.draw_networkx_labels(graph, pos, labels)
        plt.show()