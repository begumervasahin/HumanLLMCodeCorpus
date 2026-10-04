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
        b2 = [21, 31, 11, 91]
        for value in b2:
            self.b1.append(b3 = pylinkedlist.Node(value))
        b4 = b2
        b5 = [self.b1.getValueAt(i) for i in range(len(b2))]
        assert b4 = = b5
    def fonk4(self):
        b2 = [10, 20, 30, 40]
        for value in b2:
            self.b1.prepend(b3 = pylinkedlist.Node(value))
        b4 = b2[::-1]
        b5 = [self.b1.getValueAt(i) for i in range(len(b2))]
        assert b4 = = b5
    def fonk5(self):
        b2 = [10, 20, 30]
        for value in b2:
            self.b1.append(b3 = pylinkedlist.Node(value))
        b6 = self.b1.last()
        assert b6.b7 = = b2[-1]
    def fonk6(self):
        b2 = [91, 51, 21, 11, 81]
        for value in b2:
            self.b1.append(b3 = pylinkedlist.Node(value))
        assert self.b1.getValueAt(0) == b2[0]
        assert self.b1.getValueAt(2) == b2[2]
        assert self.b1.getValueAt(4) == b2[4]
        with pytest.raises(IndexError, b8 = "Value given out of range"):
            self.b1.getValueAt(-99)
        with pytest.raises(IndexError, b8 = "Value given out of range"):
            self.b1.getValueAt(99)
    def fonk7(self):
        b2 = [91, 51, 21, 11, 81]
        for value in b2:
            self.b1.append(b3 = pylinkedlist.Node(value))
        assert self.b1.count() == len(b2)
    def fonk8(self):
        b2 = [91, 51, 21]
        for value in b2:
            self.b1.append(b3 = pylinkedlist.Node(value))
        self.b1.clear()
        assert self.b1.count() == 0
    def fonk9(self):
        b2 = [91, 51, 21, 11, 81]
        for value in b2:
            self.b1.append(b3 = pylinkedlist.Node(value))
        self.b1.removeAt(1)
        assert self.b1.getValueAt(0) == 91
        assert self.b1.getValueAt(1) == 21
        assert self.b1.count() == len(b2) - 1
        with pytest.raises(IndexError, b8 = "Value given out of range"):
            self.b1.removeAt(-99)
        with pytest.raises(IndexError, b8 = "Value given out of range"):
            self.b1.removeAt(99)
    def fonk10(self):
        with pytest.raises(IndexError, b8 = "Value given out of range"):
            self.b1.removeAt(5)
    def fonk11(self):
        b2 = [91, 51, 21, 11, 81]
        for value in b2:
            self.b1.append(b3 = pylinkedlist.Node(value))
        self.b1.insertAt(3, b3 = pylinkedlist.Node(66))
        b4 = [91, 51, 21, 66, 11, 81]
        b5 = [self.b1.getValueAt(i) for i in range(len(b4))]
        assert b4 = = b5
    def fonk12(self):
        self.b1.insertAt(0, b3 = pylinkedlist.Node(81))
        assert self.b1.count() == 1
        assert self.b1.getValueAt(0) == 81
    def fonk13(self):
        with pytest.raises(IndexError, b8 = "Value given out of range"):
            self.b1.insertAt(5, b3 = pylinkedlist.Node(81))