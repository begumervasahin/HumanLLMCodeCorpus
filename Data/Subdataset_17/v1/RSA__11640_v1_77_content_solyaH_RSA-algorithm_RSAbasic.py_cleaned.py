import math
alphabet = "abcdefghijklmnopqrstuvwxyz"
def EuclidAlgorithm(a, b):
    d, x, y = 0, 1, 0
    if b == 0:
        return d, x, y
    x2, x1, y2, y1 = 1, 0, 0, 1
    while b > 0:
        q = a
        r = a - q * b
        x = x2 - q * x1
        y = y2 - q * y1
        a, b = b, r
        x2, x1 = x1, x
        y2, y1 = y1, y
    d, x, y = a, x2, y2
    return d, x, y
def intToBit(letterNumb, bitLength):
    return '{0:0b}'.format(letterNumb).zfill(bitLength)
def RSA(text, p, q, e, action):
    n = p * q
    phi = (p - 1) * (q - 1)
    smt, u, v = EuclidAlgorithm(phi, e)
    bitLength = int(math.log(len(alphabet), 2)) + 1
    maxBitIntervalLength = int(math.log(n - 1, 2))
    if action == 'e':
        bitStr = ''
        for letter in text:
            letterNumb = alphabet.find(letter) + 1
            bitStr += intToBit(letterNumb, bitLength)
        C = []
        lengthOfCipher = len(bitStr)
        for i in range(lengthOfCipher):
            M = int(bitStr[maxBitIntervalLength * i : maxBitIntervalLength * (i + 1)], 2)
            C.append((M ** e) % n)
        return C
    elif action == 'd':
        d = v % phi
        M = [(code ** d) % n for code in text]
        bitStr = ''
        for i in range(len(M)):
            if i == len(M) - 1:
                length = int(maxBitIntervalLength * (len(M) - 1) / bitLength) + 1
                bitStr += intToBit(M[i], length * bitLength - len(bitStr))
            else:
                bitStr += intToBit(M[i], maxBitIntervalLength)
        decodedText = ''
        lengthOfCipher = len(bitStr)
        for i in range(lengthOfCipher):
            letterNumb = int(bitStr[bitLength * i : bitLength * (i + 1)], 2)
            decodedText += alphabet[letterNumb - 1]
        return decodedText
def main():
    text = 'wonderfull'
    action = 'e'
    p = 17
    q = 31
    e = 7
    result = RSA(text, p, q, e, action)
    print(result)
if __name__ == "__main__":
    main()