class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy_head = ListNode(0)
        current = dummy_head
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            current.next = ListNode(carry % 10)
            current = current.next
            carry
        return dummy_head.next
