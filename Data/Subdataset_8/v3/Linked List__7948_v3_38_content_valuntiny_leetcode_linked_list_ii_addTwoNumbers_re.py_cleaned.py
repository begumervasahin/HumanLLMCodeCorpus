class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        result_root = ListNode(0)
        result_ptr = result_root
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            result_ptr.next = ListNode(carry % 10)
            carry
            result_ptr = result_ptr.next
        return result_root.next
def create_linked_list(values):
    head = ListNode(0)
    current = head
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return head.next
def print_linked_list(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()
if __name__ == "__main__":
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    print_linked_list(result)