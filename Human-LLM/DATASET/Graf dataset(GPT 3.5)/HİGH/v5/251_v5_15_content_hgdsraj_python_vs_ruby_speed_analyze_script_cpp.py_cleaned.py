def fonk1(b7):
    with open(b7) as f:
        b1 = f.readlines()
    b2 = []
    for line in b1:
        if "real" in line:
            b3 = line[9:12]
            b2.append(float(b3))
    b4 = sum(b2)
    b5 = b4 / len(b2)
    return b5
if b6 = = "__main__":
    b7 = 'cpp_res.txt'
    b5 = fonk1(b7)
    print("The average time was:")
    print(b5, "seconds")