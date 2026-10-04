def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)
def mod2div(divident, divisor):
    result = ""
    pick = len(divisor)
    tmp = divident[0 : pick]
    while pick < len(divident):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + divident[pick]
            result = result + "1"
        else:
            tmp = xor('0'*pick, tmp) + divident[pick]
            result = result + "0"
        pick += 1
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
        result = result + "1"
    else:
        tmp = xor('0'*pick, tmp)
        result = result + "0"
    print ("Result is: ", result)
    print ("Reminder is :", tmp)
data = "1001110"
key = "1011"
mod2div(data, key)