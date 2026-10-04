class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = ListNode(0)
        current = dummy
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, out = divmod(val1 + val2 + carry, 10)
            current.next = ListNode(out)
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next
def print_linked_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next
if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    print("Result linked list:")
    print_linked_list(result)