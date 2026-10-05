a1 = 99999
def fonk1(filename):
    with open(filename, "r") as file:
        b1 = file.readlines()
        b2 = int(b1[0])
        b3 = [[int(elem.strip()) if elem.strip() != 'a1' else a1
                  for elem in line.strip().split(',')]
                 for line in b1[1:]]
    return b2, b3
def fonk2(b3, b2):
    for k in range(b2):
        for i in range(b2):
            for j in range(b2):
                if b3[i][j] > b3[i][k] + b3[k][j]:
                    b3[i][j] = b3[i][k] + b3[k][j]
    for i in range(b2):
        if b3[i][i] < 0:
            print("Negative cycle detected on vertex:", i)
def fonk3(b3, filename):
    with open(filename, "w") as file:
        for row in b3:
            file.write(','.join(map(str, row)) + '\n')
def fonk4():
    b4 = input("Choose the file (1 - Graph without Negative Cycles or 2 - Graph with Negative Cycles): ")
    if b4 = = '1':
        b5 = "input.txt"
    elif b4 = = '2':
        b5 = "inputNegativeCycle.txt"
    else:
        print("Invalid b4. Please choose either 1 or 2.")
        return
    b2, b3 = fonk1(b5)
    print("Vertices:", b2)
    print("Graph:")
    for row in b3:
        print(row)
    fonk2(b3, b2)
    print("Resulting Graph:")
    for row in b3:
        print(row)
    b6 = "output.txt"
    fonk3(b3, b6)
    print("Resulting b3 written to", b6)
if b7 = = "__main__":
    fonk4()