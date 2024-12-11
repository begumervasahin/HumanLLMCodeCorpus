
with open("results/estimated_datafile.js") as file:
    b1 = file.readlines()
    b2 = float(b1[-2].strip().split("=")[1])
    b3 = float(b1[-1].strip().split("=")[1])
def fonk1(x):
    return b3 * (b2 ** x)
def fonk2(x):
    return (210 * (x ** 2) + 1060 * x - 1410) * (10 ** -9)
def fonk3(x):
    return (2650 * (x ** 3) + 1060 * x - 1410) * (10 ** -9)
b4 = {}
b5 = {}
b6 = {}
a1 = 2048
for x in range(4, a1 + 4, 4):
    b4[x] = fonk1(x)
    b5[x] = fonk3(x)
    b6[x] = fonk2(x)
with open("results/quantum_datafile.js", "w") as file:
    file.write("b7 = [\n")
    for x in range(4, a1 + 4, 4):
        file.write('{"bits": ' + str(x) + ', "time": ' + str(b4[x]) + '},\n')
    file.write("];\n")
    file.write("b8 = [\n")
    for x in range(4, a1 + 4, 4):
        file.write('{"bits": ' + str(x) + ', "time": ' + str(b6[x]) + '},\n')
    file.write("];\n")
    file.write("b9 = [\n")
    for x in range(4, a1 + 4, 4):
        file.write('{"bits": ' + str(x) + ', "time": ' + str(b5[x]) + '},\n')
    file.write("];\n")