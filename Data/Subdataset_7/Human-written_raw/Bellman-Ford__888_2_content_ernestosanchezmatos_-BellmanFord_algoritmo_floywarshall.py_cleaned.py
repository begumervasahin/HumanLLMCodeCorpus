import numpy
a1 = 99999
a2 = 0
b1 = input(
    "Choose the file (1 - Graph without Negative Cycles or 2 - Graph with Negative Cycles):")
b2 = None
if int(b1) == 1:
      b2 = open("input.txt", "r")
elif int(b1) == 2:
      b2 = open("inputNegativeCycle.txt", "r")
b3 = b2.readlines()
b4 = []
for b5 in range(len(b3)):
    if b5 = = 0:
        a2 = int(b3[b5])
    else:
        b6 = [int(elem.strip()) if elem.strip() !=
               'a1' else a1 for elem in str(b3[b5]).split(',')]
        b4.append(b6)
def fonk1(b4):
    for k in range(a2):
        for b5 in range(a2):
            for j in range(a2):
                if b4[b5][j] > b4[b5][k] + b4[k][j]:
                    b4[b5][j] = b4[b5][k] + b4[k][j]
    for b5 in range(a2):
        if (b4[b5][b5] < 0):
            print("Existis Negative Cycle on Vertice(s): " + str(b5))
print("Vertices: " + str(a2))
print(b4)
fonk1(b4)
print(b4)
b2 = open("output.txt", "w")
for elem in b4:
    b2.write(str(elem)+"\n")
b2.close()