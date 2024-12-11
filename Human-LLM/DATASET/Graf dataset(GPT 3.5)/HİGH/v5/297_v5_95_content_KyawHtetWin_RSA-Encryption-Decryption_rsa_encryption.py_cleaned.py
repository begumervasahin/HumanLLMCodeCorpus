
a1 = 43
a2 = 59
b1 = a1 * a2
a3 = 13
b2 = input("\nEnter your message: ").upper()
b3 = list(b2)
print("User message as list of characters:", b3)
b4 = []
for char in b3:
    for num in str(ord(char) - ord('A')):
        b4.append(num)
print("Message integers:", b4)
b5 = len(str(b1))
print("Block Size:", b5)
b6 = [b4[i * b5:(i + 1) * b5] for i in range((len(b4) + b5 - 1)
print("Blocked message integers:", b6)
b7 = []
for block in b6:
    if len(block) != b5:
        for i in range(1, (b5 - len(block)) + 1):
            block.append(0)
    b8 = ''.join(block)
    b7.append((int(b8) ** a3) % b1)
print("Encrypted messages:", b7)
b9 = ''.join(map(str, b7))
print("\nEncrypted Messages:", b9)