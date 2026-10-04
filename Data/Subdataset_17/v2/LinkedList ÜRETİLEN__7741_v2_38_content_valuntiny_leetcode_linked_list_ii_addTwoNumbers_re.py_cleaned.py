class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = ListNode(0)
        current = root
        while l1 or l2 or carry:
            sum_value = carry
            if l1:
                sum_value += l1.val
                l1 = l1.next
            if l2:
                sum_value += l2.val
                l2 = l2.next
            carry = sum_value
            current.next = ListNode(sum_value % 10)
            current = current.next
        return root.next
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
    print("Input:")
    print("l1: ", end="")
    print_linked_list(l1)
    print("l2: ", end="")
    print_linked_list(l2)
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    print("Output:")
    print_linked_list(result)