def generate_strings(n, i=0, sol=[]):
    if i == n:
        print(''.join(sol))
    else:
        for x in {'0', '1', '2', '3'}:
            if i == 0 or (x != str(int(sol[i-1]) + 1) and x != str(int(sol[i-1]) - 1)):
                sol.append(str(x))
                generate_strings(n, i + 1, sol)
                sol.pop()
generate_strings(6)