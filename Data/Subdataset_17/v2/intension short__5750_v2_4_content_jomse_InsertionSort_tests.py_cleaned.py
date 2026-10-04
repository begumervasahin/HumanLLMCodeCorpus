
class FileReadError(Exception):
    pass
class NotIntError(Exception):
    pass
def read_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()
    except Exception as error:
        raise FileReadError(f"Failed to read from '{file_path}': {error}")
def write_file(write_mode, append, file_path, data):
    mode = 'a' if append else 'w'
    try:
        with open(file_path, mode) as file:
            for item in data:
                file.write(f"{item}\n")
    except Exception as error:
        raise FileReadError(f"Failed to write to '{file_path}': {error}")
def convert_lines_to_ints(strict, lines):
    result = []
    for line in lines:
        try:
            result.append(int(line))
        except ValueError:
            if strict:
                raise NotIntError(f"Cannot convert '{line}' to an integer.")
    return result