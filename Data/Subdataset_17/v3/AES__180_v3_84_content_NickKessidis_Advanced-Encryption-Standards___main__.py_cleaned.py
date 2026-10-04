import random
def generate_random_128_bit_number():
    return random.randint(2**127, 2**128 - 1)
def generate_random_sbox():
    return [random.randint(2**7, 2**8 - 1) for _ in range(256)]
def convert_to_state_array(number):
    bin_number = bin(number)[2:].zfill(128)
    return [bin_number[i*8:(i+1)*8] for i in range(16)]
def apply_sbox_to_state(state, sbox):
    for i in range(16):
        z = state[i]
        row = int(z[:4], 2)
        col = int(z[4:], 2)
        sbox_value = sbox[(col + row) % 16]
        state[i] = format(sbox_value, '08b')
    return state
if __name__ == "__main__":
    number = generate_random_128_bit_number()
    key = generate_random_128_bit_number()
    print(f"Result of XOR: {bin(number ^ key)}")
    print(f"Plain text: {bin(number)}")
    state = convert_to_state_array(number)
    print("State Array:")
    print(state)
    sbox = generate_random_sbox()
    state = apply_sbox_to_state(state, sbox)
    print("State Array after the Substitution process:")
    print(state)