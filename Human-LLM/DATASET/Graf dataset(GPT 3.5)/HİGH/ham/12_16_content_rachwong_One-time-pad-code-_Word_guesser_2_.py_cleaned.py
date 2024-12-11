import enchant
b1 = enchant.Dict("en_US")
a1 = 2
b2 = '7FC84F8DD054A217B29110BD3B02A4AEFF2E5E3A92B4D9C0AC44'
b3 = [b2[i:i+a1] for i in range(0, len(b2), a1)]
b4 = '7BC455848307A01FB8930FF83044E5A5E16B537292ECC7D2A144'
b5 = [b4[i:i+a1] for i in range(0, len(b4), a1)]
b6 = '6DC9509BD04EB956B7D410F83716E1BDAD2F487982A1D5DDAC44'
b7 = [b6[i:i+a1] for i in range(0, len(b6), a1)]
b8 = '7BC04D9C9C42AC04B99A17BD2305F7E9FE24076983A5D3D8A144'
b9 = [b8[i:i+a1] for i in range(0, len(b8), a1)]
b10 = '6ACE548D9F49AF56BD9A0CEA2744E5A5E16B547F94BED5C7AB44'
b11 = [b10[i:i+a1] for i in range(0, len(b10), a1)]
b12 = '7ED4578E9955AF56BF8743F53105F6ADAD22493A99A3C2C7B044'
b13 = [b12[i:i+a1] for i in range(0, len(b12), a1)]
b14 = '6ACE548DD045A304B28743FE350AA4BAE226426884ADC5DFAC44'
b15 = [b14[i:i+a1] for i in range(0, len(b14), a1)]
b16 = [0x39]
b17 = [0x3d,0x3c,0x3a,0x39,0x38,0x2f,0x2e,0x2c,0x2b,0x29,0x28]
b18 = [0xac,0xad,0xa1,0xa2,0xa3,0xa5,0xa6,0xa7]
b19 = [0x27,0x26,0x25,0x24,0x23,0x22,0x21,0x20,0x3f,0x3e,0x3d,0x3c,
       0x3b,0x3a,0x39,0x38]
b20 = [0xef,0xe9,0xe8,0xeb,0xea,0xfd,0xfe,0xf4,0xf7]
for one in range(len(b16)):
    b21 = one
    b22 = int('0x'+b11[0],16)^b16[one]
    b23 = int('0x'+b5[0],16)^b16[one]
    b22 = chr(b22)
    b23 = chr(b23)
    print('trying this b22: '+ b22)
    b24 = [b22]
    b25 = [b23]
    for two in range(len(b18)):
        b26 = int('0x'+b11[1],16)^b18[two]
        b26 = chr(b26)
        b27 = int('0x'+b5[1],16)^b18[two]
        b27 = chr(b27)
        for three in range(len(b19)):
            b28 = int('0x'+b11[2],16)^b19[three]
            b28 = chr(b28)
            b29 = int('0x'+b5[2],16)^b19[three]
            b29 = chr(b29)
            for four in range(len(b20)):
                b30 = int('0x'+b11[3],16)^b20[four]
                b30 = chr(b30)
                b31 = int('0x'+b5[3],16)^b20[four]
                b31 = chr(b31)
                if b1.check(str(b22+b26+b28+b30)) == True:
                    print('----')
                    print(b22+b26+b28+b30)
                if b1.check(str(b23+b27+b29+b31)) == True:
                    print(b23+b27+b29+b31)
                    print('----')
    print('-----')
b24 = []
for i in range(len(keys)):
    b22 = int('0x'+b3[i],16)^keys[i]
    b24.append(chr(b22))
print(''.join(b24))