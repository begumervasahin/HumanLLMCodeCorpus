import pylinkedlist
import pytest
class TestLinkedList:
    linkedList = None
    @classmethod
    def setup_class(cls):
        cls.linkedList = pylinkedlist.LinkedList()
    def setup_method(self):
        TestLinkedList.linkedList.clear()
    def test_append(self):
        nodes = [21, 31, 11, 91]
        for value in nodes:
            self.linkedList.append(node=pylinkedlist.Node(value))
        expected_order = nodes
        actual_order = [self.linkedList.getValueAt(i) for i in range(len(nodes))]
        assert expected_order == actual_order
    def test_prepend(self):
        nodes = [10, 20, 30, 40]
        for value in nodes:
            self.linkedList.prepend(node=pylinkedlist.Node(value))
        expected_order = nodes[::-1]
        actual_order = [self.linkedList.getValueAt(i) for i in range(len(nodes))]
        assert expected_order == actual_order
    def test_last(self):
        nodes = [10, 20, 30]
        for value in nodes:
            self.linkedList.append(node=pylinkedlist.Node(value))
        last_node = self.linkedList.last()
        assert last_node.data == nodes[-1]
    def test_get_value_at(self):
        nodes = [91, 51, 21, 11, 81]
        for value in nodes:
            self.linkedList.append(node=pylinkedlist.Node(value))
        assert self.linkedList.getValueAt(0) == nodes[0]
        assert self.linkedList.getValueAt(2) == nodes[2]
        assert self.linkedList.getValueAt(4) == nodes[4]
        with pytest.raises(IndexError, match="Value given out of range"):
            self.linkedList.getValueAt(-99)
        with pytest.raises(IndexError, match="Value given out of range"):
            self.linkedList.getValueAt(99)
    def test_count(self):
        nodes = [91, 51, 21, 11, 81]
        for value in nodes:
            self.linkedList.append(node=pylinkedlist.Node(value))
        assert self.linkedList.count() == len(nodes)
    def test_clear(self):
        nodes = [91, 51, 21]
        for value in nodes:
            self.linkedList.append(node=pylinkedlist.Node(value))
        self.linkedList.clear()
        assert self.linkedList.count() == 0
    def test_remove_at(self):
        nodes = [91, 51, 21, 11, 81]
        for value in nodes:
            self.linkedList.append(node=pylinkedlist.Node(value))
        self.linkedList.removeAt(1)
        assert self.linkedList.getValueAt(0) == 91
        assert self.linkedList.getValueAt(1) == 21
        assert self.linkedList.count() == len(nodes) - 1
        with pytest.raises(IndexError, match="Value given out of range"):
            self.linkedList.removeAt(-99)
        with pytest.raises(IndexError, match="Value given out of range"):
            self.linkedList.removeAt(99)
    def test_remove_at_when_empty(self):
        with pytest.raises(IndexError, match="Value given out of range"):
            self.linkedList.removeAt(5)
    def test_insert_at(self):
        nodes = [91, 51, 21, 11, 81]
        for value in nodes:
            self.linkedList.append(node=pylinkedlist.Node(value))
        self.linkedList.insertAt(3, node=pylinkedlist.Node(66))
        expected_order = [91, 51, 21, 66, 11, 81]
        actual_order = [self.linkedList.getValueAt(i) for i in range(len(expected_order))]
        assert expected_order == actual_order
    def test_insert_at_0_when_empty(self):
        self.linkedList.insertAt(0, node=pylinkedlist.Node(81))
        assert self.linkedList.count() == 1
        assert self.linkedList.getValueAt(0) == 81
    def test_insert_at_out_of_index(self):
        with pytest.raises(IndexError, match="Value given out of range"):
            self.linkedList.insertAt(5, node=pylinkedlist.Node(81))