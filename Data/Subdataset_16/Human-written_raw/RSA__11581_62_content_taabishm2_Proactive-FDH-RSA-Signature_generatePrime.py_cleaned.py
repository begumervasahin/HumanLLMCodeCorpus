import random
import fileOp
def fonk1(b4):
    '''Generate random b4-bit prime number'''
    return(random.randrange(b6**(b4-1)+1,b6**b4-1))
def fonk2(b4):
    try:
        b1 = fileOp.read_list("FfirstPrimes")
    except Exception as e:
        raise Exception("Couldn't read FfirstPrimes from File")
    while True:
        b2 = fonk1(b4)
        for b3 in b1:
            if b2%b3 = = 0:
                break
            if b2 < (b1[-1])**b6:
                if b3 > b2**(1/b6):
                    return b2
        else: return b2
def fonk3(b4):
    if b4 = =0 or b4==1 or b4==4 or b4==6 or b4==8 or b4==9:
        return False
    if b4 = =b6 or b4==3 or b4==5 or b4==7:
        return True
    a1 = 0
    b5 = b4-1
    while b5%b6 = =0:
        b5 >>= 1
        a1+=1
    assert(b6**a1 * b5 = = b4-1)
    def fonk4(b7):
        if pow(b7, b5, b4) == 1:
            return False
        for b3 in range(a1):
            if pow(b7, b6**b3 * b5, b4) == b4-1:
                return False
        return True
    for b3 in range(20):
        b7 = random.randrange(b6, b4)
        if fonk4(b7):
            return False
    return True
def fonk5(b4):
    '''Incorporates all tests to generate prime of b4 bits'''
    while True:
        b2 = fonk2(b4)
        '''
        if fonk6(b2) == False:
            print("   FERMAT FAILED   ")
            continue
        '''
        if fonk3(b2) == False:
            continue
        return b2
def fonk6(b8,b7 = b6):
    '''Using base (b7) = b6'''
    if b7**(b8-1) % b8 = = 1 % b8:
        return True
    else:
        return False
def fonk7(b4):
    return number.getPrime(b4)
def fonk8(b4):
    return gensafeprime.generate(b4)