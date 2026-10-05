import pylinkedlist
import pytest
class class1:
    b1 = None
    @classmethod
    def fonk1(cls):
        cls.b1 = pylinkedlist.LinkedList()
    def fonk2(self):
        class1.b1.clear()
    def fonk3(self):
        self.b1.append(b2 = pylinkedlist.Node(21))
        self.b1.append(b2 = pylinkedlist.Node(31))
        self.b1.append(b2 = pylinkedlist.Node(11))
        self.b1.append(b2 = pylinkedlist.Node(91))
        assert self.b1.to_list() == [21, 31, 11, 91]
    def fonk4(self):
        self.b1.prepend(b2 = pylinkedlist.Node(10))
        self.b1.prepend(b2 = pylinkedlist.Node(20))
        self.b1.prepend(b2 = pylinkedlist.Node(30))
        self.b1.prepend(b2 = pylinkedlist.Node(40))
        assert self.b1.to_list() == [40, 30, 20, 10]
    def fonk5(self):
        self.b1.append(b2 = pylinkedlist.Node(10))
        self.b1.append(b2 = pylinkedlist.Node(20))
        self.b1.append(b2 = pylinkedlist.Node(30))
        assert self.b1.last().b3 = = 30
    def fonk6(self):
        self.b1.append(b2 = pylinkedlist.Node(91))
        self.b1.append(b2 = pylinkedlist.Node(51))
        self.b1.append(b2 = pylinkedlist.Node(21))
        self.b1.append(b2 = pylinkedlist.Node(11))
        self.b1.append(b2 = pylinkedlist.Node(81))
        assert self.b1.getValueAt(0) == 91
        assert self.b1.getValueAt(2) == 21
        assert self.b1.getValueAt(4) == 81
        with pytest.raises(IndexError) as exc_info:
            self.b1.getValueAt(-99)
        assert str(exc_info.value) == "Value given out of range"
if b4 = = "__main__":
    pytest.main()