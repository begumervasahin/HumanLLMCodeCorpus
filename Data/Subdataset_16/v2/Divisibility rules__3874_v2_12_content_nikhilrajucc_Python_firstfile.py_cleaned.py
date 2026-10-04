def fonk1(b1 = "input.txt"):
    try:
        with open(b1) as file:
            b2 = file.read().split()
        b3 = int(b2[0])
        b4 = int(b2[1])
        b5 = int(b2[2])
        for i in range(1, b5 + 1):
            if i % b3 = = 0 and i % b4 == 0:
                print("FB")
            elif i % b3 = = 0:
                print("F")
            elif i % b4 = = 0:
                print("B")
            else:
                print(i)
    except FileNotFoundError:
        print(f"File '{b1}' not found.")
    except (IndexError, ValueError):
        print("Error in reading or parsing the file content.")
if b6 = = "__main__":
    fonk1("input.txt")