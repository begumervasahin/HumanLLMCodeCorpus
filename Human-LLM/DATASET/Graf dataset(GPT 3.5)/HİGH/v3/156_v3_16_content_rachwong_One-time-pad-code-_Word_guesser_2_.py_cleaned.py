import enchant
b1 = enchant.Dict("en_US")
b2 = [
    '7FC84F8DD054A217B29110BD3B02A4AEFF2E5E3A92B4D9C0AC44',
    '7BC455848307A01FB8930FF83044E5A5E16B537292ECC7D2A144',
    '6DC9509BD04EB956B7D410F83716E1BDAD2F487982A1D5DDAC44',
    '7BC04D9C9C42AC04B99A17BD2305F7E9FE24076983A5D3D8A144',
    '6ACE548D9F49AF56BD9A0CEA2744E5A5E16B547F94BED5C7AB44',
    '7ED4578E9955AF56BF8743F53105F6ADAD22493A99A3C2C7B044',
    '6ACE548DD045A304B28743FE350AA4BAE226426884ADC5DFAC44'
]
b3 = [[int(hex_str[i:i+2], 16) for i in range(0, len(hex_str), 2)] for hex_str in b2]
b4 = [0x39]
b5 = [0xac, 0xad, 0xa1, 0xa2, 0xa3, 0xa5, 0xa6, 0xa7]
b6 = [0x27, 0x26, 0x25, 0x24, 0x23, 0x22, 0x21, 0x20, 0x3f, 0x3e, 0x3d, 0x3c,
         0x3b, 0x3a, 0x39, 0x38]
b7 = [0xef, 0xe9, 0xe8, 0xeb, 0xea, 0xfd, 0xfe, 0xf4, 0xf7]
for hex_list in b3:
    b8 = hex_list
    b9 = []
    for char1_val in b4:
        b10 = []
        b11 = chr(hex_list[0] ^ char1_val)
        for char2_val in b5:
            b12 = chr(hex_list[1] ^ char2_val)
            for char3_val in b6:
                b13 = chr(hex_list[2] ^ char3_val)
                for char4_val in b7:
                    b14 = chr(hex_list[3] ^ char4_val)
                    if b1.check(b11 + b12 + b13 + b14):
                        b9.append(b11 + b12 + b13 + b14)
    print('\n'.join(b9))