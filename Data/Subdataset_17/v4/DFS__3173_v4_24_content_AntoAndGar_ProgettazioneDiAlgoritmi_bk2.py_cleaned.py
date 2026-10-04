def generate_binary_strings(n, k):
    def backtrack(index, total_ones, solution):
        if index == n:
            print(''.join(solution))
            return
        solution.append('0')
        backtrack(index + 1, total_ones, solution)
        solution.pop()
        if total_ones < k:
            solution.append('1')
            backtrack(index + 1, total_ones + 1, solution)
            solution.pop()
    backtrack(0, 0, [])
generate_binary_strings(4, 1)