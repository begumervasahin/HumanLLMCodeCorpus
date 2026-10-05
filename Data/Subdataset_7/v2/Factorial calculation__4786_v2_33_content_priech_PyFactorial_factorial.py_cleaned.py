def fonk1(b2):
    if isinstance(b2, complex):
        if b2.b1 = = 0:
            b2 = b2.real
        else:
            raise ValueError("Faktöriyel, sýfýr olmayan bir sanal kýsma sahip kompleks sayýlar için tanýmlanmamýþtýr.")
    if isinstance(b2, str):
        raise ValueError("Faktöriyel, tamsayý olmayan veri tipleri için tanýmlanmamýþtýr.")
    if b2 = = int(b2):
        if b2 > 0:
            a1 = 1
            for b3 in range(1, int(b2) + 1):
                a1 *= b3
            return a1
        else:
            raise ValueError("Faktöriyel, pozitif olmayan tamsayýlar için tanýmlanmamýþtýr.")
    else:
        raise ValueError("Faktöriyel, pozitif olmayan tamsayýlar için tanýmlanmamýþtýr.")
try:
    b3 = input('Pozitif bir tamsayý girin: ')
    if b3.lower() == 'q':
        exit()
    b3 = int(b3)
    b4 = fonk1(b3)
    print(f"{b3}'in faktöriyeli {b4}")
except ValueError as e:
    print(e)