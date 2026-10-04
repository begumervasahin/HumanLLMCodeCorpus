def load(filename="input.txt"):
    with open(filename, 'r') as file:
        data = file.read().split()
    fizz = int(data[0])
    buzz = int(data[1])
    end = int(data[2])
    for i in range(1, end + 1):
        if i % fizz == 0 and i % buzz == 0:
            print("FB")
        elif i % fizz == 0:
            print("F")
        elif i % buzz == 0:
            print("B")
        else:
            print(i)
load("input.txt")