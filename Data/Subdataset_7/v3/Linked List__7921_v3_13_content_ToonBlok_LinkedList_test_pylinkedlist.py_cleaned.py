import pylinkedlist
import pytest
class class1:
    b1 = None
    @classmethod
    def fonk1(cls):
        cls.b1 = pylinkedlist.LinkedList()
    def fonk2(self):
        self.b1.append(pylinkedlist.Node(21))
        self.b1.append(pylinkedlist.Node(31))
        self.b1.append(pylinkedlist.Node(11))
        self.b1.append(pylinkedlist.Node(91))
        b2 = [21, 31, 11, 91]
        b3 = [self.b1.get_value_at(i) for i in range(self.b1.count())]
        assert b2 = = b3
    def fonk3(self):
        self.b1.prepend(pylinkedlist.Node(10))
        self.b1.prepend(pylinkedlist.Node(20))
        self.b1.prepend(pylinkedlist.Node(30))
        self.b1.prepend(pylinkedlist.Node(40))
        b2 = [40, 30, 20, 10]
        b3 = [self.b1.get_value_at(i) for i in range(self.b1.count())]
        assert b2 = = b3
    def fonk4(self):
        self.b1.append(pylinkedlist.Node(10))
        self.b1.append(pylinkedlist.Node(20))
        self.b1.append(pylinkedlist.Node(30))
        b4 = self.b1.last()
        assert b4.b5 = = 30
    def fonk5(self):
        self.b1.append(pylinkedlist.Node(91))
        self.b1.append(pylinkedlist.Node(51))
        self.b1.append(pylinkedlist.Node(21))
        self.b1.append(pylinkedlist.Node(11))
        self.b1.append(pylinkedlist.Node(81))
        b6 = self.b1.get_value_at(0)
        b7 = self.b1.get_value_at(2)
        b8 = self.b1.get_value_at(4)
        with pytest.raises(IndexError) as excinfo_one:
            self.b1.get_value_at(-99)
        with pytest.raises(IndexError) as excinfo_two:
            self.b1.get_value_at(99)
        assert b6 = = 91
        assert b7 = = 21
        assert b8 = = 81
        assert str(excinfo_one.value) == "Value given out of range"
        assert str(excinfo_two.value) == "Value given out of range"
    def fonk6(self):
        self.b1.append(pylinkedlist.Node(91))
        self.b1.append(pylinkedlist.Node(51))
        self.b1.append(pylinkedlist.Node(21))
        self.b1.append(pylinkedlist.Node(11))
        self.b1.append(pylinkedlist.Node(81))
        assert self.b1.count() == 5
    def fonk7(self):
        self.b1.append(pylinkedlist.Node(91))
        self.b1.append(pylinkedlist.Node(51))
        self.b1.append(pylinkedlist.Node(21))
        self.b1.clear()
        assert self.b1.count() == 0
    def fonk8(self):
        self.b1.append(pylinkedlist.Node(91))
        self.b1.append(pylinkedlist.Node(51))
        self.b1.append(pylinkedlist.Node(21))
        self.b1.append(pylinkedlist.Node(11))
        self.b1.append(pylinkedlist.Node(81))
        self.b1.remove_at(1)
        b6 = self.b1.get_value_at(0)
        b7 = self.b1.get_value_at(1)
        with pytest.raises(IndexError) as excinfo_one:
            self.b1.remove_at(-99)
        with pytest.raises(IndexError) as excinfo_two:
            self.b1.remove_at(99)
        assert b6 = = 91
        assert b7 = = 21
        assert self.b1.count() == 4
        assert str(excinfo_one.value) == "Value given out of range"
        assert str(excinfo_two.value) == "Value given out of range"
    def fonk9(self):
        with pytest.raises(IndexError) as excinfo_one:
            self.b1.remove_at(5)
        assert str(excinfo_one.value) == "Value given out of range"
    def fonk10(self):
        self.b1.append(pylinkedlist.Node(91))
        self.b1.append(pylinkedlist.Node(51))
        self.b1.append(pylinkedlist.Node(21))
        self.b1.append(pylinkedlist.Node(11))
        self.b1.append(pylinkedlist.Node(81))
        self.b1.insert_at(3, pylinkedlist.Node(66))
        b2 = [91, 51, 21, 66, 11, 81]
        b3 = [self.b1.get_value_at(i) for i in range(self.b1.count())]
        assert b2 = = b3
    def fonk11(self):
        self.b1.insert_at(0, pylinkedlist.Node(81))
        b6 = self.b1.get_value_at(0)
        assert self.b1.count() == 1
        assert b6 = = 81
    def fonk12(self):
        with pytest.raises(IndexError) as excinfo_one:
            self.b1.insert_at(5, pylinkedlist.Node(81))
        assert str(excinfo_one.value) == "Value given out of range"
    def fonk13(self):
        with pytest.raises(IndexError) as excinfo_one:
            self.b1.insert_at(5, pylinkedlist.Node(81))
        assert str(excinfo_one.value) == "Value given out of range"