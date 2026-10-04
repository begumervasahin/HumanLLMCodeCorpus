def xor(a, b):
    return ''.join('0' if a[i] == b[i] else '1' for i in range(1, len(b)))
def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[:pick]
    result = []
    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
            result.append('1')
        else:
            tmp = xor('0' * pick, tmp) + dividend[pick]
            result.append('0')
        pick += 1
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
        result.append('1')
    else:
        tmp = xor('0' * pick, tmp)
        result.append('0')
    return ''.join(result), tmp
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