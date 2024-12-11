
a1 = 43
a2 = 59
b1 = a1 * a2
a3 = 13
b2 = input("\nEnter your message: ").upper()
b3 = list(b2)
print("User message as list of characters:", b3)
b4 = []
for um in b3:
    for number in str(ord(um) - ord('A')):
        b4.append(number)
print("Message integers:", b4)
b5 = len(str(b1))
print("Block Size:", b5)
b6 = [b4[i * b5:(i + 1) * b5] for i in range((len(b4) + b5 - 1)
print("Blocked message integers:", b6)
b7 = []
for b4 in b6:
    if len(b4) != b5:
        for i in range(1, (b5 - len(b4)) + 1):
            b4.append(0)
    b8 = ''
    for msg_int in b4:
        b8 += str(msg_int)
    b7.append((int(b8) ** a3) % b1)
print("Encrypted messages:", b7)
b9 = ''
for encrypted_message in b7:
    b9 += str(encrypted_message)
print("\nEncrypted Messages:", b9)