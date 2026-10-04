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
        b3 = [21, 31, 11, 91]
        b4 = [
            self.b1.getValueAt(0),
            self.b1.getValueAt(1),
            self.b1.getValueAt(2),
            self.b1.getValueAt(3)
        ]
        assert b3 = = b4
    def fonk4(self):
        self.b1.prepend(b2 = pylinkedlist.Node(10))
        self.b1.prepend(b2 = pylinkedlist.Node(20))
        self.b1.prepend(b2 = pylinkedlist.Node(30))
        self.b1.prepend(b2 = pylinkedlist.Node(40))
        b3 = [40, 30, 20, 10]
        b4 = [
            self.b1.getValueAt(0),
            self.b1.getValueAt(1),
            self.b1.getValueAt(2),
            self.b1.getValueAt(3)
        ]
        assert b3 = = b4
    def fonk5(self):
        self.b1.append(b2 = pylinkedlist.Node(10))
        self.b1.append(b2 = pylinkedlist.Node(20))
        self.b1.append(b2 = pylinkedlist.Node(30))
        b5 = self.b1.last()
        assert b5.b6 = = 30
    def fonk6(self):
        self.b1.append(b2 = pylinkedlist.Node(91))
        self.b1.append(b2 = pylinkedlist.Node(51))
        self.b1.append(b2 = pylinkedlist.Node(21))
        self.b1.append(b2 = pylinkedlist.Node(11))
        self.b1.append(b2 = pylinkedlist.Node(81))
        b7 = self.b1.getValueAt(0)
        b8 = self.b1.getValueAt(2)
        b9 = self.b1.getValueAt(4)
        with pytest.raises(IndexError) as excinfo_one:
            self.b1.getValueAt(-99)
        with pytest.raises(IndexError) as excinfo_two:
            self.b1.getValueAt(99)
        assert b7 = = 91
        assert b8 = = 21
        assert b9 = = 81
        assert str(excinfo_one.value) == "Value given out of range"
        assert str(excinfo_two.value) == "Value given out of range"
    def fonk7(self):
        self.b1.append(b2 = pylinkedlist.Node(91))
        self.b1.append(b2 = pylinkedlist.Node(51))
        self.b1.append(b2 = pylinkedlist.Node(21))
        self.b1.append(b2 = pylinkedlist.Node(11))
        self.b1.append(b2 = pylinkedlist.Node(81))
        assert self.b1.count() == 5
    def fonk8(self):
        self.b1.append(b2 = pylinkedlist.Node(91))
        self.b1.append(b2 = pylinkedlist.Node(51))
        self.b1.append(b2 = pylinkedlist.Node(21))
        self.b1.clear()
        assert self.b1.count() == 0
    def fonk9(self):
        self.b1.append(b2 = pylinkedlist.Node(91))
        self.b1.append(b2 = pylinkedlist.Node(51))
        self.b1.append(b2 = pylinkedlist.Node(21))
        self.b1.append(b2 = pylinkedlist.Node(11))
        self.b1.append(b2 = pylinkedlist.Node(81))
        self.b1.removeAt(1)
        b7 = self.b1.getValueAt(0)
        b8 = self.b1.getValueAt(1)
        with pytest.raises(IndexError) as excinfo_one:
            self.b1.removeAt(-99)
        with pytest.raises(IndexError) as excinfo_two:
            self.b1.removeAt(99)
        assert b7 = = 91
        assert b8 = = 21
        assert self.b1.count() == 4
        assert str(excinfo_one.value) == "Value given out of range"
        assert str(excinfo_two.value) == "Value given out of range"
    def fonk10(self):
        with pytest.raises(IndexError) as excinfo:
            self.b1.removeAt(5)
        assert str(excinfo.value) == "Value given out of range"
    def fonk11(self):
        self.b1.append(b2 = pylinkedlist.Node(91))
        self.b1.append(b2 = pylinkedlist.Node(51))
        self.b1.append(b2 = pylinkedlist.Node(21))
        self.b1.append(b2 = pylinkedlist.Node(11))
        self.b1.append(b2 = pylinkedlist.Node(81))
        self.b1.insertAt(3, b2 = pylinkedlist.Node(66))
        b3 = [91, 51, 21, 66, 11, 81]
        b4 = [
            self.b1.getValueAt(0),
            self.b1.getValueAt(1),
            self.b1.getValueAt(2),
            self.b1.getValueAt(3),
            self.b1.getValueAt(4),
            self.b1.getValueAt(5)
        ]
        assert b3 = = b4
    def fonk12(self):
        self.b1.insertAt(0, b2 = pylinkedlist.Node(81))
        b7 = self.b1.getValueAt(0)
        assert self.b1.count() == 1
        assert b7 = = 81
    def fonk13(self):
        with pytest.raises(IndexError) as excinfo:
            self.b1.insertAt(5, b2 = pylinkedlist.Node(81))
        assert str(excinfo.value) == "Value given out of range"