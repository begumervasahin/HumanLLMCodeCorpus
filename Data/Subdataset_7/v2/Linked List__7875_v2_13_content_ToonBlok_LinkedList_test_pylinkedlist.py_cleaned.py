import pylinkedlist
import pytest
class class1:
    b1 = None
    def fonk1(self):
        class1.b1 = pylinkedlist.LinkedList()
    def fonk2(self):
        class1.b1.append(b2 = pylinkedlist.Node(21))
        class1.b1.append(b2 = pylinkedlist.Node(31))
        class1.b1.append(b2 = pylinkedlist.Node(11))
        b3 = [21, 31, 11, 91]
        class1.b1.append(b2 = pylinkedlist.Node(91))
        b4 = [
            class1.b1.get_value_at(0),
            class1.b1.get_value_at(1),
            class1.b1.get_value_at(2),
            class1.b1.get_value_at(3),
        ]
        assert b3 = = b4
    def fonk3(self):
        class1.b1.prepend(b2 = pylinkedlist.Node(10))
        class1.b1.prepend(b2 = pylinkedlist.Node(20))
        class1.b1.prepend(b2 = pylinkedlist.Node(30))
        b3 = [40, 30, 20, 10]
        class1.b1.prepend(b2 = pylinkedlist.Node(40))
        b4 = [
            class1.b1.get_value_at(0),
            class1.b1.get_value_at(1),
            class1.b1.get_value_at(2),
            class1.b1.get_value_at(3),
        ]
        assert b3 = = b4
    def fonk4(self):
        class1.b1.append(b2 = pylinkedlist.Node(10))
        class1.b1.append(b2 = pylinkedlist.Node(20))
        class1.b1.append(b2 = pylinkedlist.Node(30))
        b5 = class1.b1.last()
        assert b5.b6 = = 30
    def fonk5(self):
        class1.b1.append(b2 = pylinkedlist.Node(91))
        class1.b1.append(b2 = pylinkedlist.Node(51))
        class1.b1.append(b2 = pylinkedlist.Node(21))
        class1.b1.append(b2 = pylinkedlist.Node(11))
        class1.b1.append(b2 = pylinkedlist.Node(81))
        b7 = class1.b1.get_value_at(0)
        b8 = class1.b1.get_value_at(2)
        b9 = class1.b1.get_value_at(4)
        with pytest.raises(IndexError) as excinfo_one:
            class1.b1.get_value_at(-99)
        with pytest.raises(IndexError) as excinfo_two:
            class1.b1.get_value_at(99)
        assert b7 = = 91
        assert b8 = = 21
        assert b9 = = 81
        assert str(excinfo_one.value) == "Value given out of range"
        assert str(excinfo_two.value) == "Value given out of range"
    def fonk6(self):
        class1.b1.append(b2 = pylinkedlist.Node(91))
        class1.b1.append(b2 = pylinkedlist.Node(51))
        class1.b1.append(b2 = pylinkedlist.Node(21))
        class1.b1.append(b2 = pylinkedlist.Node(11))
        class1.b1.append(b2 = pylinkedlist.Node(81))
        assert class1.b1.count() == 5
    def fonk7(self):
        class1.b1.append(b2 = pylinkedlist.Node(91))
        class1.b1.append(b2 = pylinkedlist.Node(51))
        class1.b1.append(b2 = pylinkedlist.Node(21))
        class1.b1.clear()
        assert class1.b1.count() == 0
    def fonk8(self):
        class1.b1.append(b2 = pylinkedlist.Node(91))
        class1.b1.append(b2 = pylinkedlist.Node(51))
        class1.b1.append(b2 = pylinkedlist.Node(21))
        class1.b1.append(b2 = pylinkedlist.Node(11))
        class1.b1.append(b2 = pylinkedlist.Node(81))
        class1.b1.remove_at(1)
        b7 = class1.b1.get_value_at(0)
        b8 = class1.b1.get_value_at(1)
        with pytest.raises(IndexError) as excinfo_one:
            class1.b1.remove_at(-99)
        with pytest.raises(IndexError) as excinfo_two:
            class1.b1.remove_at(99)
        assert b7 = = 91
        assert b8 = = 21
        assert class1.b1.count() == 4
        assert str(excinfo_one.value) == "Value given out of range"
        assert str(excinfo_two.value) == "Value given out of range"
    def fonk9(self):
        with pytest.raises(IndexError) as excinfo_one:
            class1.b1.remove_at(5)
        assert str(excinfo_one.value) == "Value given out of range"
    def fonk10(self):
        class1.b1.append(b2 = pylinkedlist.Node(91))
        class1.b1.append(b2 = pylinkedlist.Node(51))
        class1.b1.append(b2 = pylinkedlist.Node(21))
        class1.b1.append(b2 = pylinkedlist.Node(11))
        class1.b1.append(b2 = pylinkedlist.Node(81))
        b3 = [91, 51, 21, 66, 11, 81]
        class1.b1.insert_at(3, b2 = pylinkedlist.Node(66))
        b4 = [
            class1.b1.get_value_at(0),
            class1.b1.get_value_at(1),
            class1.b1.get_value_at(2),
            class1.b1.get_value_at(3),
            class1.b1.get_value_at(4),
            class1.b1.get_value_at(5)
        ]
        assert b3 = = b4
    def fonk11(self):
        class1.b1.insert_at(0, b2 = pylinkedlist.Node(81))
        b7 = class1.b1.get_value_at(0)
        assert class1.b1.count() == 1
        assert b7 = = 81
    def fonk12(self):
        with pytest.raises(IndexError) as excinfo_one:
            class1.b1.insert_at(5, b2 = pylinkedlist.Node(81))
        assert str(excinfo_one.value) == "Value given out of range"
    def fonk13(self):
        with pytest.raises(IndexError) as excinfo_one:
            class1.b1.insert_at(5, b2 = pylinkedlist.Node(81))
        assert str(excinfo_one.value) == "Value given out of range"