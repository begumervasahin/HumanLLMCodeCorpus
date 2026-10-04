class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = ListNode(0)
        dummy = root
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            dummy.next = ListNode(carry % 10)
            carry
            dummy = dummy.next
        return root.next
if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    while result:
        print(result.val, end=" -> " if result.next else "\n")
        result = result.next