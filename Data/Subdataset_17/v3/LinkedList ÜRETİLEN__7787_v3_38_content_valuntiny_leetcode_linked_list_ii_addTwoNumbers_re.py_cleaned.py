class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = ListNode(0)
        current = dummy
        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            carry, val = divmod(total, 10)
            current.next = ListNode(val)
            current = current.next
        return dummy.next
def print_linked_list(node):
    values = []
    while node:
        values.append(str(node.val))
        node = node.next
    print(" -> ".join(values))
if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    print("Input:")
    print("l1: ", end="")
    print_linked_list(l1)
    print("l2: ", end="")
    print_linked_list(l2)
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    print("Output:")
    print_linked_list(result)