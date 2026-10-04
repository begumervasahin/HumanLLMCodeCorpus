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
        self.linkedList.append(node=pylinkedlist.Node(21))
        self.linkedList.append(node=pylinkedlist.Node(31))
        self.linkedList.append(node=pylinkedlist.Node(11))
        self.linkedList.append(node=pylinkedlist.Node(91))
        expected_order = [21, 31, 11, 91]
        actual_order = [
            self.linkedList.getValueAt(0),
            self.linkedList.getValueAt(1),
            self.linkedList.getValueAt(2),
            self.linkedList.getValueAt(3)
        ]
        assert expected_order == actual_order
    def test_prepend(self):
        self.linkedList.prepend(node=pylinkedlist.Node(10))
        self.linkedList.prepend(node=pylinkedlist.Node(20))
        self.linkedList.prepend(node=pylinkedlist.Node(30))
        self.linkedList.prepend(node=pylinkedlist.Node(40))
        expected_order = [40, 30, 20, 10]
        actual_order = [
            self.linkedList.getValueAt(0),
            self.linkedList.getValueAt(1),
            self.linkedList.getValueAt(2),
            self.linkedList.getValueAt(3)
        ]
        assert expected_order == actual_order
    def test_last(self):
        self.linkedList.append(node=pylinkedlist.Node(10))
        self.linkedList.append(node=pylinkedlist.Node(20))
        self.linkedList.append(node=pylinkedlist.Node(30))
        last_node = self.linkedList.last()
        assert last_node.data == 30
    def test_get_value_at(self):
        self.linkedList.append(node=pylinkedlist.Node(91))
        self.linkedList.append(node=pylinkedlist.Node(51))
        self.linkedList.append(node=pylinkedlist.Node(21))
        self.linkedList.append(node=pylinkedlist.Node(11))
        self.linkedList.append(node=pylinkedlist.Node(81))
        val_one = self.linkedList.getValueAt(0)
        val_two = self.linkedList.getValueAt(2)
        val_three = self.linkedList.getValueAt(4)
        with pytest.raises(IndexError) as excinfo_one:
            self.linkedList.getValueAt(-99)
        with pytest.raises(IndexError) as excinfo_two:
            self.linkedList.getValueAt(99)
        assert val_one == 91
        assert val_two == 21
        assert val_three == 81
        assert str(excinfo_one.value) == "Value given out of range"
        assert str(excinfo_two.value) == "Value given out of range"
    def test_count(self):
        self.linkedList.append(node=pylinkedlist.Node(91))
        self.linkedList.append(node=pylinkedlist.Node(51))
        self.linkedList.append(node=pylinkedlist.Node(21))
        self.linkedList.append(node=pylinkedlist.Node(11))
        self.linkedList.append(node=pylinkedlist.Node(81))
        assert self.linkedList.count() == 5
    def test_clear(self):
        self.linkedList.append(node=pylinkedlist.Node(91))
        self.linkedList.append(node=pylinkedlist.Node(51))
        self.linkedList.append(node=pylinkedlist.Node(21))
        self.linkedList.clear()
        assert self.linkedList.count() == 0
    def test_remove_at(self):
        self.linkedList.append(node=pylinkedlist.Node(91))
        self.linkedList.append(node=pylinkedlist.Node(51))
        self.linkedList.append(node=pylinkedlist.Node(21))
        self.linkedList.append(node=pylinkedlist.Node(11))
        self.linkedList.append(node=pylinkedlist.Node(81))
        self.linkedList.removeAt(1)
        val_one = self.linkedList.getValueAt(0)
        val_two = self.linkedList.getValueAt(1)
        with pytest.raises(IndexError) as excinfo_one:
            self.linkedList.removeAt(-99)
        with pytest.raises(IndexError) as excinfo_two:
            self.linkedList.removeAt(99)
        assert val_one == 91
        assert val_two == 21
        assert self.linkedList.count() == 4
        assert str(excinfo_one.value) == "Value given out of range"
        assert str(excinfo_two.value) == "Value given out of range"
    def test_remove_at_when_empty(self):
        with pytest.raises(IndexError) as excinfo:
            self.linkedList.removeAt(5)
        assert str(excinfo.value) == "Value given out of range"
    def test_insert_at(self):
        self.linkedList.append(node=pylinkedlist.Node(91))
        self.linkedList.append(node=pylinkedlist.Node(51))
        self.linkedList.append(node=pylinkedlist.Node(21))
        self.linkedList.append(node=pylinkedlist.Node(11))
        self.linkedList.append(node=pylinkedlist.Node(81))
        self.linkedList.insertAt(3, node=pylinkedlist.Node(66))
        expected_order = [91, 51, 21, 66, 11, 81]
        actual_order = [
            self.linkedList.getValueAt(0),
            self.linkedList.getValueAt(1),
            self.linkedList.getValueAt(2),
            self.linkedList.getValueAt(3),
            self.linkedList.getValueAt(4),
            self.linkedList.getValueAt(5)
        ]
        assert expected_order == actual_order
    def test_insert_at_0_when_empty(self):
        self.linkedList.insertAt(0, node=pylinkedlist.Node(81))
        val_one = self.linkedList.getValueAt(0)
        assert self.linkedList.count() == 1
        assert val_one == 81
    def test_insert_at_out_of_index(self):
        with pytest.raises(IndexError) as excinfo:
            self.linkedList.insertAt(5, node=pylinkedlist.Node(81))
        assert str(excinfo.value) == "Value given out of range"