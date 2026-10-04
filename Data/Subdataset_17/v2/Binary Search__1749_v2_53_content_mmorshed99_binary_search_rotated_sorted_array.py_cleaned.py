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
            elif A[mid] > A[end]:
                return find_break_point(mid, end, A)
            elif A[mid] < A[start]:
                return find_break_point(start, mid, A)
            else:
                return -1
        def binary_search(start, end, target, A):
            if end - start < 3:
                if target == A[start]:
                    return start
                elif target == A[end]:
                    return end
                else:
                    return -1
            mid = start + (end - start)
            if target == A[mid]:
                return mid
            elif target > A[mid]:
                return binary_search(mid + 1, end, target, A)
            else:
                return binary_search(start, mid - 1, target, A)
        target = B
        break_point = find_break_point(0, len(A) - 1, A)
        if break_point == -1:
            return binary_search(0, len(A) - 1, target, A)
        else:
            left_search = binary_search(0, break_point - 1, target, A)
            if left_search != -1:
                return left_search
            return binary_search(break_point, len(A) - 1, target, A)
if __name__ == "__main__":
    solution = Solution()
    A = [4, 5, 6, 7, 0, 1, 2]
    B = 1
    result = solution.search(A, B)
    print(f"Index of target {B}: {result}")