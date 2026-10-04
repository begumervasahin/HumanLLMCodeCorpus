def xor(a, b):
    result = []
    for i in range(1, len(b)):
        result.append('0' if a[i] == b[i] else '1')
    return ''.join(result)
def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[:pick]
    result = ""
    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
            result += "1"
        else:
            tmp = xor('0' * pick, tmp) + dividend[pick]
            result += "0"
        pick += 1
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
        result += "1"
    else:
        tmp = xor('0' * pick, tmp)
        result += "0"
    return result, tmp
def main():
    data = "1001110"
    key = "1011"
    result, remainder = mod2div(data, key)
    print("Data:", data)
    print("Key:", key)
    print("Result:", result)
    print("Remainder:", remainder)
if __name__ == "__main__":
    main()