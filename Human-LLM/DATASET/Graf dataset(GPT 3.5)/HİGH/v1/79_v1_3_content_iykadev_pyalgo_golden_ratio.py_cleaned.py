import cProfile
def fonk1(n):
    a1 = 1
    a2 = 1
    for i in range(2, n):
        b1 = a1 + a2
        a1 = a2
        a2 = b1
        b2 = a2 / a1
        print(b2)
def fonk2(n):
    fonk1(n)
if b3 = = "__main__":
    cProfile.run("fonk2(1476)", b4 = "profile_results.txt")