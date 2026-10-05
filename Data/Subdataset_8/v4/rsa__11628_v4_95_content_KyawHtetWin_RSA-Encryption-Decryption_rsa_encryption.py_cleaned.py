
p = 43
q = 59
n = p * q
e = 13
user_message = input("\nEnter your message: ").upper()
user_messages = list(user_message)
print("User message as list of characters:", user_messages)
msg_integers = []
for um in user_messages:
    for number in str(ord(um) - ord('A')):
        msg_integers.append(number)
print("Message integers:", msg_integers)
block_size = len(str(n))
print("Block Size:", block_size)
blocked_msg_integers = [msg_integers[i * block_size:(i + 1) * block_size] for i in range((len(msg_integers) + block_size - 1)
print("Blocked message integers:", blocked_msg_integers)
encrypted_messages = []
for msg_integers in blocked_msg_integers:
    if len(msg_integers) != block_size:
        for i in range(1, (block_size - len(msg_integers)) + 1):
            msg_integers.append(0)
    integers_string = ''
    for msg_int in msg_integers:
        integers_string += str(msg_int)
    encrypted_messages.append((int(integers_string) ** e) % n)
print("Encrypted messages:", encrypted_messages)
encrypted_int_string = ''
for encrypted_message in encrypted_messages:
    encrypted_int_string += str(encrypted_message)
print("\nEncrypted Messages:", encrypted_int_string)