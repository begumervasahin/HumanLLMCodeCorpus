import pylinkedlist
import pytest
class TestLinkedListOperations:
    linked_list = None
    @classmethod
    def setup_class(cls):
        cls.linked_list = pylinkedlist.LinkedList()
    def teardown_method(self):
        TestLinkedListOperations.linked_list.clear()
    def test_append_operation(self):
        self.linked_list.append(node=pylinkedlist.Node(21))
        self.linked_list.append(node=pylinkedlist.Node(31))
        self.linked_list.append(node=pylinkedlist.Node(11))
        self.linked_list.append(node=pylinkedlist.Node(91))
        assert self.linked_list.to_list() == [21, 31, 11, 91]
    def test_prepend_operation(self):
        self.linked_list.prepend(node=pylinkedlist.Node(10))
        self.linked_list.prepend(node=pylinkedlist.Node(20))
        self.linked_list.prepend(node=pylinkedlist.Node(30))
        self.linked_list.prepend(node=pylinkedlist.Node(40))
        assert self.linked_list.to_list() == [40, 30, 20, 10]
    def test_last_operation(self):
        self.linked_list.append(node=pylinkedlist.Node(10))
        self.linked_list.append(node=pylinkedlist.Node(20))
        self.linked_list.append(node=pylinkedlist.Node(30))
        assert self.linked_list.last().data == 30
    def test_getValueAt_operation(self):
        self.linked_list.append(node=pylinkedlist.Node(91))
        self.linked_list.append(node=pylinkedlist.Node(51))
        self.linked_list.append(node=pylinkedlist.Node(21))
        self.linked_list.append(node=pylinkedlist.Node(11))
        self.linked_list.append(node=pylinkedlist.Node(81))
        assert self.linked_list.getValueAt(0) == 91
        assert self.linked_list.getValueAt(2) == 21
        assert self.linked_list.getValueAt(4) == 81
        with pytest.raises(IndexError) as exc_info:
            self.linked_list.getValueAt(-99)
        assert str(exc_info.value) == "Value given out of range"
if __name__ == "__main__":
    pytest.main()