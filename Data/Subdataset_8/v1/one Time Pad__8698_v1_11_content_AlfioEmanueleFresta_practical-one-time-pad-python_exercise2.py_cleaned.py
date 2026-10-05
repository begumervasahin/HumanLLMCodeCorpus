
def strxor(a, b):
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])
def intercept_in():
    return raw_input("Enter input: ")
def intercept_out(data):
    print("Intercepted data:", data)
if __name__ == "__main__":
    x = intercept_in()
    y = x
    intercept_out(y)