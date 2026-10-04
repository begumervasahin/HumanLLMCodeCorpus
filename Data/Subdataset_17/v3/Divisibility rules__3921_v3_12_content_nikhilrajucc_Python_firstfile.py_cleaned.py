def load(filename="input.txt"):
    try:
        with open(filename) as file:
            data = file.read().split()
        if len(data) != 3:
            raise ValueError("File must contain exactly three integers.")
        fizz, buzz, end = map(int, data)
        for i in range(1, end + 1):
            if i % fizz == 0 and i % buzz == 0:
                print("FB")
            elif i % fizz == 0:
                print("F")
            elif i % buzz == 0:
                print("B")
            else:
                print(i)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    load("input.txt")