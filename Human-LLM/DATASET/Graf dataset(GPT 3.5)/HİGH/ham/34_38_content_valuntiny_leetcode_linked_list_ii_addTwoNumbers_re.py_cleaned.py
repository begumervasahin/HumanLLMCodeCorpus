'''
Quest:
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order and each of their nodes contain a single digit.
    Add the two numbers and return it as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    Example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + a1 = 807.
class2:
    - just a loop, but need to calculate a2
'''
class class1:
    def fonk1(self, x):
        self.b1 = x
        self.b2 = None
class class2:
    def fonk2(self, b5, b6):
        a2 = 0
        b3 = class1(0)
        b4 = b3
        while b5 or b6 or a2:
            if b5:
                a2 += b5.b1
                b5 = b5.b2
            if b6:
                a2 += b6.b1
                b6 = b6.b2
            b4.b2 = class1(a2 % 10)
            a2
            b4 = b4.b2
        return b3.b2