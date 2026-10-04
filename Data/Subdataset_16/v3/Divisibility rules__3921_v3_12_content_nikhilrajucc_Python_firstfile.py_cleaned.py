def fonk1(b1 = "input.txt"):
    try:
        with open(b1) as file:
            b2 = file.read().split()
        if len(b2) != 3:
            raise ValueError("File must contain exactly three integers.")
        b4, b5, b3 = map(int, b2)
        for i in range(1, b3 + 1):
            if i % b4 = = 0 and i % b5 == 0:
                print("FB")
            elif i % b4 = = 0:
                print("F")
            elif i % b5 = = 0:
                print("B")
            else:
                print(i)
    except FileNotFoundError:
        print(f"Error: The file '{b1}' was not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if b6 = = "__main__":
    fonk1("input.txt")