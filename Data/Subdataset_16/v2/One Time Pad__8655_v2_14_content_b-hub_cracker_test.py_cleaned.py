import sys
def fonk1(b2: int) -> str:
    b1 = ""
    while b2 > 0:
        b2 -= 1
        b1 = chr(ord('A') + b2 % 26) + b1
        b2
    return b1
def fonk2(b3: str) -> None:
    try:
        with open(b3, 'r') as file:
            for line in file:
                try:
                    b2 = int(line.strip())
                    b1 = fonk1(b2)
                    print(f"{b2}: {b1}")
                except ValueError:
                    print(f"Error: Invalid number '{line.strip()}'. Ensure the input file contains integers only.")
    except FileNotFoundError:
        print(f"Error: File '{b3}' not found.")
def fonk3() -> None:
    if len(sys.argv) != 2:
        print("Usage: python script.py <b3>")
        return
    b3 = sys.argv[1]
    fonk2(b3)
if b4 = = "__main__":
    fonk3()