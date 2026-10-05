import enchant
english_dict = enchant.Dict("en_US")
char_sets = {
    "char1": [0x39],
    "char2": [0xac, 0xad, 0xa1, 0xa2, 0xa3, 0xa5, 0xa6, 0xa7],
    "char3": [0x27, 0x26, 0x25, 0x24, 0x23, 0x22, 0x21, 0x20, 0x3f, 0x3e, 0x3d, 0x3c,
              0x3b, 0x3a, 0x39, 0x38],
    "char4": [0xef, 0xe9, 0xe8, 0xeb, 0xea, 0xfd, 0xfe, 0xf4, 0xf7]
}
ciphertexts = [
    '7FC84F8DD054A217B29110BD3B02A4AEFF2E5E3A92B4D9C0AC44',
    '7BC455848307A01FB8930FF83044E5A5E16B537292ECC7D2A144',
    '6DC9509BD04EB956B7D410F83716E1BDAD2F487982A1D5DDAC44',
    '7BC04D9C9C42AC04B99A17BD2305F7E9FE24076983A5D3D8A144',
    '6ACE548D9F49AF56BD9A0CEA2744E5A5E16B547F94BED5C7AB44',
    '7ED4578E9955AF56BF8743F53105F6ADAD22493A99A3C2C7B044',
    '6ACE548DD045A304B28743FE350AA4BAE226426884ADC5DFAC44'
]
def chunk_string(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]
for i, cipher_chunk in enumerate(zip(*[chunk_string(ciphertext, 2) for ciphertext in ciphertexts])):
    for char1 in char_sets['char1']:
        for char2 in char_sets['char2']:
            for char3 in char_sets['char3']:
                for char4 in char_sets['char4']:
                    decrypted = ''.join([chr(int(chunk, 16) ^ key) for chunk, key in zip(cipher_chunk, [char1, char2, char3, char4])])
                    if english_dict.check(decrypted):
                        print("Decrypted text:", decrypted)