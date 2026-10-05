import numpy as np
def primegen():
    bits = int(input('How many bits? '))
    final = 2 ** bits
    ints_to_final = np.array(list(range(2, final + 1)))
    index = 0
    while index < len(ints_to_final):
        del_vect = np.zeros_like(ints_to_final)
        for i in range(len(ints_to_final)):
            if ints_to_final[i] == ints_to_final[index]:
                del_vect[i] = 0
            else:
                if ints_to_final[i] % ints_to_final[index] == 0:
                    del_vect[i] = ints_to_final[i]
                else:
                    del_vect[i] = 0
        ints_to_final = ints_to_final - del_vect
        ints_to_final = ints_to_final[ints_to_final != 0]
        index = index + 1
    random1 = int(np.random.choice(ints_to_final, 1))
    random2 = int(np.random.choice(ints_to_final, 1))
    print(f'(Hidden) P Value: {int(random1)}')
    print(f'(Hidden) Q Value: {int(random2)}')
    return random1, random2
if __name__ == "__main__":
    primegen()