def fonk1(n, k, b1 = 0, tot1 = 0, sol = []) :
    if b1 = = n :
        print(''.join(sol))
    else:
        sol.append('0')
        fonk1(n, k, b1 + 1, tot1, sol)
        sol.pop()
        if tot1 < k:
            sol.append('1')
            fonk1(n, k, b1 + 1, tot1 + 1, sol)
            sol.pop()
fonk1(4,1)