def fonk1(n, b1 = 0, sol=[]):
    if b1 = = n:
        print(''.join(sol))
    else:
        for x in {'0', '1', '2', '3'}:
            if b1 = = 0 or (x != str(int(sol[b1-1]) + 1) and x != str(int(sol[b1-1]) - 1)):
                sol.append(str(x))
                fonk1(n, b1 + 1, sol)
                sol.pop()
fonk1(6)