
p = 43
q = 59
n = p * q
e = 13
def get_user_input():
    user_message = input("\nEnter your message: ").upper()
    print("User Message:", user_message)
    return user_message
def convert_to_integers(user_message):
    msg_integers = [str(ord(character) - ord('A')) for character in user_message]
    print("Message Integers:", msg_integers)
    return msg_integers
def determine_block_size():
    block_size = len(str(n))
    print("Block Size:", block_size)
    return block_size
def split_into_blocks(msg_integers, block_size):
    blocked_msg_integers = [msg_integers[i:i+block_size] for i in range(0, len(msg_integers), block_size)]
    print("Blocked Message Integers:", blocked_msg_integers)
    return blocked_msg_integers
def pad_block(block, block_size):
    if len(block) < block_size:
        block += ['0'] * (block_size - len(block))
    return block
def encrypt_blocks(blocked_msg_integers):
    encrypted_messages = [(int(''.join(block)) ** e) % n for block in blocked_msg_integers]
    print("Encrypted Messages:", encrypted_messages)
    return encrypted_messages
def convert_to_string(encrypted_messages):
    encrypted_int_string = ''.join(map(str, encrypted_messages))
    print("\nEncrypted Messages:", encrypted_int_string)
    return encrypted_int_string
def main():
    user_message = get_user_input()
    msg_integers = convert_to_integers(user_message)
    block_size = determine_block_size()
    blocked_msg_integers = split_into_blocks(msg_integers, block_size)
    padded_blocks = [pad_block(block, block_size) for block in blocked_msg_integers]
    encrypted_messages = encrypt_blocks(padded_blocks)
    convert_to_string(encrypted_messages)
if __name__ == "__main__":
    main()