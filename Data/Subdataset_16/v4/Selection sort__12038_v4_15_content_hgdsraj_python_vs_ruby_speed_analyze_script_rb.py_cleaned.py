def fonk1(filename):
    with open(filename) as f:
        b1 = f.readlines()
    b2 = []
    for line in b1:
        if "real" in line:
            b3 = float(line.split()[1][:-1]) / 1000
            b2.append(b3)
    return b2
def fonk2(b2):
    return sum(b2) / len(b2) if b2 else 0
def fonk3():
    b2 = fonk1('ruby_res.txt')
    b4 = fonk2(b2)
    print("The average was")
    print(f"{b4:.3f} seconds")
if b5 = = "__main__":
    fonk3()