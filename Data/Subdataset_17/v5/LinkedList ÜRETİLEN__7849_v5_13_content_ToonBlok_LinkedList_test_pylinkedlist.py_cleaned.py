import pylinkedlist
import pytest
class TestLinkedList:
    def setup_method(self):
        self.linked_list = pylinkedlist.LinkedList()
    def test_append(self):
        self.linked_list.append(node=pylinkedlist.Node(21))
        self.linked_list.append(node=pylinkedlist.Node(31))
        self.linked_list.append(node=pylinkedlist.Node(11))
        self.linked_list.append(node=pylinkedlist.Node(91))
        expected_order = [21, 31, 11, 91]
        actual_order = [self.linked_list.getValueAt(i) for i in range(4)]
        assert expected_order == actual_order
    def test_prepend(self):
        self.linked_list.prepend(node=pylinkedlist.Node(10))
        self.linked_list.prepend(node=pylinkedlist.Node(20))
        self.linked_list.prepend(node=pylinkedlist.Node(30))
        self.linked_list.prepend(node=pylinkedlist.Node(40))
        expected_order = [40, 30, 20, 10]
        actual_order = [self.linked_list.getValueAt(i) for i in range(4)]
        assert expected_order == actual_order
    def test_last(self):
        self.linked_list.append(node=pylinkedlist.Node(10))
        self.linked_list.append(node=pylinkedlist.Node(20))
        self.linked_list.append(node=pylinkedlist.Node(30))
        last_node = self.linked_list.last()
        assert last_node.data == 30
    def test_get_value_at(self):
        self.linked_list.append(node=pylinkedlist.Node(91))
        self.linked_list.append(node=pylinkedlist.Node(51))
        self.linked_list.append(node=pylinkedlist.Node(21))
        self.linked_list.append(node=pylinkedlist.Node(11))
        self.linked_list.append(node=pylinkedlist.Node(81))
        assert self.linked_list.getValueAt(0) == 91
        assert self.linked_list.getValueAt(2) == 21
        assert self.linked_list.getValueAt(4) == 81
        with pytest.raises(IndexError) as excinfo:
            self.linked_list.getValueAt(-99)
        assert str(excinfo.value) == "Value given out of range"
        with pytest.raises(IndexError) as excinfo:
            self.linked_list.getValueAt(99)
        assert str(excinfo.value) == "Value given out of range"
    def test_count(self):
        self.linked_list.append(node=pylinkedlist.Node(91))
        self.linked_list.append(node=pylinkedlist.Node(51))
        self.linked_list.append(node=pylinkedlist.Node(21))
        self.linked_list.append(node=pylinkedlist.Node(11))
        self.linked_list.append(node=pylinkedlist.Node(81))
        assert self.linked_list.count() == 5
    def test_clear(self):
        self.linked_list.append(node=pylinkedlist.Node(91))
        self.linked_list.append(node=pylinkedlist.Node(51))
        self.linked_list.append(node=pylinkedlist.Node(21))
        self.linked_list.clear()
        assert self.linked_list.count() == 0
    def test_remove_at(self):
        self.linked_list.append(node=pylinkedlist.Node(91))
        self.linked_list.append(node=pylinkedlist.Node(51))
        self.linked_list.append(node=pylinkedlist.Node(21))
        self.linked_list.append(node=pylinkedlist.Node(11))
        self.linked_list.append(node=pylinkedlist.Node(81))
        self.linked_list.removeAt(1)
        assert self.linked_list.getValueAt(0) == 91
        assert self.linked_list.getValueAt(1) == 21
        assert self.linked_list.count() == 4
        with pytest.raises(IndexError) as excinfo:
            self.linked_list.removeAt(-99)
        assert str(excinfo.value) == "Value given out of range"
        with pytest.raises(IndexError) as excinfo:
            self.linked_list.removeAt(99)
        assert str(excinfo.value) == "Value given out of range"
    def test_remove_at_when_empty(self):
        with pytest.raises(IndexError) as excinfo:
            self.linked_list.removeAt(5)
        assert str(excinfo.value) == "Value given out of range"
    def test_insert_at(self):
        self.linked_list.append(node=pylinkedlist.Node(91))
        self.linked_list.append(node=pylinkedlist.Node(51))
        self.linked_list.append(node=pylinkedlist.Node(21))
        self.linked_list.append(node=pylinkedlist.Node(11))
        self.linked_list.append(node=pylinkedlist.Node(81))
        self.linked_list.insertAt(3, node=pylinkedlist.Node(66))
        expected_order = [91, 51, 21, 66, 11, 81]
        actual_order = [self.linked_list.getValueAt(i) for i in range(6)]
        assert expected_order == actual_order
    def test_insert_at_0_when_empty(self):
        self.linked_list.insertAt(0, node=pylinkedlist.Node(81))
        assert self.linked_list.getValueAt(0) == 81
        assert self.linked_list.count() == 1
    def test_insert_at_out_of_index(self):
        with pytest.raises(IndexError) as excinfo:
            self.linked_list.insertAt(5, node=pylinkedlist.Node(81))
        assert str(excinfo.value) == "Value given out of range"