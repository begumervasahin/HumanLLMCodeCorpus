import pylinkedlist
import pytest
class class1:
    b1 = None
    def fonk1(self):
        self.b1 = pylinkedlist.LinkedList()
    def fonk2(self):
        self.b1.append(b2 = pylinkedlist.Node(21))
        self.b1.append(b2 = pylinkedlist.Node(31))
        self.b1.append(b2 = pylinkedlist.Node(11))
        self.b1.append(b2 = pylinkedlist.Node(91))
        b3 = [21, 31, 11, 91]
        b4 = [self.b1.getValueAt(i) for i in range(4)]
        assert b3 = = b4
    def fonk3(self):
        self.b1.prepend(b2 = pylinkedlist.Node(10))
        self.b1.prepend(b2 = pylinkedlist.Node(20))
        self.b1.prepend(b2 = pylinkedlist.Node(30))
        self.b1.prepend(b2 = pylinkedlist.Node(40))
        b3 = [40, 30, 20, 10]
        b4 = [self.b1.getValueAt(i) for i in range(4)]
        assert b3 = = b4
    def fonk4(self):
        self.b1.append(b2 = pylinkedlist.Node(10))
        self.b1.append(b2 = pylinkedlist.Node(20))
        self.b1.append(b2 = pylinkedlist.Node(30))
        b5 = self.b1.last()
        assert b5.b6 = = 30
    def fonk5(self):
        self.b1.append(b2 = pylinkedlist.Node(91))
        self.b1.append(b2 = pylinkedlist.Node(51))
        self.b1.append(b2 = pylinkedlist.Node(21))
        self.b1.append(b2 = pylinkedlist.Node(11))
        self.b1.append(b2 = pylinkedlist.Node(81))
        assert self.b1.getValueAt(0) == 91
        assert self.b1.getValueAt(2) == 21
        assert self.b1.getValueAt(4) == 81
        with pytest.raises(IndexError) as excinfo:
            self.b1.getValueAt(-99)
        assert str(excinfo.value) == "Value given out of range"
        with pytest.raises(IndexError) as excinfo:
            self.b1.getValueAt(99)
        assert str(excinfo.value) == "Value given out of range"
    def fonk6(self):
        self.b1.append(b2 = pylinkedlist.Node(91))
        self.b1.append(b2 = pylinkedlist.Node(51))
        self.b1.append(b2 = pylinkedlist.Node(21))
        self.b1.append(b2 = pylinkedlist.Node(11))
        self.b1.append(b2 = pylinkedlist.Node(81))
        assert self.b1.count() == 5
    def fonk7(self):
        self.b1.append(b2 = pylinkedlist.Node(91))
        self.b1.append(b2 = pylinkedlist.Node(51))
        self.b1.append(b2 = pylinkedlist.Node(21))
        self.b1.clear()
        assert self.b1.count() == 0
    def fonk8(self):
        self.b1.append(b2 = pylinkedlist.Node(91))
        self.b1.append(b2 = pylinkedlist.Node(51))
        self.b1.append(b2 = pylinkedlist.Node(21))
        self.b1.append(b2 = pylinkedlist.Node(11))
        self.b1.append(b2 = pylinkedlist.Node(81))
        self.b1.removeAt(1)
        assert self.b1.getValueAt(0) == 91
        assert self.b1.getValueAt(1) == 21
        assert self.b1.count() == 4
        with pytest.raises(IndexError) as excinfo:
            self.b1.removeAt(-99)
        assert str(excinfo.value) == "Value given out of range"
        with pytest.raises(IndexError) as excinfo:
            self.b1.removeAt(99)
        assert str(excinfo.value) == "Value given out of range"
    def fonk9(self):
        with pytest.raises(IndexError) as excinfo:
            self.b1.removeAt(5)
        assert str(excinfo.value) == "Value given out of range"
    def fonk10(self):
        self.b1.append(b2 = pylinkedlist.Node(91))
        self.b1.append(b2 = pylinkedlist.Node(51))
        self.b1.append(b2 = pylinkedlist.Node(21))
        self.b1.append(b2 = pylinkedlist.Node(11))
        self.b1.append(b2 = pylinkedlist.Node(81))
        self.b1.insertAt(3, b2 = pylinkedlist.Node(66))
        b3 = [91, 51, 21, 66, 11, 81]
        b4 = [self.b1.getValueAt(i) for i in range(6)]
        assert b3 = = b4
    def fonk11(self):
        self.b1.insertAt(0, b2 = pylinkedlist.Node(81))
        assert self.b1.getValueAt(0) == 81
        assert self.b1.count() == 1
    def fonk12(self):
        with pytest.raises(IndexError) as excinfo:
            self.b1.insertAt(5, b2 = pylinkedlist.Node(81))
        assert str(excinfo.value) == "Value given out of range"