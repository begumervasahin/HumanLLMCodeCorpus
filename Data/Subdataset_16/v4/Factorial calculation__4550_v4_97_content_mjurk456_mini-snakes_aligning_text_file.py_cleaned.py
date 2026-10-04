def fonk1(b6, b1, b7):
    if b1 = = 'r':
        b2 = '{:>'
    elif b1 = = 'l':
        b2 = '{:'
    elif b1 = = 'c':
        b2 = '{:^'
    else:
        raise ValueError("Invalid alignment option. Use 'r', 'l', or 'c'.")
    b2 += f"{b7}}"
    try:
        with open(b6, 'r') as file:
            for b3 in file:
                b3 = b3.rstrip('\n')
                while len(b3) > b7:
                    b4 = b3[:b7].rfind(' ')
                    if b4 = = -1:
                        b4 = b7
                    print(b2.format(b3[:b4].rstrip()))
                    b3 = b3[b4:].lstrip()
                print(b2.format(b3))
    except FileNotFoundError:
        print(f"Error: The file '{b6}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
if b5 = = "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python script.py <b6> <alignment> <b7>")
        sys.exit(1)
    b6 = sys.argv[1]
    b1 = sys.argv[2]
    try:
        b7 = int(sys.argv[3])
    except ValueError:
        print("Error: Line length must be an integer.")
        sys.exit(1)
    fonk1(b6, b1, b7)