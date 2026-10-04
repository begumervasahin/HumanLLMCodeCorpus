def fonk1(n, k):
    def fonk2(b1, tot1, sol):
        if b1 = = n:
            print(''.join(sol))
        else:
            sol.append('0')
            fonk2(b1 + 1, tot1, sol)
            sol.pop()
            if tot1 < k:
                sol.append('1')
                fonk2(b1 + 1, tot1 + 1, sol)
                sol.pop()
    fonk2(0, 0, [])
fonk1(4, 1)