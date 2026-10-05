
p = 43
q = 59
n = p * q
e = 13
user_message = input("\nEnter your message: ").upper()
user_characters = list(user_message)
print("User message as list of characters:", user_characters)
msg_integers = []
for char in user_characters:
    for num in str(ord(char) - ord('A')):
        msg_integers.append(num)
print("Message integers:", msg_integers)
block_size = len(str(n))
print("Block Size:", block_size)
blocked_msg_integers = [msg_integers[i * block_size:(i + 1) * block_size] for i in range((len(msg_integers) + block_size - 1)
print("Blocked message integers:", blocked_msg_integers)
encrypted_messages = []
for block in blocked_msg_integers:
    if len(block) != block_size:
        for i in range(1, (block_size - len(block)) + 1):
            block.append(0)
    integers_string = ''.join(block)
    encrypted_messages.append((int(integers_string) ** e) % n)
print("Encrypted messages:", encrypted_messages)
encrypted_string = ''.join(map(str, encrypted_messages))
print("\nEncrypted Messages:", encrypted_string)