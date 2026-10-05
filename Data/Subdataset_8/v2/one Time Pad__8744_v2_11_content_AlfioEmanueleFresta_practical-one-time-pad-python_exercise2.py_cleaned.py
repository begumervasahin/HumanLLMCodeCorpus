def str_xor(a, b):
    return "".join([chr(ord(x) ^ ord(y)) for x, y in zip(a, b)])
def read_user_input(prompt="Enter input: "):
    return input(prompt)
def print_intercepted_data(data):
    print("Intercepted data:", data)
if __name__ == "__main__":
    user_input = read_user_input()
    intercepted_data = user_input
    print_intercepted_data(intercepted_data)