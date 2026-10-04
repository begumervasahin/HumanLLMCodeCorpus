class Solution:
    def search(self, A, B):
        def find_break_point(start, end, A):
            if len(A) < 3:
                return start
            while start <= end:
                mid = start + (end - start)
                if mid > 0 and A[mid] < A[mid - 1]:
                    return mid
                elif A[mid] >= A[start]:
                    if A[mid] > A[end]:
                        start = mid + 1
                    else:
                        break
                else:
                    end = mid - 1
            return start
        def binary_search(start, end, target, A):
            while start <= end:
                mid = start + (end - start)
                if A[mid] == target:
                    return mid
                elif A[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1
        target = B
        n = len(A)
        break_point = find_break_point(0, n - 1, A)
        if break_point == 0:
            return binary_search(0, n - 1, target, A)
        elif target >= A[0]:
            return binary_search(0, break_point - 1, target, A)
        else:
            return binary_search(break_point, n - 1, target, A)
if __name__ == "__main__":
    solution = Solution()
    A = [4, 5, 6, 7, 0, 1, 2]
    B = 1
    result = solution.search(A, B)
    print(f"Index of target {B}: {result}")