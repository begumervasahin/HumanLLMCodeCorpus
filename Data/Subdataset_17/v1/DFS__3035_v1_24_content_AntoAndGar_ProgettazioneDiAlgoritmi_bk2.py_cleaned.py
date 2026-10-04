def generate_binary_strings(n, k):
    def backtrack(i, tot1, sol):
        if i == n:
            print(''.join(sol))
        else:
            sol.append('0')
            backtrack(i + 1, tot1, sol)
            sol.pop()
            if tot1 < k:
                sol.append('1')
                backtrack(i + 1, tot1 + 1, sol)
                sol.pop()
    backtrack(0, 0, [])
generate_binary_strings(4, 1)