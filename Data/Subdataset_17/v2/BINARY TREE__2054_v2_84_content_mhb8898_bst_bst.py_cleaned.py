
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
            yield from self.left
        yield (self.value, self.count)
        if self.right:
            yield from self.right
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
        else:
            current = self
            while current.parent and current == current.parent.right:
                current = current.parent
            return current.parent
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
        elif self.right or self.left:
            if self.left:
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
        if self.left:
            yield (self.value, self.left.value)
        if self.right:
            yield (self.value, self.right.value)
        if self.left:
            yield from self.left.edge_list(counter)
        if self.right:
            yield from self.right.edge_list(counter)
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
        self.count_dict = dict()
        if url:
            self._build_tree_from_url(url)
        if file:
            self._build_tree_from_file(file)
    def _build_tree_from_url(self, url):
        text = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(text, 'html.parser')
        [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
        visible_text = soup.get_text()
        words = re.sub(r"[^\w]", " ", visible_text).split()
        for word in words:
            self.put(word)
    def _build_tree_from_file(self, file):
        with open(file, "r") as f:
            data = f.read()
            words = re.sub(r"[^\w]", " ", data).split()
            for word in words:
                self.put(word)
    def __len__(self):
        return self.size
    def __iter__(self):
        return iter(self.root) if self.root else iter([])
    def put(self, val):
        node = self.get(val)
        if node:
            self._increment_count(node)
        else:
            if self.root:
                self._put(val, self.root)
            else:
                self.root = Node(val)
                self._increment_count(self.root)
            self.size += 1
    def _increment_count(self, node):
        if self.count_dict.get(node.count) == 1:
            del self.count_dict[node.count]
        else:
            self.count_dict[node.count] = self.count_dict.get(node.count, 0) - 1
        node.count += 1
        self.count_dict[node.count] = self.count_dict.get(node.count, 0) + 1
    def _put(self, val, current_node):
        if val < current_node.value:
            if current_node.left:
                self._put(val, current_node.left)
            else:
                current_node.left = Node(val, parent=current_node)
                self._increment_count(current_node.left)
        else:
            if current_node.right:
                self._put(val, current_node.right)
            else:
                current_node.right = Node(val, parent=current_node)
                self._increment_count(current_node.right)
    def get(self, val):
        if self.root:
            return self._get(val, self.root)
        return None
    def _get(self, val, current_node):
        if not current_node:
            return None
        if val == current_node.value:
            return current_node
        if val < current_node.value:
            return self._get(val, current_node.left)
        return self._get(val, current_node.right)
    def __contains__(self, val):
        return self.get(val) is not None
    def delete(self, val):
        if self.size > 1:
            node_to_remove = self.get(val)
            if node_to_remove:
                self._remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError(f"Error, '{val}' not in tree")
        elif self.size == 1 and self.root.value == val:
            self.root = None
            self.size -= 1
        else:
            raise KeyError(f"Error, '{val}' not in tree")
    def _remove(self, current_node):
        if not current_node.right and not current_node.left:
            if current_node.parent.left == current_node:
                current_node.parent.left = None
            else:
                current_node.parent.right = None
        elif current_node.right and current_node.left:
            successor = current_node.find_successor()
            successor.splice_out()
            current_node.value = successor.value
        else:
            if current_node.left:
                if current_node.parent.left == current_node:
                    current_node.parent.left = current_node.left
                else:
                    current_node.parent.right = current_node.left
                current_node.left.parent = current_node.parent
            else:
                if current_node.parent.left == current_node:
                    current_node.parent.left = current_node.right
                else:
                    current_node.parent.right = current_node.right
                current_node.right.parent = current_node.parent
    def sorted_by_count(self):
        sorted_list = [None] * self.size
        count_dict = OrderedDict(self.count_dict)
        position_map = OrderedDict()
        start_index = -1
        for count in count_dict:
            position_map[count] = count_dict[count] + start_index
            start_index += count_dict[count]
        for value, count in self:
            sorted_list[position_map[count]] = (value, count)
            position_map[count] -= 1
        return sorted_list[::-1]
    def plot(self):
        labels = {node: node for node, _ in self.root.edge_list()}
        graph = nx.Graph(self.root.edge_list())
        pos = graphviz_layout(graph, prog='dot')
        nx.draw(graph, pos)
        nx.draw_networkx_labels(graph, pos, labels)
        plt.show()
if __name__ == "__main__":
    bst = BST(file='sample.txt')
    bst.plot()
    bst.put('example')
    print('example' in bst)
    bst.delete('example')
    print('example' in bst)
    print(bst.sorted_by_count())