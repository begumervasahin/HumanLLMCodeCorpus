def generate_strings(n, i=0, sol=None):
    if sol is None:
        sol = []
    if i == n:
        print(''.join(sol))
        return
    for x in {'0', '1', '2', '3'}:
        if i == 0 or not are_consecutive(sol[i-1], x):
            sol.append(x)
            generate_strings(n, i + 1, sol)
            sol.pop()
def are_consecutive(a, b):
    return abs(int(a) - int(b)) == 1
generate_strings(6)