import misc
import permutations
def fonk1(key):
    b1 = []
    b2 = misc.hex_to_bits(key)
    b2 = ''.join([b2[b4:b4 + 7] for b4 in range(0, len(b2), 8)])
    b5, b3 = b2[:int(len(b2) / 2)], b2[
                                                                             int(len(b2) / 2):]
    for b4 in range(16):
        if b4 = = 0 \
                or b4 = = 1 \
                or b4 = = 8 \
                or b4 = = 15:
            b5 = misc.left_shift(b5, 1)
            b3 = misc.left_shift(b3, 1)
        else:
            b5 = misc.left_shift(b5, 2)
            b3 = misc.left_shift(b3, 2)
        b1.append(permutations.permutation(b5 + b3, "compression"))
    return b1