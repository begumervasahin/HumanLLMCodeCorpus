import cProfile
def fonk1(a3):
    a1 = 1
    a2 = 1
    for i in range(2, a3):
        b1 = a1 + a2
        a1 = a2
        a2 = b1
        b2 = a2 / a1
        print(b2)
def fonk2():
    a3 = 1476
    fonk1(a3)
if b3 = = "__main__":
    cProfile.run("fonk2()", b4 = "profile_results.txt")