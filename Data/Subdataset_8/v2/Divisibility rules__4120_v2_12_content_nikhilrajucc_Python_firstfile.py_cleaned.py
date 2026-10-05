def load(filename="input.txt"):
    with open(filename, 'r') as file:
        lines = file.readlines()
    fizz, buzz, end = map(int, lines[0].split())
    for i in range(1, end + 1):
        if i % fizz == 0 and i % buzz == 0:
            print("FB")
        elif i % fizz == 0:
            print("F")
        elif i % buzz == 0:
            print("B")
        else:
            print(i)
load()