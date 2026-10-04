
class class1(Exception):
    pass
class class2(Exception):
    pass
def fonk1(file_path):
    try:
        with open(file_path, 'r') as file:
            b1 = file.read().splitlines()
        return b1
    except Exception as e:
        raise class1(f"Error reading the file: {e}")
def fonk2(write_mode, append, file_path, data):
    b2 = 'a' if append else 'w'
    try:
        with open(file_path, b2) as file:
            for item in data:
                file.write(f"{item}\n")
    except Exception as e:
        raise class1(f"Error writing to the file: {e}")
def fonk3(strict, b1):
    b3 = []
    for line in b1:
        try:
            b3.append(int(line))
        except ValueError:
            if strict:
                raise class2(f"Cannot convert '{line}' to an integer.")
            else:
                continue
    return b3