import cProfile
def fonk1(n):
    if n <= 1:
        return n
    else:
        return fonk1(n - 1) + fonk1(n - 2)
def fonk2(limit):
    for n in range(1, limit + 1):
        b1 = fonk1(n)
        print(f"{n}\t{b1}")
if b2 = = "__main__":
    cProfile.run("fonk2(47)", b3 = "profile_results.txt")