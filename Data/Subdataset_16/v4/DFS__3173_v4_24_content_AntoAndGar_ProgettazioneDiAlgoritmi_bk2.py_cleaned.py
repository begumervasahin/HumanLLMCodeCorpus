def fonk1(n, k):
    def fonk2(b1, total_ones, solution):
        if b1 = = n:
            print(''.join(solution))
            return
        solution.append('0')
        fonk2(b1 + 1, total_ones, solution)
        solution.pop()
        if total_ones < k:
            solution.append('1')
            fonk2(b1 + 1, total_ones + 1, solution)
            solution.pop()
    fonk2(0, 0, [])
fonk1(4, 1)