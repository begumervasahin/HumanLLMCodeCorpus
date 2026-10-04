
class class1(Exception):
    pass
class class2(Exception):
    pass
def fonk1(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()
    except Exception as error:
        raise class1(f"Failed to read from '{file_path}': {error}")
def fonk2(write_mode, append, file_path, data):
    b1 = 'a' if append else 'w'
    try:
        with open(file_path, b1) as file:
            for item in data:
                file.write(f"{item}\n")
    except Exception as error:
        raise class1(f"Failed to write to '{file_path}': {error}")
def fonk3(strict, lines):
    b2 = []
    for line in lines:
        try:
            b2.append(int(line))
        except ValueError:
            if strict:
                raise class2(f"Cannot convert '{line}' to an integer.")
    return b2