import random
def generate_random_128_bit_number():
    return random.randrange(2**127, 2**128)
def generate_random_sbox():
    return [random.randrange(2**7, 2**8) for _ in range(256)]
def convert_to_state_array(number):
    state = ["0"] * 16
    bin_number = bin(number)[2:].zfill(128)
    for i in range(16):
        state[i] = bin_number[8 * i: 8 * (i + 1)]
    return state
def apply_sbox_to_state(state, sbox):
    for i in range(16):
        z = state[i]
        row = int(z[:4], 2)
        col = int(z[4:], 2)
        state[i] = format(sbox[(col + row) % 16], '08b')
    return state
if __name__ == "__main__":
    number = generate_random_128_bit_number()
    key = generate_random_128_bit_number()
    print("Result of XOR:", bin(number ^ key))
    print("Plain text:", bin(number))
    state = convert_to_state_array(number)
    print("State Array:")
    print(state)
    sbox = generate_random_sbox()
    state = apply_sbox_to_state(state, sbox)
    print("State Array after the Substitution process:")
    print(state)