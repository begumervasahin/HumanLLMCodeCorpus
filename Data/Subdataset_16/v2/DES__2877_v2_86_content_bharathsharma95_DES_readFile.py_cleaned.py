def fonk1(b1):
    with open(b1, 'rb') as file:
        return list(file.read())
def fonk2():
    b1 = 'path/to/your/file'
    try:
        b2 = fonk1(b1)
        print(b2)
    except FileNotFoundError:
        print(f"Error: The file at {b1} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
if b3 = = "__main__":
    fonk2()