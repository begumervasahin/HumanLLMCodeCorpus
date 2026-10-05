import pylinkedlist
import pytest
class TestAppend:
    linked_list = None
    def setup(self):
        TestAppend.linked_list = pylinkedlist.LinkedList()
    def test_append(self):
        TestAppend.linked_list.append(node=pylinkedlist.Node(21))
        TestAppend.linked_list.append(node=pylinkedlist.Node(31))
        TestAppend.linked_list.append(node=pylinkedlist.Node(11))
        expected_order = [21, 31, 11, 91]
        TestAppend.linked_list.append(node=pylinkedlist.Node(91))
        actual_order = [
            TestAppend.linked_list.getValueAt(0),
            TestAppend.linked_list.getValueAt(1),
            TestAppend.linked_list.getValueAt(2),
            TestAppend.linked_list.getValueAt(3),
        ]
        assert expected_order == actual_order
    def test_prepend(self):
        TestAppend.linked_list.prepend(node=pylinkedlist.Node(10))
        TestAppend.linked_list.prepend(node=pylinkedlist.Node(20))
        TestAppend.linked_list.prepend(node=pylinkedlist.Node(30))
        expected_order = [40, 30, 20, 10]
        TestAppend.linked_list.prepend(node=pylinkedlist.Node(40))
        actual_order = [
            TestAppend.linked_list.getValueAt(0),
            TestAppend.linked_list.getValueAt(1),
            TestAppend.linked_list.getValueAt(2),
            TestAppend.linked_list.getValueAt(3),
        ]
        assert expected_order == actual_order
    def test_last(self):
        TestAppend.linked_list.append(node=pylinkedlist.Node(10))
        TestAppend.linked_list.append(node=pylinkedlist.Node(20))
        TestAppend.linked_list.append(node=pylinkedlist.Node(30))
        last_node = TestAppend.linked_list.last()
        assert last_node.data == 30
    def test_getValueAt(self):
        TestAppend.linked_list.append(node=pylinkedlist.Node(91))
        TestAppend.linked_list.append(node=pylinkedlist.Node(51))
        TestAppend.linked_list.append(node=pylinkedlist.Node(21))
        TestAppend.linked_list.append(node=pylinkedlist.Node(11))
        TestAppend.linked_list.append(node=pylinkedlist.Node(81))
        val_one = TestAppend.linked_list.getValueAt(0)
        val_two = TestAppend.linked_list.getValueAt(2)
        val_three = TestAppend.linked_list.getValueAt(4)
        with pytest.raises(IndexError) as exc_info_one:
            TestAppend.linked_list.getValueAt(-99)
        with pytest.raises(IndexError) as exc_info_two:
            TestAppend.linked_list.getValueAt(99)
        assert val_one == 91
        assert val_two == 21
        assert val_three == 81
        assert str(exc_info_one.value) == "Value given out of range"
        assert str(exc_info_two.value) == "Value given out of range"
    def test_count(self):
        TestAppend.linked_list.append(node=pylinkedlist.Node(91))
        TestAppend.linked_list.append(node=pylinkedlist.Node(51))
        TestAppend.linked_list.append(node=pylinkedlist.Node(21))
        TestAppend.linked_list.append(node=pylinkedlist.Node(11))
        TestAppend.linked_list.append(node=pylinkedlist.Node(81))
        assert TestAppend.linked_list.count() == 5
    def test_clear(self):
        TestAppend.linked_list.append(node=pylinkedlist.Node(91))
        TestAppend.linked_list.append(node=pylinkedlist.Node(51))
        TestAppend.linked_list.append(node=pylinkedlist.Node(21))
        TestAppend.linked_list.clear()
        assert TestAppend.linked_list.count() == 0
    def test_removeAt(self):
        TestAppend.linked_list.append(node=pylinkedlist.Node(91))
        TestAppend.linked_list.append(node=pylinkedlist.Node(51))
        TestAppend.linked_list.append(node=pylinkedlist.Node(21))
        TestAppend.linked_list.append(node=pylinkedlist.Node(11))
        TestAppend.linked_list.append(node=pylinkedlist.Node(81))
        TestAppend.linked_list.removeAt(1)
        val_one = TestAppend.linked_list.getValueAt(0)
        val_two = TestAppend.linked_list.getValueAt(1)
        with pytest.raises(IndexError) as exc_info_one:
            TestAppend.linked_list.removeAt(-99)
        with pytest.raises(IndexError) as exc_info_two:
            TestAppend.linked_list.removeAt(99)
        assert val_one == 91
        assert val_two == 21
        assert TestAppend.linked_list.count() == 4
        assert str(exc_info_one.value) == "Value given out of range"
        assert str(exc_info_two.value) == "Value given out of range"
    def test_removeAtWhenEmpty(self):
        with pytest.raises(IndexError) as exc_info_one:
            TestAppend.linked_list.removeAt(5)
        assert str(exc_info_one.value) == "Value given out of range"
    def test_insertAt(self):
        TestAppend.linked_list.append(node=pylinkedlist.Node(91))
        TestAppend.linked_list.append(node=pylinkedlist.Node(51))
        TestAppend.linked_list.append(node=pylinkedlist.Node(21))
        TestAppend.linked_list.append(node=pylinkedlist.Node(11))
        TestAppend.linked_list.append(node=pylinkedlist.Node(81))
        expected_order = [91, 51, 21, 66, 11, 81]
        TestAppend.linked_list.insertAt(3, node=pylinkedlist.Node(66))
        actual_order = [
            TestAppend.linked_list.getValueAt(0),
            TestAppend.linked_list.getValueAt(1),
            TestAppend.linked_list.getValueAt(2),
            TestAppend.linked_list.getValueAt(3),
            TestAppend.linked_list.getValueAt(4),
            TestAppend.linked_list.getValueAt(5)
        ]
        assert expected_order == actual_order
    def test_insertat0whenempty(self):
        TestAppend.linked_list.insertAt(0, node=pylinkedlist.Node(81))
        val_one = TestAppend.linked_list.getValueAt(0)
        assert TestAppend.linked_list.count() == 1
        assert val_one == 81
    def test_insertAt5WhenEmpty(self):
        with pytest.raises(IndexError) as exc_info_one:
            TestAppend.linked_list.insertAt(5, node=pylinkedlist.Node(81))
        assert str(exc_info_one.value) == "Value given out of range"
    def test_insertAtOutOfIndex(self):
        with pytest.raises(IndexError) as exc_info_one:
            TestAppend.linked_list.insertAt(5, node=pylinkedlist.Node(81))
        assert str(exc_info_one.value) == "Value given out of range"