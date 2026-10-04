class Solution:
    def search(self, A, B):
        def find_break_point(start, end, A):
            if len(A) < 3:
                return start
            mid = start + (end - start)
            if A[mid] < A[mid - 1] and A[mid] < A[mid + 1]:
                return mid
            elif A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
                return mid
            if A[mid] > A[end]:
                return find_break_point(mid, end, A)
            elif A[mid] < A[start]:
                return find_break_point(start, mid, A)
            else:
                return -1
        def binary_search(start, end, target, A):
            if start > end:
                return -1
            mid = start + (end - start)
            if target == A[mid]:
                return mid
            if target > A[mid]:
                return binary_search(mid + 1, end, target, A)
            else:
                return binary_search(start, mid - 1, target, A)
        target = B
        break_point = find_break_point(0, len(A) - 1, A)
        if break_point == -1:
            return binary_search(0, len(A) - 1, target, A)
        index = binary_search(0, break_point - 1, target, A)
        if index == -1:
            return binary_search(break_point, len(A) - 1, target, A)
        return index