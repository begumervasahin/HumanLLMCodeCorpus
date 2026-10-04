class Solution:
    def search(self, A, B):
        def find_break_point(start, end, A):
            while start <= end:
                if A[start] <= A[end]:
                    return start
                mid = start + (end - start)
                if A[mid] > A[mid + 1]:
                    return mid + 1
                if A[mid] < A[mid - 1]:
                    return mid
                if A[mid] > A[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1
        def binary_search(start, end, target, A):
            while start <= end:
                mid = start + (end - start)
                if A[mid] == target:
                    return mid
                if A[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1
        break_point = find_break_point(0, len(A) - 1, A)
        if break_point == -1:
            return binary_search(0, len(A) - 1, B, A)
        if B >= A[0] and B <= A[break_point - 1]:
            return binary_search(0, break_point - 1, B, A)
        else:
            return binary_search(break_point, len(A) - 1, B, A)
